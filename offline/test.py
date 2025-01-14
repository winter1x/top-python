students = [('alice', 20), ('alice', 20), ('alice', 20)]
grades = [[1, 2, 3], [1, 2, 3], [1, 2, 4]]

combined_data = list(zip(students, grades))
student_averages = []

for (name, age), student_grades in combined_data:
    average_grade = sum(student_grades) / len(student_grades)
    student_averages.append((name, age, student_grades, average_grade))
    print(f"'{name}', {age}, {student_grades}, {average_grade:.2f}")

all_grades = [grade for student_grades in grades for grade in student_grades]
overall_average = sum(all_grades) / len(all_grades)

best_student = max(student_averages, key=lambda x: x[3])

print(round(overall_average, 2))
print(best_student[0], best_student[1], best_student[2], round(best_student[3], 2))