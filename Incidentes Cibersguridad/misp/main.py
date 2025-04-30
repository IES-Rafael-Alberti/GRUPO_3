import os
import requests
import time
from dotenv import load_dotenv
from pymisp import PyMISP, MISPEvent, MISPAttribute
import urllib3
import sys

# cargar .env
load_dotenv()
misp_url = os.getenv('MISP_URL')
misp_key = os.getenv('MISP_KEY')
misp_verifycert = os.getenv('MISP_VERIFYCERT', 'True').lower() == 'true'
vt_api_key = os.getenv('VT_API_KEY')

# desactivar advertencias de ssl
if not misp_verifycert:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def init_misp_instance(url, key, ssl):
    return PyMISP(url, key, ssl, 'json')

def analyze_url_with_virustotal(url):
    print(f"🔍 Analyzing URL with VirusTotal: {url}")
    headers = {"x-apikey": vt_api_key,"Content-Type": "application/x-www-form-urlencoded"}
    url_vt = "https://www.virustotal.com/api/v3"

    response = requests.post(f"{url_vt}/urls",headers=headers,data=f"url={url}")

    if response.status_code != 200:
        print(f"Failed to submit URL to VirusTotal. Code: {response.status_code}")
        return None

    analysis_url = response.json()["data"]["links"]["self"]

    result = requests.get(analysis_url, headers=headers).json()

    return result

def create_misp_event_from_url(misp, url, analysis):
    event = MISPEvent()
    event.info = f'URL Analysis: {url}'
    event.distribution = 0
    event.analysis = 1
    event.threat_level_id = 3

    new_event = misp.add_event(event)
    event_id = new_event['Event']['id']
    print(f"✅ Event created with ID: {event_id}")

    attribute = MISPAttribute()
    attribute.type = 'url'
    attribute.value = url
    attribute.category = 'Network activity'
    misp.add_attribute(event_id, attribute)

    attributes = analysis.get("data", {}).get("attributes", {})
    stats = attributes.get("stats", {})
    results = attributes.get("last_analysis_results", {})

    malicious_count = stats.get("malicious", 0)
    malicious_engines = [engine for engine, data in results.items() if data.get("category") == "malicious"]

    if malicious_count > 0:
        print(f"⚠️ VirusTotal flagged this URL as malicious by {malicious_count} engine(s).")
        print(f"🚨 Engines: {', '.join(malicious_engines)}")
    else:
        print("✅ Esta URL no fue marcada como maliciosa por VirusTotal.")

    return event_id

def list_misp_events(misp):
    print("\n📋 MISP Event List:")
    events = misp.search_index()
    sorted_events = sorted(events, key=lambda x: x.get('date', ''), reverse=True)

    for e in sorted_events:
        print(f"🆔 ID: {e['id']} | 📅 Date: {e['date']} | 📝 Info: {e['info']} | 🔢 Attributes: {e['attribute_count']}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py https://example.com")
        sys.exit(1)

    url = sys.argv[1]
    misp = init_misp_instance(misp_url, misp_key, misp_verifycert)
    analysis = analyze_url_with_virustotal(url)
    
    if analysis:
        create_misp_event_from_url(misp, url, analysis)
        list_misp_events(misp)
