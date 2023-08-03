rub = int(input())
cop = int(input())
n = int(input())

cop += rub * 100

total_cop = cop * n

print(total_cop // 100, total_cop % 100)
