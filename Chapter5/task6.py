a = input()

if a.count("f") == 0:
    print(-2)
elif a.count("f") == 1:
    print(-1)
else:
    print(a.find("f", a.find("f") + 1))
