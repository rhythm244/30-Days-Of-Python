import random
import numpy

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


class Statistics:
    def __init__(self, num_list):
        self.num_list = num_list

    def count(self):
        thong = len(self.num_list)
        return f'{thong}'

    def plus(self):
        summ = 0
        for i in self.num_list:
            summ = summ + i
        return f'{summ}'

    def minn(self):
        mi = min(self.num_list)
        return f'{mi}'


class thong(Statistics):
    def __init__(self, num_list):
        self.num_list = num_list


def describe():
    stat = thong(ages)
    print(stat.count())
    print(stat.minn())
    print(stat.plus())


#Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, 
# total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its 
# description. The same goes for expenses.

class PersonAccount():
    def __init__(self, firstname, lastname, income, expense, properties):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income
        self.expense = expense
        self.properties = properties
        self.total_income = 0
    
    def add_income(self, add_income):
        self.total_income += add_income
        return 0

    def buy(self, cost):
        self.total_income -= cost
        return 0
    
    def info(self):
        return f'{self.total_income}'
            
thong = PersonAccount('wasawat', 'bourperk', 0, 'know', 'pilot')


thong.add_income(5000)
thong.add_income(10000)
thong.add_income(10000)
thong.add_income(500)
thong.buy(10000)

#ทำได้ซะทีเว้ยยยยยยยยยยยยย
print(thong.info())

# total = 0
# for i in thong.total_income:
#     total = total + i

# print(total)


# class Person:
#       def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city
#           self.skills = []

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
#       def add_skill(self, skill):
#           self.skills.append(skill)

# p1 = Person()
# print(p1.person_info())
# p1.add_skill('HTML')
# p1.add_skill('CSS')
# p1.add_skill('JavaScript')
# p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)


