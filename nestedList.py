if __name__ == '__main__':
    #student list with name and score
    students = []
    #taking input 
    for _ in range(int(input())): 
        name = input()
        score = float(input())
        students.append([name,score])
    # extracting only the scores 
    newScore = [student[1] for student in students]
    # soring score
    uniqueScore = sorted(set(newScore))
    #finding the second lowest
    secondLowest = uniqueScore[1]
    # extracting the names 
    names = [student[0] for student in students if student[1]==secondLowest]
    # printing the name alphabetically
    for name in sorted(names):
        print(name)
    