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
                


    elif(key==0):
        return
