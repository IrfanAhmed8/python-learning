
from datetime import datetime
class Task:
    count=0
    

    def __init__(self,id,title,description,priority,due_date,status):
        self.id=id
        self.title=title
        self.description=description
        self.priority=priority
        self.due_date=self.validate_date(due_date)
        self._status=status
        Task.count+1
        #magic method
    def __str__(self):
       return f'|{self.id}|{self.title}|{self.description}|{self.priority}|{self.due_date}|{self.status}'
    #creating a getter for status

    @property
    def status(self):
        return self._status
    #setter for status

    @status.setter
    def status(self,status):
        if status not  in ['pending','completed']:
            raise ValueError("not Status must be either 'Pending' or 'Completed'")
        self._status=status
    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            raise ValueError("Date must be in format DD-MM-YYYY")

    
    @classmethod
    def total_task(cls):
        return cls.count
task_list=[]

def tasks(key):
    if(key==1):
        id = len(task_list) + 1
        title=input('enter the title')
        description=input('enter the description')
        priority=input('enter the priority')
        due_date=input('enter the due date')
        status=input('enter the status')
        try:
            new_task=Task(id,title,description,priority,due_date,status)
            task_list.append(new_task)

            print("task is added")
        except ValueError as ve:
            print(f"❌ Error: {ve}")


    #if we dont use str function and try to print it will print address.
    elif(key==2):
        for task in task_list:
            print(task)

    elif(key==3):
        taskid=int(input('enter the id for the task'))

        for task in task_list:
            if(taskid==task.id):
                task.status='completed'
            else:
                print('id not found')

    elif(key==4):
        pendingtask=list(filter(lambda x:x.status=='pending',task_list))
        
        for task in pendingtask:
            print(task)




