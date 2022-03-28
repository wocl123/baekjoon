from sys import stdin

count_alpha = [0]*26

user_input = stdin.read().replace('\n', '').replace(' ', '')

for i in user_input:
    count_alpha[ord(i)-97] += 1
    
max_number = max(count_alpha)
print(user_input)
print(count_alpha)
for i in range(26):
    if count_alpha[i] == max_number:
        print(chr(i+97), end = '')