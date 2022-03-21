num = int(input())

time_num = list(map(int, input().split()))
y_sum = m_sum = 0

for i in range(num):
    y_sum += (time_num[i]//30+1)*10
    m_sum += (time_num[i]//60+1)*15
    print(y_sum, m_sum)
if y_sum > m_sum:
    print("M {}".format(m_sum))
elif y_sum < m_sum:
    print("Y {}".format(y_sum))
else:
    print("Y M {}".format(y_sum))
"""
영식요금제
30미만 : 10원 청구
30~60 : 20원 청구

민식 요금제
60미만 : 15원 청구
60~120 : 30원 청구
"""