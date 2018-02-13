import os
import sys

# Create the Wordlist file adjacent to the script
filepath=('wordlist.txt') 

f=open(filepath, 'w')

# "xselections" function generates the payload with permutation technique
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss


# Ascii Values
# Numbers = 48 - 57
# Capital = 65 - 90
# Lower = 97 - 122

choice = 0
while int(choice) not in range(1,9):
    choice = raw_input('''
    1) Numbers
    2) Uppercase Letters
    3) Lowercase Letters
    4) Numbers & Uppercase Letters
    5) Numbers & Lowercase Letters
    6) Numbers & Uppercase Letters + Lowercase Letters
    7) Uppercase Letters & Lowercase Letters
    8) Exit
    Enter the Choice: ''') 

# Condition provided to create the payloads selected by the user.
choice = int(choice)
poss = []
if choice == 1:
    num1=raw_input("Enter the Min Range Number: ")
    num2=raw_input("Enter the Max Range Number: ")
    numb = (range(ord(num1), ord(num2)+1))    
    poss += numb    
elif choice == 2:
    cap1=raw_input("Enter the Min Range Character (Only Uppercase Letters): ")
    cap2=raw_input("Enter the Max Range Character (Only Uppercase Letters): ")
    cap = (range(ord(cap1), ord(cap2)+1))
    poss += cap
elif choice == 3:
    low1=raw_input("Enter the Min Range Character (Only Lowercase Letters): ")
    low2=raw_input("Enter the Max Range Character (Only Lowercase Letters): ")
    low = (range(ord(low1), ord(low2)+1))
    poss += low
elif choice == 4:
    num1=raw_input("Enter the Min Range Number: ")
    num2=raw_input("Enter the Max Range Number: ")
    numb = (range(ord(num1), ord(num2)+1))
    poss += numb
    cap1=raw_input("Enter the Min Range Character (Only Uppercase Letters): ")
    cap2=raw_input("Enter the Max Range Character (Only Uppercase Letters): ")
    cap = (range(ord(cap1), ord(cap2)+1))
    poss += cap
elif choice == 5:
    num1=raw_input("Enter the Min Range Number: ")
    num2=raw_input("Enter the Max Range Number: ")
    numb = (range(ord(num1), ord(num2)+1))
    poss += numb
    low1=raw_input("Enter the Min Range Character (Only Lowercase Letters): ")
    low2=raw_input("Enter the Max Range Character (Only Lowercase Letters): ")
    low = (range(ord(low1), ord(low2)+1))
    poss += low
elif choice == 6:
    num1=raw_input("Enter the Min Range Number: ")
    num2=raw_input("Enter the Max Range Number: ")
    numb = (range(ord(num1), ord(num2)+1))
    poss += numb
    cap1=raw_input("Enter the Min Range Character (Only Uppercase Letters): ")
    cap2=raw_input("Enter the Max Range Character (Only Uppercase Letters): ")
    cap = (range(ord(cap1), ord(cap2)+1))
    poss += cap
    low1=raw_input("Enter the Min Range Character (Only Lowercase Letters): ")
    low2=raw_input("Enter the Max Range Character (Only Lowercase Letters): ")
    low = (range(ord(low1), ord(low2)+1))
    poss += low
elif choice == 7:
    cap1=raw_input("Enter the Min Range Character (Only Uppercase Letters): ")
    cap2=raw_input("Enter the Max Range Character (Only Uppercase Letters): ")
    cap = (range(ord(cap1), ord(cap2)+1))
    poss += cap
    low1=raw_input("Enter the Min Range Character (Only Lowercase Letters): ")
    low2=raw_input("Enter the Max Range Character (Only Lowercase Letters): ")
    low = (range(ord(low1), ord(low2)+1))
    poss += low
elif choice == 8:
    raise SystemExit

bigList = []
for i in poss:
    bigList.append(str(chr(i)))

# Provide the length of the payload
MIN = raw_input("Enter the Minimum Length: ")
MIN = int(MIN)
MAX = raw_input("Enter the Maximum Length: ")
MAX = int(MAX)
for i in range(MIN,MAX+1):
    for s in xselections(bigList,i): f.write(''.join(s) + '\n')