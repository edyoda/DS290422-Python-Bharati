def get_marks():
    total_value = 300
    eng = int(input("Enter English Marks : "))
    maths = int(input("Enter Maths Marks : "))
    science = int(input("Enter Science Marks : "))
    total_marks = eng + maths + science
    return total_value,total_marks

def get_marks_all_subjects():
    total_value = 600
    eng = int(input("Enter English Marks : "))
    maths = int(input("Enter Maths Marks : "))
    science = int(input("Enter Science Marks : "))
    history = int(input("Enter History Marks : "))
    geo = int(input("Enter Geo Marks : "))
    pt = int(input("Enter PT Marks : "))
    total_marks = eng + maths + science + history + geo + pt
    return total_value,total_marks

def calculate_percentage(total_value,total_marks):
    per = (total_marks/total_value)*100
    return per
    
def calculate_grade(per):
    if per >= 90:
        grade = "A"
    elif per >= 70 and per < 90:
        grade = "B"
    elif per >= 60 and per < 70:
        grade = "C"
    else:
        grade = "F"
    return grade

# total,student_marks = get_marks()
# percent = calculate_percentage(total,student_marks)
# grade = calculate_grade(percent)

# print("Congratz you got ",grade,"grade")

total,student_marks = get_marks_all_subjects()
percent = calculate_percentage(total,student_marks)
grade = calculate_grade(percent)

print("Congratz you got ",grade,"grade")