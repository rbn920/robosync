import unittest
import os
import shutil
import robosync

class testMirror(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_source')
        os.mkdir('test_dest')
        self.source_dirs = ['dir1', 'dir2', 'dir3']
        self.dest_dirs = ['dir1_c', 'dir2_c', 'dir3_c']
        filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        contents = ['foobar1', 'foobar2', 'foobar3']
        with open('source_file.txt', 'w') as f:
            f.write('\n'.join(self.source_dirs))

        with open('dest_file.txt', 'w') as f:
            f.write('\n'.join(self.dest_dirs))

        for d_name, f_name, content, in zip(self.source_dirs, filenames, contents):
            new_dir = os.path.join('test_source', d_name)
            os.mkdir(new_dir)
            with open(os.path.join('test_source', d_name, f_name), 'w') as f:
                f.write(content)


    def tearDown(self):
        shutil.rmtree('test_source')
        shutil.rmtree('test_dest')
        os.remove('source_file.txt')
        os.remove('dest_file.txt')

    def test_read(self):
        inlist = robosync.read('source_file.txt')
        outlist = robosync.read('dest_file.txt')
        self.assertListEqual(inlist, self.source_dirs)
        self.assertListEqual(outlist, self.dest_dirs)

    def test_mirror(self):
        pass

if __name__ == '__main__':
    unittest.main()
