import sys, os
from shutil import copyfile

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='copy files')
    parser.add_argument('--srcdir', dest='srcdir', help="src  dir", type=str)
    parser.add_argument('--dstdir', dest='dstdir', help="dst dir", type=str)
    parser.add_argument('--list_file', dest='list_file', help="namelist file", type=str)
    args = parser.parse_args()
    return args

args = parse_args()
srcdir = args.srcdir
dstdir = args.dstdir

if args.list_file is None:
    namelist =  os.listdir(srcdir)
    for cnt, name in enumerate(namelist):
        print cnt, name
        inpath = os.path.join(srcdir, name)
        outpath = os.path.join(dstdir, name)
        copyfile(inpath, outpath)
else :
    f = open(args.list_file, 'r')
    namelist = [x.strip() for x in f.readlines()]


