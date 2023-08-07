a = input()

print(a[:a.find("h")] + a[a.rfind("h"): a.find("h"): -1] + a[a.rfind("h"):])
