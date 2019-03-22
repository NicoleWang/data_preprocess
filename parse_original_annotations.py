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

def parse_AIC(ann_file_path, obj_class):
    with open(ann_file_path, 'r') as f:
        data = json.load(f)
    out_dict = dict()
    for cnt, ann in enumerate(data):
        prefix = ann['image_id']
        bbs = ann[obj_class]
        extract_bbs = []
        for h, b in bbs.iteritems():
            extract_bbs.append(b)
        if len(extract_bbs) == 0:
            continue
        out_dict[prefix] = extract_bbs
    return out_dict

def show_some_of_dict(d, n):
    cnt = 0
    for key, val in d.iteritems():
        if cnt >= n:
            break
        print key
        print val
        cnt += 1

def parse_args():
    #parse input arguments
    parser = argparse.ArgumentParser(description='parse dataset into customed format')
    parser.add_argument('--dataset', dest='dataset', help="dataset to parse", type=str)
    parser.add_argument('--ann_file', dest='ann_file', help="annotation file path", type=str)
    parser.add_argument('--obj_class', dest='obj_class', help="obj class to return", type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    if args.dataset == 'crowdHuman':
        data = parse_crowdHuman(args.ann_file, args.obj_class)
        #print data
    if args.dataset == 'AIC':
        data = parse_AIC(args.ann_file, args.obj_class)
        show_some_of_dict(data, 10)
    #imgdir = sys.argv[1]
    #ann_file = sys.argv[2]
    #tag = sys.argv[3]
    #outdir = sys.argv[4]
#        json_path = os.path.join(outdir, prefix+ ".json")
#        with open(json_path, 'w') as f:
#            json.dump(all_bbs, f)
