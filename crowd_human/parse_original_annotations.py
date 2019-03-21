import sys, os, json
import cv2

imgdir = sys.argv[1]
ann_file = sys.argv[2]
tag = sys.argv[3]
outdir = sys.argv[4]

with open(ann_file, 'r') as f:
    data  = [json.loads(x) for x in f.readlines()]

for ann in data:
    prefix = ann['ID']
    bbs = ann['gtboxes']
    all_bbs = []
    for bb in bbs:
        if bb['tag'] == 'mask':
            continue
        if tag in bb.keys():
            box = bb[tag]
            xmin = box[0]
            ymin = box[1]
            xmax = box[0] + box[2] - 1
            ymax = box[1] + box[3] - 1
            all_bbs.append([xmin, ymin, xmax, ymax])
    json_path = os.path.join(outdir, prefix+ ".json")
    with open(json_path, 'w') as f:
        json.dump(all_bbs, f)
