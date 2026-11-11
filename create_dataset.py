import csv

# Fictional student records for Assignment Two.
students = [
    ["STU001", "Computer Science", 200, 92, 88],
    ["STU002", "Accounting", 100, 85, 76],
    ["STU003", "Mass Communication", 300, 78, 81],
    ["STU004", "Computer Science", 100, 95, 91],
    ["STU005", "Business Administration", 200, 88, 79],
    ["STU006", "Cyber Security", 300, 90, 86],
    ["STU007", "Accounting", 400, 72, 68],
    ["STU008", "Computer Science", 200, 81, 84],
    ["STU009", "Economics", 100, 76, 73],
    ["STU010", "Mass Communication", 200, 89, 90],
    ["STU011", "Cyber Security", 100, 93, 87],
    ["STU012", "Business Administration", 300, 80, 75],
    ["STU013", "Computer Science", 400, 97, 94],
    ["STU014", "Economics", 200, 74, 70],
    ["STU015", "Accounting", 300, 86, 82],
    ["STU016", "Computer Science", 300, 68, 72],
    ["STU017", "Mass Communication", 400, 91, 89],
    ["STU018", "Cyber Security", 200, 84, 80],
    ["STU019", "Business Administration", 100, 79, 77],
    ["STU020", "Economics", 400, 87, 85],
]

columns = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(students)

print(f"Created student_dataset.csv with {len(students)} fictional student records.")
