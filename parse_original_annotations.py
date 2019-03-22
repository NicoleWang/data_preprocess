import sys, os, json
import cv2
import argparse

def parse_crowdHuman(ann_file_path, obj_class):
    with open(ann_file_path, 'r') as f:
        data  = [json.loads(x) for x in f.readlines()]
    out_dict = dict()
    for cnt, ann in enumerate(data):
        prefix = ann['ID'] #image name prefix
        bbs = ann['gtboxes']
        extract_bbs = []
        for bb in bbs:
            if bb['tag'] == 'mask':
                #tag is mask means that this box is crowd/reflection/something like person/... and need to be ignore
                continue
            if obj_class not in bb.keys():
                continue
            box = bb[obj_class]
            xmin = box[0]
            ymin = box[1]
            xmax = box[0] + box[2] - 1
            ymax = box[1] + box[3] - 1
            extract_bbs.append([xmin, ymin, xmax, ymax])
        out_dict[prefix] = extract_bbs
    return out_dict




def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='parse dataset into customed format')
    parser.add_argument('--dataset', dest='dataset', help="dataset to parse", type=str)
    parser.add_argument('--datapath', dest='datapath', help="dataset to parse", type=str)
    parser.add_argument('--obj_class', dest='obj_class', help="obj class to return", type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    data = parse_crowdHuman(args.datapath, args.obj_class)
    print data
    #imgdir = sys.argv[1]
    #ann_file = sys.argv[2]
    #tag = sys.argv[3]
    #outdir = sys.argv[4]
#        json_path = os.path.join(outdir, prefix+ ".json")
#        with open(json_path, 'w') as f:
#            json.dump(all_bbs, f)
