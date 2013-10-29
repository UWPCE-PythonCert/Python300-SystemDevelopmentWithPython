import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('input', type=argparse.FileType('rb', 0))
parser.add_argument('output', type=argparse.FileType('wb', 0))
args = parser.parse_args()

i=0
for line in args.input:
    i += 1
    args.output.write("%d: %s" % (i,line))

