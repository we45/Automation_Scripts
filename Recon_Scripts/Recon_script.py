#!/usr/bin/env python
import re
import sys
import time
import glob, os
import subprocess


'''
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
'''


# Enter the Client Name / Project Name, the folder with the provided name will be created adjacent to this script. 
client_name = raw_input("Enter Client Name Without Space: ")

# Provide the file name with extension which consists of List of IP's which needs to scanned.
client_file_name = raw_input("Enter File Name Without Space: ")

filepath = os.path.join(client_file_name)


# This function is used to create the nmap comm959.ands and load it into a bash file. The results will be uploaded into Nmap_Results folder.
def func_sh_nmap_cmd(payload,f_name):
	filepath1 = os.path.join(os.getcwd(),'nmap_sh_cmd.sh')
	f1 = open(filepath1,'a')
	with open(filepath) as f:
		content123 = f.readlines()
		for lines in content123:
			strip_l = lines.rstrip()
			dir4 = "/Nmap_Results/"
			dir3 = os.path.join(client_name+dir4)
			if not os.path.exists(dir3):
				os.makedirs(dir3)
			data1 = payload+strip_l+" -Pn -oA "+dir3+f_name+strip_l
			f1.write(data1)
			f1.write("\n")
		f1.close()

# This function is used to create the nmap host command (To check host is up or not) and load it into a bash file. The results will be uploaded into Nmap_Results folder.
def func_nmap_host_cmd(payload):
	filepath1 = os.path.join(os.getcwd(),'nmap_sh_cmd.sh')
	f1 = open(filepath1,'a')
	dir4 = "/Nmap_Results/"
	dir3 = os.path.join(client_name+dir4)
	if not os.path.exists(dir3):
		os.makedirs(dir3)
	data1 = payload+" -oN "+dir3+"Host_up.txt"
	f1.write(data1)
	f1.write("\n")
	f1.close()
	

# This function is used to create the sslscan commands and load it into a bash file. The results will be uploaded into SSL_Scan_Results folder.
def func_sh_ssl_scan():
	filepath1 = os.path.join(os.getcwd(),'sh_ssl_scan.sh')
	f1 = open(filepath1,'w')
	with open(filepath) as f:
		content123 = f.readlines()
		for lines in content123:
			strip_l = lines.rstrip()
			dir7 = "/SSL_Scan_Results/"
			dir3 = os.path.join(client_name+dir7)
			if not os.path.exists(dir3):
				os.makedirs(dir3)
			dir4 = dir3.replace(" ", "\ ")			
			data1 = "sslscan --xml="+dir4+"SSL_Scan_"+strip_l+".xml "+strip_l
			f1.write(data1)
			f1.write("\n")
		f1.close()	


# This function is used to create the Metasploit modules and load it into a .rc file. The MSF Console will read the modules from the .rc file and perform the TCP scans. The results will be uploaded into Metasploit_Results folder.

def func_metasploit_tcp_scan():
	dir4 = "/Metasploit_Results/"
	dir3 = os.path.join(client_name+dir4)
	if not os.path.exists(dir3):
		os.makedirs(dir3)
	filepath = os.path.join(client_file_name)
	# In MSF Console, Spool is a command which is used to write the output to a file
	spool_tool = "spool tmp_scan_results.txt"
	module = "use auxiliary/scanner/portscan/tcp"
	rhosts = "set RHOSTS "
	rport = "set RPORTS 1-65535"
	exploit = "run"
	filepath1 = 'metasploit_tcp.rc'
	f1 = open(filepath1,'w')
	f1.write(spool_tool+"\n")
	f1.write(module+"\n")
	f1.write(rport+"\n")

	with open(filepath) as ipfile:
		content123 = ipfile.readlines()
		for lines in content123:
			strip_l = lines.rstrip()
			rhosts1 = rhosts+" "+strip_l
			f1.write(rhosts1+"\n")
			f1.write(exploit+"\n")
			f1.write("\n")

	# "spool off" command will stop writing the results to the file
	f1.write("spool off\n")
	f1.write("exit")
	f1.close()
	ipfile.close()
	msf_command = "sudo msfconsole -r "+filepath1
	os.system(msf_command)

	# Beautifying the file by removing the ansible codes
	filepath2 = "tmp_scan_results.txt"
	# filepath3 = "Metasploit_scan_results.txt"
	filepath3 = os.getcwd()+"/"+dir3+"Metasploit_scan_results.txt"	
	f2 = open(filepath3,'w')
	ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
	with open(filepath2) as o_file:
		content123 = o_file.readlines()
		l = []
		for i,lines in enumerate(content123):
			strip_l = lines.rstrip()
			kv = ansi_escape.sub('', strip_l)
			data = '-'*30+'\n'
			l.append(data)
			if "TCP OPEN" in kv:
				kv = kv.replace("[*] ", "")
				l[i] = kv
				f2.write(kv+"\n")
			else:
				if l[i-1] != data:
					f2.write(data)
	f2.close()

	# Once the scans are performed the below code will remove ".rc" & "tmp" file
	command1 = ['rm', '-r', filepath1]
	subprocess.Popen(command1)
	command2 = ['sudo', 'rm', '-r', 'tmp_scan_results.txt']
	subprocess.Popen(command2)
	time.sleep(2)



# This code describes about the swith case/user selection. The code snippet allows the user to select what type of tool can be used for scanning such as Nmap, SSL Scan and Metasploit Framework.

choice1 = 0

