#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"a test module"

__author__ = "BanishedWay"

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world!")
    elif len(args) == 2:
        print("Hello %s" % args[1])
    else:
        print("Too many arguments!")


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Student(%s, %s)" % (self.name, self.age)

    def __repr__(self):
        return "Student(%s, %s)" % (self.name, self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


if __name__ == "__main__":
    test()
    s = Student("BanishedWay", 18)
    print(s)
