import re

st = input("Enter string:")
res = re.findall(r"\w+$",st)
print(res)
