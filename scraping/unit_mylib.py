import unittest
import mylib

class Filename_from_url(unittest.TestCase):

    def test_positive_with_https(self):
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library/unittest.html'), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library/unittest.html',True), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library/unittest.html/'), '')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library/unittest.html/', True), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library'), 'library')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library', True), 'library')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library/unittest.html?hello=world&world=hello'), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org/3/library/unittest.html?hello=world&world=hello', True), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org'), '')
        self.assertEqual(mylib.filename_from_url('https://docs.python.org', True), 'index.html')

    def test_positive_without_https(self):
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library/unittest.html'), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library/unittest.html',True), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library/unittest.html/'), '')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library/unittest.html/', True), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library'), 'library')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library', True), 'library')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library/unittest.html?hello=world&world=hello'), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('docs.python.org/3/library/unittest.html?hello=world&world=hello', True), 'unittest.html')
        self.assertEqual(mylib.filename_from_url('docs.python.org'), '')
        self.assertEqual(mylib.filename_from_url('docs.python.org', True), 'index.html')

if __name__ == '__main__':
    unittest.main()
