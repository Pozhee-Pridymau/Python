class User:
    
    def set_first_name(self, first_name):
        self.first_name = first_name
        print(f"Ваше имя - {self.first_name}")

    def set_last_name(self, last_name):
        self.last_name = last_name
        print(f"А фамилия - {self.last_name}")

    def say_full_name(self):
        print(f"Значит вы - {self.first_name} {self.last_name}?")