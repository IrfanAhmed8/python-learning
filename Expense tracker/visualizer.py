import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def plot_expenses(file_path='data/expense.csv'):
    category_totals = defaultdict(int)

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 3:
                continue
            category, amount = row[1], row[2]
            try:
                category_totals[category] += float(amount)
            except ValueError:
                pass

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.bar(categories, amounts, color='skyblue')
    plt.title('Expense by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Spent')
    plt.tight_layout()
    plt.show()
