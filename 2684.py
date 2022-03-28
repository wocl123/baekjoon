test_case = int(input())
check_list = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]

for i in range(test_case):
    count_list = [0]*8
    moonja = list(map(str, input()))
    for j in range(len(moonja)-2):
        sum = moonja[j]+moonja[j+1]+moonja[j+2]
        for k in range(8):
            if sum == check_list[k]:
                count_list[k] += 1
    for j in count_list:
        print(j, end=' ')
    print()
        
"""
TTT : count_list[0]
TTH : count_list[1]
THT : count_list[2]
THH : count_list[3]
HTT : count_list[4]
HTH : count_list[5]
HHT : count_list[6]
HHH : count_list[7]
"""