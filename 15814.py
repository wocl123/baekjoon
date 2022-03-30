sentense = list(map(str, input()))
test_case = int(input())

for i in range(test_case):
    a,b = map(int, input().split())
    temp_a = sentense[b]
    sentense[b] = sentense[a]
    sentense[a] = temp_a
    
print("".join(sentense))