"""
# ASSERT
def soma(a: int, b: int) -> int:
    assert a > 0 and b > 0, 'Ambos os valore devem ser positivos'
    return a + b

print(soma(2,4))
print(soma(-2,4))

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, outher):
        return self.name == outher.name
    


"""
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

