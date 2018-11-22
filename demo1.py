import re

st = input("Enter string:")
res = re.match(r"method",st)
if res == None:
    print("match not found")
else:
    print("match found")