a,b = map(str, input().split())
a = int(a, 2)
b = int(b, 2)
sum = format(a+b, 'b')
print(sum)





"""
[접두어]
2진수 : 0b (binary number) / 함수 : bin
8진수 : 0o (octal number) / 함수 : oct
16진수 : 0x (hexadecimal number) / 함수 : hex

1. 내장함수를 이용한 출력
 ㅇ 2진수를 10진수로 변환
  : a = int(input(), 2)
    print(a)
    [입력] : 110
    [출력] : 6

 ㅇ 10진수를 2진수로 변환
  : a = int(input())
    b = bin(a)
    print(b)
    [입력] : 220
    [출력] : 0b11011100

 ㅇ 8진수를 10진수로 변환
  : a = int(input(), 8)
    print(a)
    [입력] : 123123
    [출력] : 42579

 ㅇ 16진수를 10진수로 변환 
  : a = int(input(), 16)
    print(a)   
    [입력] : a10
    [출력] : 2576
    
 ㅇ 10진수를 16진수로 변환
  : a = int(input())
    b = hex(a)
    print(a)
    [입력] : 220
    [출력] : 0xdc
    
 2. 출력 시 앞에 붙는 0x, 0b, 0c를 없애는 방법
  ㅇ format(인자값, '접두어)
   ex) 
   num = 100
   num_b = format(num, 'b') #2진수
   num_o = format(num, 'o') #8진수
   num_x = format(num, 'x') #16진수
"""