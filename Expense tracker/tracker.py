from datetime import datetime
import csv
from visualizer import plot_expenses

class Expense:
    def __init__(self,expense,category):
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
         date=datetime.now().strftime("%d-%m-%y")
         with open(filepath,'a',newline='') as file:
              writer=csv.writer(file)
              writer.writerow([date,self.cost,self.category])

def view_expense(filepath="data/expense.csv"):
        try:
            with open(filepath,'r',newline='') as file:
                reader=csv.reader(file)
                print("your expenses")
                print(f"{'Date':<12} {'Category':<12} {'Amount':<12}")
                print("-" * 35)
                for row in reader:
                    if len(row)==3:
                        print(f'{row[0]:<12} {row[1]:<12} {row[2]:<12}') 


        except FileNotFoundError:
            print("file not found")




def Task(key):
    if(key==1):
        expense=input("enter the expense")
        category=input("enter the category (tour,food,college)")
        try:
            expense1=Expense(expense,category,)
           
            expense1.save_to_csv()
            print("expense added sucessesfully")
        except ValueError as e:
                print(e)


    elif(key==2):
         view_expense()
         
         
    elif(key==3):
         plot_expenses()
         





    


