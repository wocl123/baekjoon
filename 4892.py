i=1
while(True):
    num = int(input())
    
    if num == 0:
        break
    
    n_one = num * 3
    
    if n_one %2 == 0: #n1 이 짝수면?
        n_two = n_one//2
        name = "even"
    else:
        n_two = (n_one+1)//2
        name = "odd"
        
    n_three = n_two * 3
    n_four = n_three // 9
    
    # print(n_one, n_two, n_three, n_four)
    if n_four % 2 == 0:
        print("{}. {} {}".format(i, name, n_four))
    else:
        print("{}. {} {}".format(i, name, n_four))
    i += 1