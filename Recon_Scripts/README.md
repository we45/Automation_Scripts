# Recon_Scripts

Automation is a critical element of a robust and scalable application security program. Penetration Testers are now not just required to run tools, but also find intuitive ways to automated running of these tools, saving them critical effort and bandwidth - custom scripts being one such approach. Custom Scripting not only goes into the depth and scope of your application testing coverage but also enables you to perform rigid testing within the designated time frame of your test cycles.

__Requirements__

Python 2.7.X


__Install Instructions__

```
To install Nmap
sudo apt-get update
sudo apt-get install nmap

Install SSL Scan
sudo apt-get update
sudo apt-get install sslscan

To get Nmap xml results in tabular format in browser.
sudo apt-get install xsltproc

Install Metasploit
Download Metasploit Framework (https://www.metasploit.com/download)
sudo chmod +x metasploit-latest-linux-installer.run
sudo ./metasploit-latest-linux-installer.run
```

__Script Description__

Nmap, Metasploit and SSL Scan tools are essential in any good application security penetration testing and are usually run manually, one-by-one. In addition, you need to specify commands and rules to trigger the tools to perform their respective tasks. With this script, you can run scans without giving commands for all the three tools. You only need to provide the target hosts list when the script prompts you before triggering the scans.


__Nmap (Network Mapping):__
Nmap is customized to include Discovery Scan (identify new directories), Vulnerability Scan, TCP Scan, UDP Scan, Poodle Scan, and checks if the host is up or not.


__Metasploit Tool:__
This script only includes TCP port scans module of Metasploit, to perform port scans on the target host. While Nmap also does TCP port scans, the purpose of using Metasploit is to cross check its results against Nmap results.


__SSL Scan:__
This tool is used to check for weak ciphers within the SSL protocol. The results clarify the strength of ciphers used for transferring information within SSL connection, whether they have a strong or weak cipher suite or hashing algorithm.

__Result Format:__
Since the tools yield results that aren’t always reader friendly, this script also converts the results into a tabular format, presenting results in a structured view. For example, results obtained from the Nmap are parsed, beautified, and presented in an HTML format. The TCP Scan results from Metasploit are parsed and stored in a text format. SSL Scan results are saved to an XML format.
