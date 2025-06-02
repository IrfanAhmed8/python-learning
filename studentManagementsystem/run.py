from student import student
from task import task

print("1.Add New Student ")
print('2.View All Students')
print('3.Enroll in Subject')
print('4. Add/Update Grades')
print('5.View Student Info')
print('6. Remove Student')
print('0. exit')

taskkey=int(input("enter the key for task"))

while(taskkey!=0):
    task(taskkey)
    taskkey=int(input("enter the key for task"))


