import sys, os, json
import cv2
from pathlib import Path
image_id = 0
annotation_id = 0
def gen_ann(filepath, img_ann_all, box_ann_all, img_map):
    global image_id
    global annotation_id
    with open(filepath, 'r') as f:
        data = json.load(f)

    prefix = Path(filepath).stem
    for k, v in data.items():
        #k: frame_id
        img_ann = dict()
        #file_name: seq_0000_frameid.jpg
        file_name = "%s_%s"%(prefix, k)
        img_ann['file_name'] = file_name
        img_ann['id'] = image_id
        img_map[file_name] = image_id
        #image_id += 1
        img_ann['width'] = 1920
        img_ann['height'] = 1080
        for bb in v:
            box_ann = dict()
            box_ann['category_id'] = 1
            box_ann['image_id'] = image_id
            box_ann['id'] = annotation_id
            x,y,width,height = bb[0],bb[1],bb[2]-bb[0],bb[3]-bb[1]
            area = width * height
            box_ann['bbox'] = [x,y,width,height]
            box_ann['area'] =  area
            box_ann['iscrowd'] = 0
            annotation_id += 1
            box_ann_all.append(box_ann)
        image_id += 1
        img_ann_all.append(img_ann)
    return

filedir = sys.argv[1]
coco = dict()
coco['info'] = ""
coco['licenses'] = ""
coco['categories'] = [{"id":1, "name":'person', "supercategory":"object"}]
img_ann_all = []
box_ann_all = []
img_map = dict()
filelist = os.listdir(filedir)
filelist = sorted(filelist)
for filename in filelist:
    filepath = os.path.join(filedir, filename)
    gen_ann(filepath, img_ann_all, box_ann_all, img_map)
coco['images'] = img_ann_all
coco['annotations'] = box_ann_all
with open('aishu_human_detection_coco.json', 'w') as f:
    json.dump(coco, f, indent=2)

#for b in box_ann_all:
#    b['score'] = 1.0
with open('image_name_id_map.json', 'w') as f:
    json.dump(img_map, f, indent=2)
