if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    newArray = list(set(arr))
    newArray.sort()
    print(newArray[-2])
    
    
    
    