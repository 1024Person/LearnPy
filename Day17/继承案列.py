"""
    公司的工资管理
        1、首先分析（或者构建）一个公司的组成----->CEO---(1:n)---》若干经理(若干经理之间还有关系)------>（高级，中级，底层）员工
        2、每个组成之间会有什么样的属性
            1、CEO：工资，工号，姓名，职务
            2、经理：工资，工号，姓名，职务
            3、工人：工资，工号，姓名，职务
        3、会有的动作：
            1、计算自己会有多少工资
            2、计算要分发多少工资
"""


class Person:
    def __init__(self, salary, no, name, position):
        self.name = name
        self.salary = salary
        self.no = no
        self.position = position

    def __str__(self):
        msg = '''
        工号：{}
        姓名：{}
        职位：{}
        月薪：{}
        '''.format(self.no, self.position, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Manager(Person):
    def __init__(self, name, no, salary, per_hours, hours, position):
        self.per_hours = per_hours
        self.hours = hours
        super().__init__(salary, no, name, position)

    def getSalary(self):
        money = self.per_hours * self.hours * 30
        self.salary += money
        return super().getSalary()


class Worker(Person):
    def getSalary(self, reward):
        self.salary += reward
        return super().getSalary()


class Salesclerk(Person):
    def __init__(self, salary, name, age, no, rate, position):
        self.rate = rate
        super().__init__(salary, no, name, position)

    def getSalary(self, money):
        self.salary += money * self.rate
        return super().getSalary()


m = Manager('Jack', '001', 15000, 100, 8, '经理')
print(m)
s = m.getSalary()
print(s)

w = Worker(5000, '005', '打工仔', '底层员工')
print(w)
print(w.getSalary(200))


