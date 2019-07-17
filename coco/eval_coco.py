import sys, json
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

gt_json_file = sys.argv[1]
dt_json_file = sys.argv[2]
ann_type = 'bbox'
coco_gt = COCO(gt_json_file)
coco_res = coco_gt.loadRes(dt_json_file)
coco_eval = COCOeval(coco_gt, coco_res, ann_type)
coco_eval.params.useSegm = False
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()
