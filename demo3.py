import re

st = input("Enter string:")
res = re.findall(r"method",st)
print(res)