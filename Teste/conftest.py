import pytest as t
from arq import Fruit

@t.fixture()
def my_fruit():
    return Fruit("apple")

@t.fixture()
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]
