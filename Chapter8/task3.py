def capitalize(a):
    a = a.split()
    b = []
    for i in range(len(a)):
        b.append(a[i].replace(a[i][0], chr(ord(a[i][0]) - 32), 1))
    return " ".join(b)


a = input()

print(capitalize(a))
