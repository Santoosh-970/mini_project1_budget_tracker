def add_expenses(expenses,amount,category,description):

    expense={
        "amount":amount,
        "category":category,
        "description":description
    }
    expenses.append(expense)
    print("Expense added successfully!")

def list_expenses(expenses):
    if not expenses:
        print("\n No expenses recorded yet!")
        return
    print("\n-----Your Expenses------ ")
    for i,exp in enumerate(expenses):
        print(f"\n{i}-->{exp['amount']} | {exp['category']}|{exp['description']}")

        print("------------------------------------")
def delete_expenses(expenses,index):
    if(index<0) or (index>=len(expenses)):
        print("/nInvalid index.!!")
        return
    removed=expenses.pop(index)
    print(f"\n deleted items:\n {index}.{removed['amount']} | {removed['category']}|{removed['description']}")


    



