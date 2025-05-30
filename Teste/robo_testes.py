import unittest as t

from robo import Robo

class RoboTeste(t.TestCase):
    def setUp(self):
        print('setUp() sendo executado ...')
        self.mega = Robo('Mega', bateria=50)


    def test_carregar(self):
        self.mega.carregar()
        self.assertEqual(self.mega.bateria, 100)


    def test_dizer_nome(self):
        self.assertEqual(self.mega.fala_nome(), 'BEP BOOP. EU SOU MEGA')
        self.assertEqual(self.mega.bateria, 49, 'Bateria deveria estar em 49')

    def tearDown(self):
        print('tearDown() sendo executado ...')
        
if __name__ == '__main__':
    t.main()