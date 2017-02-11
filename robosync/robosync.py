import subprocess
import sys

def read(txtfile):
    with open(txtfile, 'r') as f:
        dir_names = [folder for folder in f]

    return dir_names

def main(infile, outfile):

    sources = read(infile)
    destinations = read(outfile)
    for s, d in zip(sources, destinations):
        subprocess.call(['robocopy', s, d, '/MIR'])

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

