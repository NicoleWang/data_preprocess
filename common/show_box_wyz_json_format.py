import sys, os, json
import argparse
import cv2

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='show bbox annotatation ')
    parser.add_argument('--imgdir', dest='imgdir', help="img dir", type=str)
    parser.add_argument('--ann', dest='ann', help="ann dir or path", type=str)
    #parser.add_argument('--mode', dest='obj_class', help="dir or path", type=str)
    args = parser.parse_args()
    return args

def show_single_image(impath, annpath):
    img = cv2.imread(impath)
    with open(annpath, 'r') as f:
        bbs = json.load(f)
    for box in bbs:
        xmin = box[0]
        ymin = box[1]
        xmax = box[2]
        ymax = box[3]
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 244, 0), 2)
    cv2.imshow("image", img)
    cv2.waitKey()

args = parse_args()
imgdir = args.imgdir
ann = args.ann

if os.path.isdir(ann):
    namelist = os.listdir(ann)
    for name in namelist:
        prefix = os.path.splitext(name)[0]
        imname = prefix + ".jpg"
        impath = os.path.join(imgdir, imname)
        annpath = os.path.join(ann, name)
        show_single_image(impath, annpath)

if os.path.isfile(ann):
    name = ann.split('/')[-1]
    prefix = os.path.splitext(name)[0]
    imname = prefix + '.jpg'
    impath = os.path.join(imgdir, imname)
    show_single_image(impath, ann)
