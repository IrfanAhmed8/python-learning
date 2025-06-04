from student import student

student_list=[]

def task(key):
    if(key==1):
        print('enter the data of the student')
        username=input('enter the name of the student')
        studentid=int(input('enter the id no'))
        subjects=input("enter the subject add comma after each subject").split(',')
        grades={}
        for subject in subjects:
            grade=input(f"Enter grade for {subject.strip()}:")
            grades[subject.strip()]=grade


        student1=student(username,studentid,subjects,grades)
        student_list.append(student1)
        print(f"\nStudent '{username}' added successfully!\n")

    elif(key==2):
        for stuentlist in student_list:
            print(stuentlist)

    elif(key==3):
        addsubject=int(input('enter the studentid'))
        for students in student_list:
            if(students.id==addsubject):
                subjects=input("enter the subject add comma after each subject").split(',')
                students.subjects.extend([s.strip() for s in subjects])
                break
            else:
                print('id not found')
    elif(key == 4):
        print("Press 'u' for update or 'a' to add grades")
        decision = input('Enter the choice: ')

        if decision == 'u':
            update_id = int(input('Enter student ID: '))
            found = False  # Track if student is found
            for students in student_list:
                if students.id == update_id:
                    subject = input("Enter the subject: ")
                    if subject in students.grades:
                        new_grade = input("Enter the new grade: ")
                        students.grades[subject] = new_grade
                        print(f"Grade updated for {subject}")
                    else:
                        print("Subject not found in student's grades.")
                    found = True
                    break
            if not found:
                print("Student ID not found.")

        elif decision == 'a':
            add_id = int(input("Enter student ID: "))
            found = False  # Track if student is found
            for students in student_list:
                if students.id == add_id:
                    subject = input("Enter the new subject: ")
                    grade = input("Enter the grade: ")
                    students.subjects.append(subject)  # Make sure this is `.subjects`, not `.subject`
                    students.grades[subject] = grade
                    print(f"Added subject '{subject}' with grade {grade}")
                    found = True
                    break
            if not found:
                print("Student ID not found.")



    elif(key==0):
        return
