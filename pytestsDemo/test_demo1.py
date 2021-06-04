# -*- coding: utf-8 -*-
#%%
import pytest

@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")
    
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
    print(crossBrowser)