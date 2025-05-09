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
urls_path = os.getenv('URLS_TXT')

# desactivar advertencias de ssl
if not misp_verifycert:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def init_misp(url, key, ssl):
    return PyMISP(url, key, ssl, 'json')

def analyze_url_with_virustotal(url):
    print(f"Analyzing URL with VirusTotal: {url}")
    headers = {"x-apikey": vt_api_key,"Content-Type": "application/x-www-form-urlencoded"}
    url_vt = "https://www.virustotal.com/api/v3"
    response = requests.post(f"{url_vt}/urls",headers=headers,data=f"url={url}")

    if response.status_code != 200:
        print(f"Failed to submit URL to VirusTotal. Code: {response.status_code}")
        return None

    analysis_url = response.json()["data"]["links"]["self"]
    result = requests.get(analysis_url, headers=headers).json()
    return result

def create_misp_event(misp, url, analysis):
    # Comprobar si ya existe un evento con esa URL
    existing = misp.search(controller='attributes', type_attribute='url', value=url)
    if existing.get('Attribute'):
        print(f"🔁 The URL already exists in MISP. No new event created: {url}")
        return None

    # Obtener análisis de VT
    attributes = analysis.get("data", {}).get("attributes", {})
    stats = attributes.get("stats", {})
    malicious_count = stats.get("malicious", 0)


    # Crear evento
    event = MISPEvent()
    event.info = f'URL Analysis: {url}'
    event.distribution = 0
    event.analysis = 1
    event.threat_level_id = 3

    # Añadir etiqueta antes de subir
    if malicious_count > 0:
        print(f"⚠️ VirusTotal flagged this URL as malicious by {malicious_count} engine(s).")
        event.add_tag('VT:malicious')
    else:
        print("✅ This URL is clean.")
        event.add_tag('VT:clean')

    # Subir evento a MISP
    new_event = misp.add_event(event)
    event_id = new_event['Event']['id']
    print(f"🆕 Event created with ID: {event_id}")

    # Añadir atributo URL
    attribute = MISPAttribute()
    attribute.type = 'url'
    attribute.value = url
    attribute.category = 'Network activity'
    misp.add_attribute(event_id, attribute)

    return event_id

def list_misp_events(misp):
    print("\n📋 MISP Event List:")
    events = misp.search_index()
    sorted_events = sorted(events, key=lambda x: x.get('date', ''), reverse=True)

    for e in sorted_events:
        print(f"🆔 ID: {e['id']} | 📅 Date: {e['date']} | 📝 Info: {e['info']} | 🔢 Attributes: {e['attribute_count']}")

if __name__ == '__main__':
        
    if not urls_path or not os.path.exists(urls_path):
        print(f"File not found: {urls_path}")
        sys.exit(1)

    misp = init_misp(misp_url, misp_key, misp_verifycert)
    
    with open(urls_path, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                print(f"\n🔎 Analizando: {url}")
                analysis = analyze_url_with_virustotal(url)
                if analysis:
                    create_misp_event(misp, url, analysis)

    list_misp_events(misp)
