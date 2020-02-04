import unittest
import pyglatin


class TestPyglatin(unittest.TestCase):

    def test_convert(self):
        self.assertEqual('"Ere\'swhay ethay eefbay?" eshay askeday, incredulouslyay.',
                         pyglatin.convert(
                             '"Where\'s the beef?" she asked, incredulously.'))

    def test_html(self):
        self.assertEqual('<emay> Atwhay ethay atwhay? </emay>',
                         pyglatin.convert('<em>What the what?</em>'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
