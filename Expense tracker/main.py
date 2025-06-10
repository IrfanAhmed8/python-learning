from tracker import Task

print("welcome to the expense tracker app")
print("what do you like to do?\n 1.)add expense\n 2.)view tracker \n3.)delete the expense")

task=int(input("enter the key for the task"))
while(task!=0):
    Task(task)
    task=int(input("enter the key for the task"))