while int(choice1) not in range(1,5):
	choice1 = raw_input('''
	1. Nmap
	2. SSL Scan
	3. Metasploit TCP Scan
	4. Exit
	Enter your choice: ''')

choice1 = int(choice1)

if choice1 == 1:
	continue_string = True
	def func_nmap_scan():
		choice2 = 0
		while  int(choice2) not in range(1,8):
			choice2 = raw_input('''
			1. Discovery Scan
			2. Vulnerability Scan
			3. TCP Scan
			4. UDP Scan
			5. Poodle Scan
			6. Check Host is up
			7. Exit from Nmap Scan
			Enter your choice: ''')

		choice2 = int(choice2)

		# This condition is used to create nmap discovery script and send it to nmap function.
		if choice2 == 1:
			payload = "nmap -sV -sC --script=discovery -p 1-65535 "
			f_name = "Discovery_"
			func_sh_nmap_cmd(payload,f_name)
			print "Discovery Script is loaded into Automation Script"

		# This condition is used to create nmap vuln script and send it to nmap function.
		elif choice2 == 2:
			payload = "nmap -sV -sC --script=vuln -p 1-65535 "
			f_name = "Vulnerability_"
			func_sh_nmap_cmd(payload,f_name)
			print "Vulnerability Script is loaded into Automation Script"			

		# This condition is used to create nmap TCP Scan and send it to nmap function.
		elif choice2 == 3:
			payload = "nmap -sT -p 1-65535 "
			f_name = "TCP_"
			func_sh_nmap_cmd(payload,f_name)
			print "TCP Script is loaded into Automation Script"

		# This condition is used to create nmap UDP Scan and send it to nmap function.
		elif choice2 == 4:
			payload = "sudo nmap -sU "
			f_name = "UDP_"
			func_sh_nmap_cmd(payload,f_name)
			print "UDP Script is loaded into Automation Script"

		# This condition is used to create nmap poodle scan and send it to nmap function.
		elif choice2 == 5:
			payload = "nmap --script ssl-poodle -p 443 "
			f_name = "Poodle_"
			func_sh_nmap_cmd(payload,f_name)
			print "Poodle Script is loaded into Automation Script"

		# This condition is used to create nmap script which checks whether the host is up or not and send it to nmap function.
		elif choice2 == 6:
			payload = "nmap -sP -iL "+client_file_name+" -Pn"
			f_name = "Host_Up_"
			func_nmap_host_cmd(payload)
			print "Host Up Script is loaded into Automation Script"

		elif choice1 == 7:
			continue_string = False
			# sys.exit()

	func_nmap_scan()

	# Below code will prompt the user to add other Nmap scripts from the switch case.
	while continue_string:
		new_data = raw_input("Would you like to run other Nmap Scripts (y/n)...??")
		if new_data == "y" or new_data == "Y":
			func_nmap_scan()
		elif new_data == "n" or new_data == "N":
			continue_string = False
		else:
			break

elif choice1 == 2:
	func_sh_ssl_scan()

elif choice1 == 3:
	func_metasploit_tcp_scan()
	# pass

elif choice1 == 4:
	sys.exit()

dir5 = os.getcwd()+'/nmap_sh_cmd.sh'
dir6 = os.getcwd()+'/sh_ssl_scan.sh'
dir8 = "/Nmap_Results/"
dir3 = os.getcwd()+"/"+(os.path.join(client_name+dir8+"Host_up.txt"))
dir9 = os.getcwd()+"/"+(os.path.join(client_name+dir8+"Host_is_not_up.txt"))


# Below Code will trigger bash script which consists of nmap commands. The scan will triggered one after the other.
if os.path.exists(dir5):
	command = ['chmod', '+x', 'nmap_sh_cmd.sh']
	subprocess.Popen(command)
	time.sleep(1)
	os.system('./nmap_sh_cmd.sh')
	time.sleep(2)
	os.system('rm -r nmap_sh_cmd.sh')
elif not os.path.exists(dir5):
	print "Nmap Automation Script not found"


# Below Code will trigger bash script which consists of sslscan commands. The scan will triggered one after the other.
if os.path.exists(dir6):	
	command = ['chmod', '+x', 'sh_ssl_scan.sh']
	subprocess.Popen(command)	
	time.sleep(1)
	os.system('./sh_ssl_scan.sh')
	time.sleep(2)
	os.system('rm -r sh_ssl_scan.sh')
elif not os.path.exists(dir6):
	print "SSL Scan Automation Script not found"

# Below Code will filter the host which are up and running. The Host/Ip's which are down, will be saved it into another file.
if os.path.exists(dir3):
	filepath2 = dir9
	f3 = open(filepath2,'w')
	with open(dir3, 'r') as f2:
		content123 = f2.readlines()
		for lines in content123:
			strip_l = lines.rstrip()
			if "Failed to resolve" in strip_l:
				f3.write(strip_l)
				f3.write("\n")
			f3.close
else:
	pass


# Beautify the XML file of Nmap results and save it to HTML file.

xml_dir = os.getcwd()+"/"+(os.path.join(client_name+dir8))
for root, dirs, files in os.walk(xml_dir):
	xml_file_path = os.path.join(root)
	os.chdir(xml_file_path)
	for i in range(len(files)):
		if ".xml" in files[i]:
			a_file = files[i].split('.xml')
			xslt_path = "xsltproc "+files[i]+" -o "+a_file[0]+".html"
			os.system(xslt_path)
		else:
			pass
