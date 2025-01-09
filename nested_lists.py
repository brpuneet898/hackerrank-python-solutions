# # Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        l = []
        name = input()
        score = float(input())
        l.append(name)
        l.append(score)
        records.append(l)
    
    scores = []
    for i in range(len(records)):
        scores.append(records[i][1])
    
    m = min(scores)
    scores.sort()
    sm = 0.0
    for i in range(len(scores)):
        if scores[i]!=m:
            sm = scores[i]
            break
    
    finallist = []
    for i in range(len(records)):
        if records[i][1] == sm:
            finallist.append(records[i][0])
    
    finallist.sort()
    for i in finallist:
        print(i)