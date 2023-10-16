import requests
import datetime
from user_program import Program
API = "YOUR SHEETY API"
SHEET_NAME = "YOUR SHEET NAME"
SHEET_INPUT_NAME = "YOUR SHEET'S PAGE NAME"
import requests
URL = f"https://api.sheety.co/{API}/{SHEET_NAME}/{SHEET_INPUT_NAME}"

class Sheety:
    def __init__(self, program: Program):
        self.amount = program.amount
        self.date = program.date
        self.sheet_inputs = {
            SHEET_INPUT_NAME: {
                "date": self.date,
                "tagada": self.amount
            }
        }

    def post_data(self):
        self.response = requests.post(url=URL, json=self.sheet_inputs)
        print(self.response.json())

