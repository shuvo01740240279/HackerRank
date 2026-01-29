if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command = input().split()
        action = command[0]
        if action == "insert":
            list.insert(int(command[1]),int(command[2]))
        elif action == "print":
            print(list)
        elif action == "remove":
            list.remove(int(command[1]))
        elif action == "append":
            list.append(int(command[1]))
        elif action == "sort":
            list.sort()
        elif action == "pop":
            list.pop()
        elif action == "reverse":
            list.reverse()
            
            
