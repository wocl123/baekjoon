chess = [[False]*8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            chess[i][j] = True

user_input = [list(map(str, input())) for _ in range(8)]
count = 0
for i in range(8):
    for j in range(8):
        if (chess[i][j]==True) and (user_input[i][j]=='F'):
            count += 1
            
print(count)