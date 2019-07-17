import sys, os, json
import cv2
from pathlib import Path
def gen_dt(filepath, box_ann_all, img_map):
    with open(filepath, 'r') as f:
        data = json.load(f)

    prefix = Path(filepath).stem
    for k, v in data.items():
        img_ann = dict()
        file_name = "%s_%s"%(prefix, k)
        image_id = img_map[file_name]
        for bb in v:
            box_ann = dict()
            box_ann['category_id'] = 1
            box_ann['image_id'] = image_id
            x,y,width,height = bb[0],bb[1],bb[2]-bb[0],bb[3]-bb[1]
            area = width * height
            box_ann['bbox'] = [x,y,width,height]
            box_ann['score'] = float(bb[4])
            box_ann_all.append(box_ann)
    return

map_file = sys.argv[1]
filedir = sys.argv[2]
with open(map_file, 'r') as f:
    name_map = json.load(f)
box_ann_all = []
filelist = os.listdir(filedir)
filelist = sorted(filelist)
for filename in filelist:
    filepath = os.path.join(filedir, filename)
    gen_dt(filepath, box_ann_all, name_map)

with open('aishu_barz_det.json', 'w') as f:
    json.dump(box_ann_all, f, indent=2)
