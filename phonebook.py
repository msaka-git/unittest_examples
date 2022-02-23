# new clasass
password = "sdada3422"
class PhoneBook:
    numbers = {}
    # def __int__(self):
    #     self.numbers = {}

    def add(self,name,number):
        self.numbers[name] = number

    def lookup(self,name):
        return self.numbers[name]


