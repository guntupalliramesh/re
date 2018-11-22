import re

st = input("Enter string:")
res = re.search(r"method",st)
if res == None:
    print("search not found")
else:
    print("search found")
    print(res.group())
    print(res.start())
    print(res.end())