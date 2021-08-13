import os
import json

#json_path:存放json文件的绝对路径
#image_path:存放图片的绝对路径

def change_json_path(json_path, image_path):
    for jsonfile_name in os.listdir(json_path):
        jsonfile_path = os.path.join(json_path, jsonfile_name)                 #得到一个json文件的路径
        with open(jsonfile_path,"r") as f:
            dic = json.load(f)                                                 #json -> dict
            image_name = str.replace(jsonfile_name, ".json", ".jpg")           #图片名.json -> 图片名.jpg
            dic["imagePath"] = os.path.join(image_path, image_name)            #修改imagePath
        
        with open(jsonfile_path,"w") as f:
            json.dump(dic,f,sort_keys=True,indent=4,ensure_ascii=False)        #dict -> json


if __name__ == '__main__':
    
    json_path = r"C:\Users\yanxiang\Desktop\统计手的检测\helmet_labels"
    image_path = r'C:\Users\yanxiang\Desktop\markSafeHelmet_partFour\helmet'
    
    change_json_path(json_path, image_path)