from expenses import add_expenses,list_expenses,delete_expenses
from summary import print_summary
from storage import load_data,save_data

def show_menu():
    print("\n =======Expense tracker======")
    print(" 1. Add expense")
    print(" 2. View expense")
    print(" 3. Delete expenses")
    print(" 4. View summary")
    print(" 5. Exit")

def main():
    expense=load_data()

    while True:
        show_menu()
        prompt=input("Enter your choice (1-5):")
        try:
            choice=int(prompt)
        except ValueError as e:
            print("value error, Enter valid number (1-5)")
        if choice==1:
            
            amount=int(input("Enter your spending: "))
            category=input("Category spent: ")
            description=input("Why spent? ")

            add_expenses(expense,amount,category,description)
            save_data(expense)
        elif choice==2:
            list_expenses(expense)
        elif choice==3:
            index=int(input("Please Enter index for the expense you choose to delete :-"))
            delete_expenses(expense,index)
            save_data(expense)

        elif choice==4:
            print_summary(expense)
        elif choice==5:
            print("\n see you!!")
            break

if __name__=="__main__":
    main()


        
