expected_answer = int(input())
student_answer = int(input())

if student_answer == 1:
    if expected_answer != 1:
        print("NO")
    else:
        print("YES")
else:
    if expected_answer == 1:
        print("NO")
    else:
        print("YES")
