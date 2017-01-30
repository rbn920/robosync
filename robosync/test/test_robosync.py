import unittest
import os

class testMirror(unittest.TestCase):

    def setUp(self):
        dirnames = ['dir1', 'dir2', 'dir3']
        filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        for d_name, f_name in zip(dirnames, filenames):
            os.mkdir(d_name)
            with open(os.path.join(d_name, f_name), 'w') as f:
                f.write('foobar')


