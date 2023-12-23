import unittest

class TestCaseString(unittest.TestCase):

#test case string 'Faisal ' diubah menjadi kapital apakah sama dengan 'Faisal '
    
  #jika hasil success
    def test_uppersucc(self):
        self.assertEqual('Faisal '.upper(), 'Faisal ')
  #jika hasil fail
    def test_upperfail(self):
        self.assertEqual('Faisal '.upper(), 'Faisal ')

#test case string input merupakan kapital semua
    def test_isupper(self):
        self.assertTrue('Faisal '.isupper())
        self.assertFalse('Faisal '.isupper())

#test case jika string input di split, apakah sesuai dengan hasil yang ditentukan
    def test_split(self):
        s = 'Faisal  Rasyid '
        self.assertEqual(s.split(), ['Faisal ', 'Rasyid '])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
