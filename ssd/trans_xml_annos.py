from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import sys, os, string, json
import cv2

indir = sys.argv[1]
imgdir = sys.argv[2]
outdir = sys.argv[3]
#cate_map = {1:'coca', 2:'sprites', 3:'schweppes', 4:'watsons'}

namelist = os.listdir(indir)

for idx, name in enumerate(namelist):
    '''
    if idx > 4:
         break
    '''
    print "processing %s"%name
    prefix = os.path.splitext(name)[0]
    inpath = os.path.join(indir, name)

    outpath = os.path.join(outdir, prefix+".xml")
    if os.path.isfile(outpath):
      continue
    imname = prefix+".jpg"
    impath = os.path.join(imgdir, imname)
    img = cv2.imread(impath)
    height, width, chs = img.shape
    with open(inpath, 'r') as f:
        ori_annos = json.load(f)

    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'Person'
    #file name
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = imname
    #image info
    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = str(width).decode('utf8')
    node_height = SubElement(node_size, 'height')
    node_height.text = str(height).decode('utf8')
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = str(3).decode('utf8')

    #object annotation
    ori_bbs = ori_annos
    #ori_lbs = ori_annos['labels']
    for bb_id, bb in enumerate(ori_bbs):
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = "person"
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(max(bb[0], 0)).decode('utf8')
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(max(bb[1], 0)).decode('utf8')
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(min(bb[2], width-1)).decode('utf8')
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(min(bb[3], height-1)).decode('utf8')
    xml_annos = tostring(node_root, pretty_print=True)
    #final_dom = parseString(xml_annos)
    #print final_dom
    with open(outpath, 'w') as f:
        f.write(xml_annos)


