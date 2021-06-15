import re
string=input("Unesite e-mail: ")

regex="[a-z].[a-z][@][f][p][m][o][z].[s][u][m].[b][a]$"
match=re.findall(regex,string)
if match:
    print("Uspješno ste unijeli vašu e-mail adresu")
else:
    print("e-mail nije validan")
string2=input("unesite eduld: ")
regex2="[a-z][@][s][u][m].[b][a]$"
match2=re.findall(regex2,string2)
if match2:
    print("Uspješno ste unijeli vaš edul")
else:print("Vaš edul nije validan")
