def max_product_with_increment(a):


    
    min_index = a.index(min(a))

    
    a[min_index] += 1

    
    max_product = 1
    for num in a:
        max_product *= num

    return max_product


def main():
    t = int(input())  
    results = []  
    for _ in range(t):
        print()
        n = int(input())  
        a = list(map(int, input().split()))
        while len(a) != n:
            print()
            a = list(map(int, input().split()))
        results.append(max_product_with_increment(a))

    
    print()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
