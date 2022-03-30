n, m = map(int, input().split())
baguni_list = []
for i in range(n):
    baguni_list.append(i+1)
    
for i in range(m):
    a,b = map(int, input().split())
    temp = baguni_list[a-1]
    baguni_list[a-1] = baguni_list[b-1]
    baguni_list[b-1] = temp

for i in baguni_list:
    print(i, end=' ')
    
# baguni_list[1] <=> baguni_list[2]
# temp = baguni_list[a]
# baguni_list[a] = baguni_list[b]