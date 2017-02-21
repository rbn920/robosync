import unittest
import os
import shutil
import robosync

class testMirror(unittest.TestCase):

    def setUp(self):
        os.mkdir('testing_dir')
        os.chdir('testing_dir')
        self.source_dirs = ['dir1', 'dir2', 'dir3']
        self.dest_dirs = ['dir1_c', 'dir2_c', 'dir3_c']
        self.filenames = ['file1.txt', 'file2.txt', 'file3.txt']
        self.contents = ['foobar1', 'foobar2', 'foobar3']
        with open('source_file.txt', 'w') as f:
            f.write('\n'.join(self.source_dirs))

        with open('dest_file.txt', 'w') as f:
            f.write('\n'.join(self.dest_dirs))

        for d_name, f_name, content, in zip(self.source_dirs, self.filenames,
                                            self.contents):
            os.mkdir(d_name)
            with open(os.path.join(d_name, f_name), 'w') as f:
                f.write(content)


    def tearDown(self):
        os.chdir('..')
        shutil.rmtree('testing_dir')

    def test_read(self):
        inlist = robosync.read('source_file.txt')
        outlist = robosync.read('dest_file.txt')
        self.assertListEqual(inlist, self.source_dirs)
        self.assertListEqual(outlist, self.dest_dirs)

    def test_mirror(self):
        robosync.main('source_file.txt', 'dest_file.txt')
        for folder, filename, content in zip(self.dest_dirs, self.filenames,
                                             self.contents):
            f = robosync.read(os.path.join(folder, filename))
            self.assertEqual(f[0], content)


if __name__ == '__main__':
    unittest.main()
