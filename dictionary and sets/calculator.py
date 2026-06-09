# student_grade_calculator.py

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def is_pass(avg):
    return avg >= 60

def save_to_file(students):
    with open('results.txt', 'w') as f:
        for s in students:
            f.write(f"{s['name']}, Avg: {s['average']:.2f}, Grade: {s['grade']}, Status: {'PASS' if s['pass'] else 'FAIL'}\n")

students = []
num = int(input("How many students? "))
for _ in range(num):
    name = input("Student name: ")
    marks = list(map(float, input("Enter marks separated by space: ").split()))
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    passed = is_pass(avg)
    students.append({
        'name': name,
        'average': avg,
        'grade': grade,
        'pass': passed
    })
    print(f"--- {name} ---")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {'PASS' if passed else 'FAIL'}")

save_to_file(students)
print("Results saved to results.txt")

