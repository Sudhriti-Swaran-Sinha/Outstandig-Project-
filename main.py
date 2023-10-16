from user_program import Program
from sheety import Sheety
from sms import Send_Sms

test_user_program = Program()
test_user_program.save_data()
test_sheety = Sheety(program=test_user_program)
test_sheety.post_data()
test_sms = Send_Sms(program=test_user_program)
test_sms.send_message()
