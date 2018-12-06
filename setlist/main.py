import unittest
class PlaylistTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, True)
    def test2(self):
        self.assertEqual(True, True)
    def test3(self):
        self.assertFalse(True == False)

if __name__== "__main__": unittest.main()