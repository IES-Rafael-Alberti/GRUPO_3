```bash
Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-09 23:28 CEST
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Nmap scan report for 10.0.2.9
Host is up (0.00060s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 2.9p2 (protocol 1.99)
80/tcp   open  http        Apache httpd 1.3.20 ((Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| vulners: 
|   cpe:/a:apache:http_server:1.3.20: 
|       CVE-2004-0940   7.8     https://vulners.com/cve/CVE-2004-0940
|       CVE-2002-2272   7.8     https://vulners.com/cve/CVE-2002-2272
|       SAINT:CE48F764F3535D6A2E3CBFC45B9F2609  7.5     https://vulners.com/saint/SAINT:CE48F764F3535D6A2E3CBFC45B9F2609        *EXPLOIT*
|       SAINT:B6E89161F5A85A6F227960760297B726  7.5     https://vulners.com/saint/SAINT:B6E89161F5A85A6F227960760297B726        *EXPLOIT*
|       SAINT:66E6068403B214B34CB01EE316C37B76  7.5     https://vulners.com/saint/SAINT:66E6068403B214B34CB01EE316C37B76        *EXPLOIT*
|       SAINT:399EF180849727C5C8C2DB4378F050B0  7.5     https://vulners.com/saint/SAINT:399EF180849727C5C8C2DB4378F050B0        *EXPLOIT*
|       PACKETSTORM:82996       7.5     https://vulners.com/packetstorm/PACKETSTORM:82996       *EXPLOIT*
|       PACKETSTORM:25903       7.5     https://vulners.com/packetstorm/PACKETSTORM:25903       *EXPLOIT*
|       MSF:EXPLOIT-WINDOWS-HTTP-APACHE_CHUNKED-        7.5     https://vulners.com/metasploit/MSF:EXPLOIT-WINDOWS-HTTP-APACHE_CHUNKED- *EXPLOIT*
|       EDB-ID:16782    7.5     https://vulners.com/exploitdb/EDB-ID:16782      *EXPLOIT*
|       CVE-2004-1082   7.5     https://vulners.com/cve/CVE-2004-1082
|       CVE-2003-0993   7.5     https://vulners.com/cve/CVE-2003-0993
|       CVE-2003-0987   7.5     https://vulners.com/cve/CVE-2003-0987
|       CVE-2002-2029   7.5     https://vulners.com/cve/CVE-2002-2029
|       CVE-2002-0843   7.5     https://vulners.com/cve/CVE-2002-0843
|       CVE-2002-0392   7.5     https://vulners.com/cve/CVE-2002-0392
|       CVE-2002-0257   7.5     https://vulners.com/cve/CVE-2002-0257
|       CVE-2002-0061   7.5     https://vulners.com/cve/CVE-2002-0061
|       APACHECHUNK_WIN32       7.5     https://vulners.com/canvas/APACHECHUNK_WIN32    *EXPLOIT*
|       CVE-2003-0542   7.2     https://vulners.com/cve/CVE-2003-0542
|       CVE-2002-0839   7.2     https://vulners.com/cve/CVE-2002-0839
|       SSV:19019       6.8     https://vulners.com/seebug/SSV:19019    *EXPLOIT*
|       CVE-2010-0010   6.8     https://vulners.com/cve/CVE-2010-0010
|       CVE-2002-0840   6.8     https://vulners.com/cve/CVE-2002-0840
|       SSV:66957       5.0     https://vulners.com/seebug/SSV:66957    *EXPLOIT*
|       SSV:4148        5.0     https://vulners.com/seebug/SSV:4148     *EXPLOIT*
|       SSV:20993       5.0     https://vulners.com/seebug/SSV:20993    *EXPLOIT*
|       SSV:20979       5.0     https://vulners.com/seebug/SSV:20979    *EXPLOIT*
|       SSV:20969       5.0     https://vulners.com/seebug/SSV:20969    *EXPLOIT*
|       SSV:17994       5.0     https://vulners.com/seebug/SSV:17994    *EXPLOIT*
|       SSV:14432       5.0     https://vulners.com/seebug/SSV:14432    *EXPLOIT*
|       PACKETSTORM:85018       5.0     https://vulners.com/packetstorm/PACKETSTORM:85018       *EXPLOIT*
|       PACKETSTORM:82197       5.0     https://vulners.com/packetstorm/PACKETSTORM:82197       *EXPLOIT*
|       PACKETSTORM:181059      5.0     https://vulners.com/packetstorm/PACKETSTORM:181059      *EXPLOIT*
|       PACKETSTORM:105672      5.0     https://vulners.com/packetstorm/PACKETSTORM:105672      *EXPLOIT*
|       PACKETSTORM:105591      5.0     https://vulners.com/packetstorm/PACKETSTORM:105591      *EXPLOIT*
|       MSF:AUXILIARY-SCANNER-HTTP-REWRITE_PROXY_BYPASS-        5.0     https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-HTTP-REWRITE_PROXY_BYPASS- *EXPLOIT*
|       EXPLOITPACK:460143F0ACAE117DD79BD75EDFDA154B    5.0     https://vulners.com/exploitpack/EXPLOITPACK:460143F0ACAE117DD79BD75EDFDA154B    *EXPLOIT*
|       EXPLOITPACK:44DAC602FB30402C58970DFAB1C4AF87    5.0     https://vulners.com/exploitpack/EXPLOITPACK:44DAC602FB30402C58970DFAB1C4AF87    *EXPLOIT*
|       EDB-ID:9887     5.0     https://vulners.com/exploitdb/EDB-ID:9887       *EXPLOIT*
|       EDB-ID:17969    5.0     https://vulners.com/exploitdb/EDB-ID:17969      *EXPLOIT*
|       CVE-2011-3368   5.0     https://vulners.com/cve/CVE-2011-3368
|       CVE-2007-6750   5.0     https://vulners.com/cve/CVE-2007-6750
|       CVE-2004-0263   5.0     https://vulners.com/cve/CVE-2004-0263
|       CVE-2003-0460   5.0     https://vulners.com/cve/CVE-2003-0460
|       CVE-2003-0083   5.0     https://vulners.com/cve/CVE-2003-0083
|       CVE-2003-0020   5.0     https://vulners.com/cve/CVE-2003-0020
|       CVE-2002-2103   5.0     https://vulners.com/cve/CVE-2002-2103
|       CVE-2001-1556   5.0     https://vulners.com/cve/CVE-2001-1556
|       CVE-2001-0731   5.0     https://vulners.com/cve/CVE-2001-0731
|       CVE-2001-0730   5.0     https://vulners.com/cve/CVE-2001-0730
|       CVE-2001-0729   5.0     https://vulners.com/cve/CVE-2001-0729
|       SSV:2174        4.7     https://vulners.com/seebug/SSV:2174     *EXPLOIT*
|       CVE-2007-3304   4.7     https://vulners.com/cve/CVE-2007-3304
|       CVE-2002-1658   4.6     https://vulners.com/cve/CVE-2002-1658
|       SSV:71772       4.3     https://vulners.com/seebug/SSV:71772    *EXPLOIT*
|       SSV:2818        4.3     https://vulners.com/seebug/SSV:2818     *EXPLOIT*
|       SSV:2801        4.3     https://vulners.com/seebug/SSV:2801     *EXPLOIT*
|       SSV:24250       4.3     https://vulners.com/seebug/SSV:24250    *EXPLOIT*
|       PACKETSTORM:61420       4.3     https://vulners.com/packetstorm/PACKETSTORM:61420       *EXPLOIT*
|       PACKETSTORM:102234      4.3     https://vulners.com/packetstorm/PACKETSTORM:102234      *EXPLOIT*
|       EXPLOITPACK:683C3B1D02827D6B32706DB1D146B2D8    4.3     https://vulners.com/exploitpack/EXPLOITPACK:683C3B1D02827D6B32706DB1D146B2D8    *EXPLOIT*
|       EDB-ID:17393    4.3     https://vulners.com/exploitdb/EDB-ID:17393      *EXPLOIT*
|       CVE-2011-4317   4.3     https://vulners.com/cve/CVE-2011-4317
|       CVE-2007-6388   4.3     https://vulners.com/cve/CVE-2007-6388
|       CVE-2007-5000   4.3     https://vulners.com/cve/CVE-2007-5000
|       CVE-2006-5752   4.3     https://vulners.com/cve/CVE-2006-5752
|       CVE-2006-3918   4.3     https://vulners.com/cve/CVE-2006-3918
|       CVE-2005-3352   4.3     https://vulners.com/cve/CVE-2005-3352
|       CVE-2002-1233   2.6     https://vulners.com/cve/CVE-2002-1233
|       CVE-2001-1534   2.1     https://vulners.com/cve/CVE-2001-1534
|       1337DAY-ID-9952 0.0     https://vulners.com/zdt/1337DAY-ID-9952 *EXPLOIT*
|       1337DAY-ID-16843        0.0     https://vulners.com/zdt/1337DAY-ID-16843        *EXPLOIT*
|_      1337DAY-ID-16323        0.0     https://vulners.com/zdt/1337DAY-ID-16323        *EXPLOIT*
|_http-trace: TRACE is enabled
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
| http-enum: 
|   /test.php: Test page
|   /icons/: Potentially interesting directory w/ listing on 'apache/1.3.20'
|   /manual/: Potentially interesting directory w/ listing on 'apache/1.3.20'
|_  /usage/: Potentially interesting folder
111/tcp  open  rpcbind     2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1           1024/tcp   status
|_  100024  1           1026/udp   status
139/tcp  open  netbios-ssn Samba smbd (workgroup: MYGROUP)
443/tcp  open  ssl/https   Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_sslv2-drown: ERROR: Script execution failed (use -d to debug)
| ssl-dh-params: 
|   VULNERABLE:
|   Transport Layer Security (TLS) Protocol DHE_EXPORT Ciphers Downgrade MitM (Logjam)
|     State: VULNERABLE
|     IDs:  BID:74733  CVE:CVE-2015-4000
|       The Transport Layer Security (TLS) protocol contains a flaw that is
|       triggered when handling Diffie-Hellman key exchanges defined with
|       the DHE_EXPORT cipher. This may allow a man-in-the-middle attacker
|       to downgrade the security of a TLS session to 512-bit export-grade
|       cryptography, which is significantly weaker, allowing the attacker
|       to more easily break the encryption and monitor or tamper with
|       the encrypted stream.
|     Disclosure date: 2015-5-19
|     Check results:
|       EXPORT-GRADE DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: mod_ssl 2.0.x/512-bit MODP group with safe prime modulus
|             Modulus Length: 512
|             Generator Length: 8
|             Public Key Length: 512
|     References:
|       https://www.securityfocus.com/bid/74733
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4000
|       https://weakdh.org
|   
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_DES_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: mod_ssl 2.0.x/1024-bit MODP group with safe prime modulus
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  BID:70574  CVE:CVE-2014-3566
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://www.securityfocus.com/bid/70574
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
| ssl-ccs-injection: 
|   VULNERABLE:
|   SSL/TLS MITM vulnerability (CCS Injection)
|     State: VULNERABLE
|     Risk factor: High
|       OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h
|       does not properly restrict processing of ChangeCipherSpec messages,
|       which allows man-in-the-middle attackers to trigger use of a zero
|       length master key in certain OpenSSL-to-OpenSSL communications, and
|       consequently hijack sessions or obtain sensitive information, via
|       a crafted TLS handshake, aka the "CCS Injection" vulnerability.
|           
|     References:
|       http://www.cvedetails.com/cve/2014-0224
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224
|_      http://www.openssl.org/news/secadv_20140605.txt
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
1024/tcp open  status      1 (RPC #100024)
MAC Address: 08:00:27:42:E5:2F (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Host script results:
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: ERROR: Server returned less data than it was supposed to (one or more fields are missing); aborting [14]
| smb-vuln-cve2009-3103: 
|   VULNERABLE:
|   SMBv2 exploit (CVE-2009-3103, Microsoft Security Advisory 975497)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2009-3103
|           Array index error in the SMBv2 protocol implementation in srv2.sys in Microsoft Windows Vista Gold, SP1, and SP2,
|           Windows Server 2008 Gold and SP2, and Windows 7 RC allows remote attackers to execute arbitrary code or cause a
|           denial of service (system crash) via an & (ampersand) character in a Process ID High header field in a NEGOTIATE
|           PROTOCOL REQUEST packet, which triggers an attempted dereference of an out-of-bounds memory location,
|           aka "SMBv2 Negotiation Vulnerability."
|           
|     Disclosure date: 2009-09-08
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3103
|_      http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3103
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: ERROR: Server returned less data than it was supposed to (one or more fields are missing); aborting [14]

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 358.10 seconds
```