from db import client
from utils.class_bench import class_bench
from utils.func_bench import function_decorator
from view.my_class import Sleep
from view.my_function import sleep_one_sec


@function_decorator
def lets_try(test: str):
    sleep_one_sec()
    print(test)


@class_bench
class Users:
    testing: dict

    def __init__(self, testing):
        self.testing = testing

    def add_user(self, testing):
        self.testing = testing
        Sleep.sleep_three_sec(Sleep)

    def find_user(self, testing):
        self.testing = testing
        Sleep.sleep_two_sec(Sleep)


lets_try('Go')
database = client.users
usernames = database.usernames


user_1 = {
    'name': 'Py',
    'surname': 'Thon',
    'role': 'Superadmin'
}

rest_of_users = [
    {
        'name': 'Ivan',
        'surname': 'Taranov',
        'role': 'user'
    },
    {
        'name': 'Paul',
        'surname': 'Sheeran',
        'role': 'user'
    },
    {
        'name': 'Eddy',
        'surname': 'Kellerman',
        'role': 'admin'
    }
]

result = usernames.insert_one(user_1)
result1 = usernames.insert_many(rest_of_users)
result2 = usernames.find_one({'surname': 'Thon'})
result3 = Users(user_1)
result3.add_user(user_1)
result4 = Users(rest_of_users)
result4.find_user(rest_of_users)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
