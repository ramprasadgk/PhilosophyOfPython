a = [16, 19, 11, 15, 10, 12, 14]

#iterating over a
for i in a:
    key = a.index(i)
    while key > 0:
        if(a[key-1]> a[key]):
            a[key-1], a[key] = a[key], a[key-1]
        else:
            break
        key = key-1


print (a)