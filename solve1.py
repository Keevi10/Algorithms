test = int(input())  

for _ in range(test):
    n=input()
    entrada = input().split() 
    #nums = list(map(int, entrada.split()))

    x=0
    for i in entrada:
        x+=(int(i))
        
    if x % 2 == 0:
        print("YES")
    else:
        print("NO")
        
