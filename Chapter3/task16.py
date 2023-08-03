p = int(input())
rub = int(input())
cop = int(input())

cop += rub * 100
cop += cop * p / 100

print(cop // 100, int(cop % 100))
