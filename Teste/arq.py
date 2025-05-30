"""
# ASSERT
def soma(a: int, b: int) -> int:
    assert a > 0 and b > 0, 'Ambos os valore devem ser positivos'
    return a + b

print(soma(2,4))
print(soma(-2,4))

"""
class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, outher):
        return self.name == outher.name
    
