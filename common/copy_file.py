import sys, os
from shutil import copyfile
import argparse

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='copy files')
    parser.add_argument('--srcdir', dest='srcdir', help="src  dir", type=str)
    parser.add_argument('--dstdir', dest='dstdir', help="dst dir", type=str)
    parser.add_argument('--list_file', dest='list_file', help="namelist file", type=str)
    parser.add_argument('--extname', dest='extname', help="replace file extname", type=str)
    args = parser.parse_args()
    return args 

def do_copy(srcdir, dstdir, namelist):
    for cnt, name in enumerate(namelist):
        print cnt, name
        inpath = os.path.join(srcdir, name)
        outpath = os.path.join(dstdir, name)
        copyfile(inpath, outpath)

args = parse_args()
srcdir = args.srcdir
dstdir = args.dstdir

if args.list_file is None:
    namelist =  os.listdir(srcdir)
else :
    with open(args.list_file, 'r') as f:
        if args.extname is None:
            namelist = [x.strip() for x in f.readlines()]
        else:
            pass
            #namelist = [x.strip().replace(x.[-4:], args.extname) for x in f.readlines()]
do_copy(srcdir, dstdir, namelist)

