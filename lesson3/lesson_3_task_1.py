from user import User

print("Введите ваше имя:")
first_name = input()
print("Введите вашу фамилию:")
last_name = input()

user = User()
user.set_first_name(first_name)
user.set_last_name(last_name)
user.say_full_name()