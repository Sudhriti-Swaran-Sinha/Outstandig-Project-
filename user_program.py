from datetime import datetime
class Program:
    def __init__(self):
        self.name = "Outstanding Program"
    def save_data(self):
        self.date = datetime.today().date().strftime("%d%m%Y")
        self.amount = input("Please enter the amount\n")
        print(f"You have successfully saved outstanding amount which is {self.amount} in {self.date}")
