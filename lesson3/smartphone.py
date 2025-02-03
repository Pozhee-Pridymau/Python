class Smartphone:
    def __init__(self, brend_phone=None, phone_model=None, subscriber_number=None):
        self.brend_phone = brend_phone
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number

    def set_brend_phone(self, brend_phone):
        self.brend_phone = brend_phone
        print(f"Марка вашего телефона - {self.brend_phone}")

    def set_phone_model(self, phone_model):
        self.phone_model = phone_model
        print(f"Модель вашего телефона - {self.phone_model}")

    def set_subscriber_number(self):
        while True:
            subscriber_number = input("Введите номер телефона: ")
            
            if len(subscriber_number) == 12 and subscriber_number[:3] == "+79" and subscriber_number[3:].isdigit():
                self.subscriber_number = subscriber_number
                print(f"Ваш номер телефона: {self.subscriber_number}")
                break
            else:
                print("Ошибка! Номер телефона должен начинаться с '+79' и содержать всего 12 символов.")


my_smartphone = Smartphone()

print("Введите марку вашего телефона:")
brend_phone = input()
my_smartphone.set_brend_phone(brend_phone)

print("Введите модель вашего телефона:")
phone_model = input()
my_smartphone.set_phone_model(phone_model)

print("Введите ваш номер телефона:")
my_smartphone.set_subscriber_number()