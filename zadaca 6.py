def unazad(s):
    if len(s)==0:
        return s
    else:
        return unazad(s[1:]) + s[0]

s="programer"

print(unazad(s))


