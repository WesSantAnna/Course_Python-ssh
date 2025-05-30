
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
    assert len(fruit_basket) == 2
    assert fruit_basket[0].name == "banana"
    assert fruit_basket[1].name == "apple"

