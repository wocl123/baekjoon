num = int(input())

num_list = list(map(int, input().split()))
                
M = max(num_list)
aver = 0

for i in range(0, num):
    aver += (num_list[i]/M)*100

print(aver/num)
