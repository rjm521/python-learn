#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Employee:
    empCount = 0 # 类共享的属性

    # 类的构造函数，每个实例都属性都定义在这里
    def __init__(self, name, salary):
        self.name = name     # 每个实例的属性
        self.salary = salary # 每个实例的属性
        Employee.empCount += 1

    def displayCount(self):
        print("total employee [%d]" % Employee.empCount)

    def displayEmployee(self):
        print("my name is:[%s]" % self.name + "\tsalary:[%s]" % self.salary)

jimmy = Employee("jimmy", 1234567)
jack  = Employee("jack", 7654321)

jimmy.displayCount()
jack.displayCount()
jimmy.displayEmployee()
jack.displayEmployee()