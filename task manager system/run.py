from task import tasks

print("welcome to the task manager")
print("1. Add Task")
print("2. View All Tasks")
print("3. Mark Task as Completed")
print("4. Filter Pending Tasks")
print("5. Exit")


key=int(input("enter the key"))

while(key):
    tasks(key)
    key=int(input("enter the key"))
