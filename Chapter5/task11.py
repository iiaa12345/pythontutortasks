a = input()

print(a[:a.find("h") + 1] + a[a.find("h") + 1: a.rfind("h")].replace("h", "H") + a[a.rfind("h"):])
