a = float(input())

h = (12 * a) / 360
m = (h - int(h)) * 60
s = (m - int(m)) * 60

print(int(h), int(m), int(s))
