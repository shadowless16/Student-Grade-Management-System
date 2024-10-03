# Define Student Class
student_info = {}

# menu = int(input("Would You like to \n1. Add student \n2. Add grade \n3. Update grade \n4. View student grade \n5. calaculate avarage grade \n6. Exit Program \nSelect one of the following options: "))
    

def add_student():
    name = input("Enter Student's Name: ").capitalize()
    student_info[name] = {"grade": {"maths": 0, "english": 0, "science": 0}}
    print(f"Student {name} has been added")


def add_grade():
    name = input("Enter Student's Name: ").capitalize()

    if name not in student_info:
        print(f"Student {name} does not exist")
    else:
        student_info[name] = {"grade": {}}
    
        math_grade = int(input("Maths Grade: "))
        eng_grade = int(input("English Grade: "))
        sci_grade = int(input("Science Grade: "))

        student_info[name]["grade"]["maths"] = math_grade
        student_info[name]["grade"]["english"] = eng_grade
        student_info[name]["grade"]["science"] = sci_grade
    
    print(f"Grades for {name} updated: {student_info[name]['grade']}")
    # print(student_info)

def update_grade():

    name = input("Enter Student's Name: ").capitalize()

    if name not in student_info:
        print(f"Student {name} does not exist")
    else:
        # Update grades one by one
        student_info[name]["grade"]["maths"] = int(input("Enter the new Maths grade: "))
        student_info[name]["grade"]["english"] = int(input("Enter the new English grade: "))
        student_info[name]["grade"]["science"] = int(input("Enter the new Science grade: "))

        print(f"Updated grades for {name}: {student_info[name]['grade']}")


def view_student_grade():

    name = input("Enter Student's Name: ").capitalize()

    # Check if the student exists in the dictionary
    if name not in student_info:
        print(f"Student {name} does not exist.")
    else:
        print(f"Grades for {name}: {student_info[name]['grade']}")



def calculate_avarage_grade():

    name = input("Enter Student's Name: ").capitalize()

    if name not in student_info:
        print(f"Student {name} does not exist.")
    else:
        grades = student_info[name]['grade']
        
        total = sum(grades.values())
        
        num_subjects = len(grades)
        
        average = total / num_subjects
        
        print(f"Average grade for {name} is: {average:.2f}")



def exit_program():
    print("Exit program")

while True:

    menu = int(input("\nWould you like to: \n1. Add student \n2. Add grade \n3. Update grade \n4. View student grade \n5. Calculate average grade \n6. Display all students \n7. Exit Program\nSelect an option: "))


    match menu:
        case 1:
            add_student()
        case 2:
            add_grade()
        case 3:
            update_grade()
        case 4:
            view_student_grade()
        case 5:
            calculate_avarage_grade()
        case 6:
            exit_program()
            break
        case _:
            print("Enter one of the follow option above")


