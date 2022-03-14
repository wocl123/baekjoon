while(True):
    ch = list(map(str, input()))
    count = 0
    if ch[0]=="#":
        break
    
    length = len(ch)
    for i in range(0, length):
        if (ch[i].lower() == "a") or (ch[i].lower() == "e") or (ch[i].lower() == "i") or (ch[i].lower() == "o") or (ch[i].lower() == "u"):
            count += 1
    
    print(count)