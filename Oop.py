# Object oriented programming

class Employee:
    # templates __(double underscore) means these variable are private
    __name = None
    __id = 0
    __salary = 0

    # constructor
    def __init__(self , name , id , salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    # self - means apne aap jo object jo create ho rha hai
    def set_name(self , name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


obj = Employee("aditya" , 202 , 200000)
print(obj.get_name())
print(obj.get_id())
print(obj.get_salary())
