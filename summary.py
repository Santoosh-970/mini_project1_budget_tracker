
def total_spending(expenses):
    total=0
    for exp in expenses:
        total+=exp['amount']
    return total
    
def spending_by_category(expenses):
    
    total_rent=0
    total_insurance=0
    total_grocery=0
    total_saving=0
    for exp in expenses:  # need fixes and shortcut looping
        if exp['category']=="rent":
            total_rent+=exp['amount']
        if exp['category']=="insurance":
            total_insurance+=exp['amount']
        if exp['category']=="grocery":
            total_grocery+=exp['amount']
        if exp['category']=="saving":
            total_saving+=exp['amount']
    total_spending ={
          "rent":total_rent,
          "insurance":total_insurance,
          "grocery":total_grocery,
          "saving":total_saving
        }
    return total_spending

def highest_expenses(total_spending,expenses):
    if not expenses:
        print("\n No expenses recorded yet!")
        return
    
    highest_spending_key= max(total_spending,key=total_spending.get)
    highest_spending_value=total_spending[highest_spending_key]

    print(f"Highest spending in {highest_spending_key} and spent amount {highest_spending_value}")

    # for key,value in expenses:

    # ot_highest_spending_key= max(expenses, key=lambda x: x["amount"])
    # ot_highest_spending_value=ot_highest_spending_key['amount']
    # print(f"Highest spending in {ot_highest_spending_key} and spent amount {ot_highest_spending_value}")
    highest_exp = max(expenses, key=lambda x: x["amount"])
    print(f"Highest single expense: {highest_exp['amount']} on {highest_exp.get('description', 'Unknown')}"
            f" ({highest_exp['category']})")



def print_summary(expenses):

    print("\n------ SUMMARY ------")

    print(f"Altogether spending : {total_spending(expenses)}")

    category_totals = spending_by_category(expenses)

    print(f"Total spending in Rent :{category_totals['rent']}")
    print(f"Total spending in Insurance :{category_totals['insurance']}")
    print(f"Total spending in Grocery :{category_totals['grocery']}")
    print(f"Total spending in Saving :{category_totals['saving']}")


    # print(f"Highest spending category: {}")
    highest_expenses(category_totals,expenses)





    



            
        

        

            
            