# -*- coding: utf-8 -*-

#import pytest
#
#@pytest.mark.usefixtures("dataLoad")
#class Testexample2:
#    def test_editprofile(self,dataLoad):
#        print(dataLoad)
#        print(dataLoad[0])

import pytest

from pytestsDemo.Baseclass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])