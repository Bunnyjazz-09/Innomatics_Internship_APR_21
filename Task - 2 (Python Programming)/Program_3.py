if __name__ == '__main__':
    python_students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
    grade=[]
    student=[]
    for x in python_students:
        ele=x[1]
        grade.append(ele)
    grade=sorted(list(set(grade)))
    second_lowest=grade[1]
    for x in python_students:
         if second_lowest==x[1]:
            ele=x[0]
            student.append(ele)
    student=sorted(student)
    for x in student:
        print(x)