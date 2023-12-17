import re 
file = open('sampletext.txt')
text = file.read()
email_pat = r'[a-zA-Z0-9\.\+_]+@[a-zA-Z0-9\.\+]+.com'
mob_pat = r'[0-9]+[#\-*]*[0-9]+[0-9]+[#\-*]*[0-9]'
url_pat = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
name_pat = r'M(?:r\.|rs\.|s\.) [a-zA-Z]+'
number_pat = r'[0-9]+[#\-*]*[0-9]+[#\-*]*[0-9]+'

# 1. Atleast 2 char
# 2. Second character digit divisible by 3
# 3. First charachter is only a-k
# 4. Allowed charachters are a-zA-Z0-9#
pattern = r'[a-kA-K][0369][a-zA-Z0-9#]*'

# to find correct mobile number with 10 digits  starting from 7 or 8 or 9
pattern1 = r'[789][0-9]{9}'

# test this patternw ith user input 
inputString = input("Enter string to test : ")
if re.match(pattern,inputString):
    print("Matched")
else:
    print("Not matched")

# to find correct mobile number with 10 digits starting from 7 or 8 or 9
input2= input("Enter string to test : ")
if re.match(pattern1,input2):
    print("Matched")
else:
    print("Not matched")
    

print(f"\nEmails in text field are : {re.findall(email_pat,text)}")
print(f"Phone numbers are : {re.findall(mob_pat,text)}")
print(f"Names are : {re.findall(name_pat,text)}")
print(f"Urls are : {re.findall(url_pat,text)}\n")