import logging
import json
from expense import Expense
from json import JSONDecodeError
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
class Manager:
    def __init__(self):
        try:
            with open("data.json", "r") as f:
                self.ExpenseList = json.load(f)
        except (FileNotFoundError, JSONDecodeError) as e:
            logging.warning(e)
            self.ExpenseList = []

            with open("data.json", "w") as file:
                json.dump(self.ExpenseList, file)
            logging.info("File created")


    def add_expense(self):

        category = input("Give a category: ")
        description = input("Give a description: ")
        while True:
            try:
                amount_user = input("Give an amount: ")
                amount = int(amount_user)
                if amount < 0:
                    raise ValueError("Cant be lower 0")
                break
            except ValueError:
                logging.info("Amount must be an integer")


        tk = Expense(category, amount, description)

        self.ExpenseList.append(tk.to_dict())
        self.save_data()


    def save_data(self):
        with open("data.json", "w") as file:
                json.dump(self.ExpenseList, file, indent=4)


    def show_expense(self):
        for expense in self.ExpenseList:
            logging.info("Category: %s, Amount: %d, Description: %s", expense["category"], expense["amount"], expense["description"])


    def sum_per_category(self):
        user_category = input("Enter category: ").strip().lower()

        total = 0

        for expense in self.ExpenseList:
            category = expense["category"].strip().lower()
            amount = expense["amount"]

            if category == user_category:
                total += amount

        logging.info(f"Total for category '{user_category}': {total}")


    def remove_expense(self):
        delete = input("Del: ")
        for title in self.ExpenseList:
            if title['description'].lower() == delete:
                self.ExpenseList.remove(title)
                logging.info("Expense removed!")

        self.save_data()