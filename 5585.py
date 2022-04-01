money = int(input())
money_list = [500, 100, 50, 10, 5, 1]

result_money = 1000-money
sum = 0

for i in money_list:
    print("현재 남은 돈 : ", result_money)
    if result_money >= i:
        sum += result_money // i
        result_money = result_money % i 
        if result_money <= 0:
            break
print(sum)