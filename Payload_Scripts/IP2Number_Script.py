'''
Converts IP address into Whole number format.
'''

import socket, struct

# provide IP Address of Malicious Site
ip1 = raw_input("Enter the IP Address: ")

# Convert string format (X.X.X.X) to the 32-bit packed binary format
packedIP = socket.inet_aton(ip1) 

# Unpack the string containing packed data to the the number format
ip2num = struct.unpack("!L", packedIP)[0] 
ip2num1 = str(ip2num)

print "\nIP2Number: "+ip1+" : "+ip2num1
print "\nCheck in Browser: http://"+ip2num1+"\n\t\t  https://"+ip2num1+"\n"