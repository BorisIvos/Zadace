import re
string=input("unesite string: ")
regex="(^b)[0-5](i$)$"
match=re.findall(regex,string)

if match:
    print("podudaranje")

else:
    print("nema podudaranja")
