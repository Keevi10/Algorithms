test = int(input())  
results = []  


for h in range(test):
    size = int(input())  
    values = input()

   
    solves = list(values)

    
    i = 0
    while i < len(solves):  
        current = solves[i]  
        j = i + 1  
        while j < len(solves):
            if solves[j] == current:  
                solves.pop(j) 
            else:
                j += 1
        i += 1

    
    result = size + len(solves)
    results.append(result)  


for res in results:
    print(res)
