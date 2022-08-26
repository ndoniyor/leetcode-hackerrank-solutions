a = [1,1]
seen = list()
for i in range(1,len(a)):
    test = i
    if a[i] not in (a[i+1:]) and a[i] not in seen:
        print(a[i])
    else:
        seen.append(a[i])