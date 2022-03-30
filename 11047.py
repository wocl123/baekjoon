test_case, money = map(int, input().split())
coin_list = []
count = 0
for i in range(test_case):
    coin_list.append(int(input()))
    
coin_list.reverse()
for i in coin_list:
    print("현재 남은 돈 : ", money)
    if money >= i:
        count += money // i
        money = money % i
        if money <= 0:
            break
print(count)