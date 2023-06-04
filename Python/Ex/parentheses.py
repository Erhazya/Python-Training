

s = "()"
verif = False

while("()" in s or "[]" in s or "{}" in s):

    if "()" in s : 
        s = s.replace("()","")
    if "[]" in s : 
        s = s.replace("[]","")
    if "{}" in s : 
        s = s.replace("{}","")




if s == "" : 
    verif = True

print(verif)