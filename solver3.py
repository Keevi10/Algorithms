def main():
    n = int(input())  
    numStrings = input().split()  
    groups = [0, 0, 0, 0]  
    
    
    for numString in numStrings:
        groups[int(numString) - 1] += 1
    
    
    n = groups[3]
    
   
    if groups[2] > 0:
        n += groups[2]
        groups[0] -= groups[2]
    
    
    if groups[1] > 0:
        n += groups[1] // 2  
        if groups[1] % 2 != 0:  
            n += 1
            groups[0] -= 2  
    
    
    n += (groups[0] > 0) * (groups[0] // 4 + (1 if groups[0] % 4 != 0 else 0))
    
    
    print(n)


if __name__ == "__main__":
    main()
