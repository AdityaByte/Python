# Object oriented programming

class Employee:
    # templates __(double underscore) means these variable are private
    __name = None
    __id = 0
    __salary = 0

    # self - means apne aap jo object jo create ho rha hai
    def set_name(self , name):
        self.__name = name

    def get_name(self):
        return self.__name

obj = Employee()
obj.set_name("aditya pawar")
obj.get_name()
print(obj.get_name())
