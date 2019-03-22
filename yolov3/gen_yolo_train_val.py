import sys, os
import random

train_dir = sys.argv[1]
val_dir = sys.argv[2]
imgdir = sys.argv[3]
train_path = 'train_yolo.txt'
val_path = 'val_yolo.txt'
tfile = open(train_path, 'w')
vfile = open(val_path, 'w')

train_list = os.listdir(train_dir)
val_list = os.listdir(val_dir)

random.shuffle(train_list)
random.shuffle(val_list)
for idx, name in enumerate(train_list):
    #tpath = os.path.join(indir)
    prefix = os.path.splitext(name)[0]
    imname = prefix + ".jpg"
    abspath = os.path.join(os.path.abspath(imgdir), imname)
    tfile.write("%s\n"%abspath)

for idx, name in enumerate(val_list):
    #tpath = os.path.join(indir)
    prefix = os.path.splitext(name)[0]
    imname = prefix + ".jpg"
    abspath = os.path.join(os.path.abspath(imgdir), imname)
    vfile.write("%s\n"%abspath)

tfile.close()
vfile.close()
