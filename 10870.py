def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
num = int(input())
print(fibonacci(num))