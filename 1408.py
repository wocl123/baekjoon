real_time = input().split(":")
start_time = input().split(":")
mi_time = []
print(real_time)
print(start_time)

for i in range(3):
    mi_time.append(int(start_time[i])-int(real_time[i]))
    
    
print(mi_time)