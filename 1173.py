"""
N : 운동을 하는 시간(분)
m : 초기 맥박
M : 맥박이 여길 넘어가면 안됨
T : 운동을 할 시 늘어나는 맥박
R : 휴식을 할 때 감소하는 맥박
 -> 영식이의 맥박이 X였다면, 1분동안 운동한 후 맥박은 X+T = m + T
 -> 만약 1분동안 휴식한다면 맥박은 X-R = m - R
"""
N, m, M, T, R = map(int, input().split())

cnt = time = 0
sum = m
if m + T > M:
    print(-1)
else:
    while(True):
        if sum + T <= M:
            sum += T
            cnt += 1
            time += 1
            print(sum, "sum+T<=M")
        else:
            sum = max(sum-R, m)
            print(sum-R, m, sum, max(sum-R, m), "else")
            time += 1
        
        if cnt == N:
            break
    print(time)
    