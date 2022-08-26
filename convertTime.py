s = "12:01:00PM"
length = len(s)

if(s[length-2:] == "AM"):
    if(s[0:2]!="12"):
        snew = s[0:length-2]
    else:
        snew = "00" + s[2:length-2]
else:
    newhour = s[0:2]
    if(s[0:2]!="12"):
        newhour = str(int(s[0:2])+12)
    snew = newhour+s[2:length-2]
return snew
