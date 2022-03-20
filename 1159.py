num = int(input())

#성의 첫 글자가 5개 이상이면 출력
#다섯명을 선발할 수 없을 경우에는 PREDAJA 출력
count_list = [0]*26
result = ""
for i in range(num):
    count_list[ord(input()[0])-97] += 1

for i in range(26):
    if count_list[i] >= 5:
        result += chr(i+97)

print(result if result else "PREDAJA")