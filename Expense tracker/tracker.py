from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import csv


class Expense:
    
    def __init__(self,expense,category,id):
        self.id=id
        self.cost=expense
        self.category=category

    def __str__(self):
         return f'cost-{self.cost} category-{self.category}'
        
    @property
    def category(self):
            return self._category
        
    @category.setter
    def category(self,category):
            if category not in ['food','tour','college']:
                raise ValueError('please enter correct category')
            self._category=category
    
    def save_to_csv(self,filepath="data/expense.csv"):
         date=datetime.now().strftime("%y-%m-%d")
         with open(filepath,'a',newline='') as file:
              writer=csv.writer(file)
              writer.writerow([date,self.cost,self.category,self.id])

def view_expense(filepath="data/expense.csv"):
        try:
            with open(filepath,'r',newline='') as file:
                reader=csv.reader(file)
                print("your expenses")
                print(f"{'Date':<12} {'Category':<12} {'Amount':<12} {'id':<12}")
                print("-" * 35)
                for row in reader:
                    if len(row)==4:
                        print(f'{row[0]:<12} {row[1]:<12} {row[2]:<12} {'id':<12}') 


        except FileNotFoundError:
            print("file not found")

def pie_viualizer(file_path="data/expense.csv"):
    category_total=defaultdict(float)
    try:
        with open(file_path,'r') as file:
            reader=csv.reader(file)
            for row in reader:
                if len(row)==4:
                        category=row[2].strip().lower()
                        try:
                            amount=float(row[1])
                            category_total[category]+=amount
                        except ValueError:
                            pass
                    
            if not category_total:
                print("No expenses to display.")
                return
            
        labels=list(category_total.keys())
        values=list(category_total.values())


        plt.figure(figsize=(6,6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title=('expense distribution')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("expense file not found")

def Task(key):
    id=0
    if(key==1):
        id=id+1
        expense=input("enter the expense")
        category=input("enter the category (tour,food,college)")
        try:
            expense1=Expense(expense,category,id)
           
            expense1.save_to_csv()
            print("expense added sucessesfully")
        except ValueError as e:
                print(e)


    elif(key==2):
         view_expense()
         
         
    elif(key==3):
         pie_viualizer()
         
         





    


