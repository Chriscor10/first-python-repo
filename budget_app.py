



def main():
    print("Welcome to the Budget App")
    initial_budget = float(input("Please enter your initial budget: "))
    # filepath = 'budget_data.json'  # Define the path to your JSON file
    # initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()