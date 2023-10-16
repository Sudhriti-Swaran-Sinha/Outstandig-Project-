import os
from twilio.rest import Client
from user_program import Program
USER_PHONE_NUM = 'YOUR TWILIO PH NO'
CLIENT_PHONE_NUM = 'YOUR CLIENT PH NO'
class Send_Sms:
    def __init__(self, program: Program):
        self.account_sid = 'YOUR TWILIO ACC SID'
        self.auth_token = 'YOUR TWILIO AUTH TOKEN'
        self.client = Client(self.account_sid, self.auth_token)
        self.date = program.date
        self.amount = program.amount
    def send_message(self):
        self.message = self.client.messages.create(
                from_=USER_PHONE_NUM,
                body=f'Hello, [YOUR NAME]\nThis msg is to inform you that .......\nOutstanding amount {self.amount} is sucessfully'
                     f' returned on {self.date}\n Thank you',
                to=CLIENT_PHONE_NUM

        )
        print(self.message.status)

