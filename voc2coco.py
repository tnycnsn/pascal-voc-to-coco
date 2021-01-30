import os
import numpy as np
import json

voc_path = "pothole_voc_kargo\\Test_annotations"

coco_dict = {"info": {}, 
			"licences": [],
			"categories": [],
			"images": [],
			"annotations": []
			}

coco_dict["info"] = {"year": 2021,
					"version": 1.0,
					"description": "South Africa Potholes",
					"contributor": "dunno :(",
					"url": "dunno too :(",
					"date_created": "2021/01/29"
					}

coco_dict["licences"] = [{"id": 1, "name": "doesnt matter", "url": "none"}]
coco_dict["categories"] = [{"id": 1, "name": "pothole", "supercategory": "pothole"}]


for voc_name in os.listdir(voc_path):
	
	img_dict = {"id": int(voc_name[1:-4]), "width": 3680, "height": 2760, "file_name": voc_name[:-3]+"JPG", "license": 1, "date_captured": "2019-12-04 17:02:52"}
	coco_dict["images"].append(img_dict)
	
	voc_file = open(os.path.join(voc_path, voc_name), "r")
	voc_content = voc_file.read()
	xmins = [int(xm[1:-2]) for xm in voc_content.split("xmin")[1::2]]
	ymins = [int(ym[1:-2]) for ym in voc_content.split("ymin")[1::2]]
	xmaxes = [int(xm[1:-2]) for xm in voc_content.split("xmax")[1::2]]
	ymaxes = [int(ym[1:-2]) for ym in voc_content.split("ymax")[1::2]]
	
	pothole_id_count = 0
	for i in range(len(xmins)):
		iscrowd = [1 if len(xmins) > 1 else 0][0]
		anno_dict = {"id": int(voc_name[1:-4] + str(pothole_id_count)), "image_id": int(voc_name[1:-4]), "category_id": 1, "segmentation":[],
					"area": float((xmaxes[i]-xmins[i])*(ymaxes[i]-ymins[i])), "bbox": [xmins[i], ymins[i], (xmaxes[i]-xmins[i]), (ymaxes[i]-ymins[i])], "iscrowd": iscrowd}
		pothole_id_count += 1
		coco_dict["annotations"].append(anno_dict)


with open("pothole_coco_test.json", 'w') as fp:
	json.dump(coco_dict, fp)

#print(coco_dict.keys())
#app_json = json.dumps(coco_dict)
#print(app_json)
