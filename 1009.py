num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    a_value = a%10
    
    if a_value == 0:
        print(10)
    elif a_value in [1,5,6]: #1,5,6일때는 본인의 값이 나옴
        print(a_value)
    #4 => 4^1=4, 4^2=16, 4^3=64, 4^4=256 => 지수가 홀수일때 4, 짝수일때 6
    #9 => 9^1=9, 9^2=81, 9^3=729 9^4=6561 => 지수가 홀수일때 9, 짝수일때 1
    elif a_value in [4, 9]:  #4, 9는 패턴이 2개씩 존재
        b_value = b%2        
        if b_value == 0:     #지수가 짝수일때
            #첫 번째 수를 제곱하고 10으로 나눈 값이 마지막 데이터처리 컴퓨터
            print((a_value*a_value)%10) 
        else:                #지수가 홀수일 때
            #첫 번째 수가 마지막 데이터 처리 컴퓨터가 됨.
            print(a_value)
    else:                    #그 외 2, 3, 7, 8
    #2 => 2^1=2, 2^2=4, 2^3=8, 2^4=16 =>2,4,8,6 반복
    #3 => 3^1=3, 3^2=9, 3^3=27, 3^4=81 =>3,9,7,1 반복
    #7 => 7^1=7, 7^2=49, 7^3=343, 7^4=2401 => 7,9,3,1 반복
    #8 => 8^1=8, 8^2=64, 8^3=512, 8^4=4096 => 8,4,2,6 반복
        b_value = b%4        #빠른 조건 검색을 위해 두번째 인자를 4로 나눈값을 구한다.
        if b_value == 0:     #지수가 4의 배수일 때 4번째 값이 반복될것이므로
            print(a_value**4%10) #첫번째 인자에 4 제곱한 값을 10으로 나눈값이랑 같다.
        else:                #지수가 4의 배수가 아니라면
            print(a_value**b_value%10) #a^b를 10으로 나눈다.
    
    
    
""" 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10 [총 10대의 컴퓨터를 가지고 있음.]

if a == 0 => (a ** b) % 10 => 10
if a == 1 => (a ** b) % 10 => 1  
if a == 2 => (a ** b) % 10 => 2, 4, 8, 6 
if a == 3 => (a ** b) % 10 => 3, 9, 7, 1
if a == 4 => (a ** b) % 10 => 4, 6
if a == 5 => (a ** b) % 10 => 5
if a == 6 => (a ** b) % 10 => 6
if a == 7 => (a ** b) % 10 => 7, 9, 3, 1
if a == 8 => (a ** b) % 10 => 8, 4, 2, 6
if a == 9 => (a ** b) % 10 => 9, 1

"""