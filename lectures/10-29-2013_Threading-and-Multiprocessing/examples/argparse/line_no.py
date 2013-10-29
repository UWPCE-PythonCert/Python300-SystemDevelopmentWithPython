import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('input', type=argparse.FileType('rb', 0))
parser.add_argument('output', type=argparse.FileType('wb', 0))
args = parser.parse_args()

for i,line in enumerate(args.input):
    args.output.write("%d: %s" % (i,line))

