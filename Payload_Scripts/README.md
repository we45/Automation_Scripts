# Payload_Scripts
Automation payload scripts that can help your penetration testing process. These tools/scripts have been developed to enhance application and infrastructure security testing.


__Requirements__

Python 2.7.X


__Install Instructions__

`pip install -r requirements.txt`

__Script Description__


__1. IP2Number Script:__
This script converts an IP Address to a generic Number format. It is useful while performing or inspecting  URL redirection /server side request forgery attacks.


__2. MSF Payload:__
This MSF script will generate payloads necessary to inject into an exploit that can be used to compromise the windows systems. The script creates the payload with minimal inputs, and sets up the listener automatically to fetch the meterpreter shell access of a victim's system.


__3. Permutation Password:__
This script generates a password dictionary using strings supplied by the user that were scraped from the application, thereby narrowing down the dictionary specific to this application.


__4. Wordlist:__
This script is a custom wordlist generator that helps with brute force attacks against the different parameters of an application. It generates the necessary payload using permutation techniques with the following combinations: Numbers, Uppercase Letters, Lowercase Letters, Numbers & Uppercase Letters, Numbers & Lowercase Letters, Numbers & Uppercase Letters + Lowercase Letters, and Uppercase Letters & Lowercase Letters.
