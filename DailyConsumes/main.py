from manager import Manager
manager = Manager()


def main_menu():
    while True:
        print("\n=== EXPENSE MANAGER ===")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Sum per category")
        print("4. Delete expense")
        print("0. Exit")

        choice = input("Choose option: ").strip()

        match choice:
            case "1":
                print("Add expense selected")
                manager.add_expense()
            case "2":
                print("Show all expenses selected")
                manager.show_expense()
            case "3":
                print("Sum per category selected")
                manager.sum_per_category()
            case "4":
                print("Delete expense selected")
                manager.remove_expense()
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, try again")
main_menu()