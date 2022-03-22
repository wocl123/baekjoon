def is_prime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
num1, num2 = map(int, input().split())
for i in range(num1, num2+1):
    if is_prime(i):
        print(i)   