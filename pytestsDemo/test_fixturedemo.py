# -*- coding: utf-8 -*-
#import pytest
#
#def test_fixtureDemo(setup):
#    print("I will be executing steps in fixture demo")


import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")