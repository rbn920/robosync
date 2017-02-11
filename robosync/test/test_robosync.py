import unittest
import os
import shutil

class testMirror(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_source')
        os.mkdir('test_dest')
        source_dirs = ['dir1', 'dir2', 'dir3']
        filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        contents = ['foobar1', 'foobar2', 'foobar3']
        for d_name, f_name, content, in zip(source_dirs, filenames, contents):
            new_dir = os.path.join('test_source', d_name)
            os.mkdir(new_dir)
            with open(os.path.join('test_source', d_name, f_name), 'w') as f:
                f.write(content)


    def tearDown(self):
        shutil.rmtree('test_source')
        shutil.rmtree('test_dest')


    def test_mirror(self):
        pass

if __name__ == '__main__':
    unittest.main()
