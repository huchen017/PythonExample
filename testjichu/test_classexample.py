from jichu import classexample
import pytest


def test_classexample():
    person = classexample.Person("lili", "女", "湖北")
    print(person.total_person)
    print(person.name)
    print(person.get_name())
    print(person.get_sex())
    print(person.get_province())
    person2 = classexample.Person("lisa", "女", "湖北")
    print(person.total_person)






