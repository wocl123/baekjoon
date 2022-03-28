num = int(input())
lst = list(input())
length = len(lst)

for i in range(num-1):
    se_lst = list(input())
    for j in range(length):
        if lst[j] != se_lst[j]:
            lst[j] = '?'
            
print("".join(lst))