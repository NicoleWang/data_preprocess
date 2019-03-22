import sys, os, json
import cv2

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = abs(box[2] - box[0])
    h = abs(box[3] - box[1])

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

imgdir = sys.argv[1]
jsondir = sys.argv[2]
txtdir = sys.argv[3]

namelist = os.listdir(jsondir)
for name in namelist:
    prefix = os.path.splitext(name)[0]

    imgpath = os.path.join(imgdir, prefix+".jpg")
    jsonpath = os.path.join(jsondir, prefix+".json")
    txtpath = os.path.join(txtdir, prefix+".txt")

    img = cv2.imread(imgpath)
    height, width = img.shape[:2]
    with open(jsonpath, 'r') as f:
        bbs = json.load(f)
    of = open(txtpath, 'w')
    for bb in bbs:
        x, y, w, h = convert((width, height), bb)
        of.write("%d\t%f\t%f\t%f\t%f\n"%(0,x,y,w,h))
    of.close()
