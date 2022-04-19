import json
from query_openi import image_types, data_folder
from tqdm import tqdm
import urllib.request

if __name__ == '__main__':
    for k, v in image_types.items():
        print (k)
        with open(data_folder + '/' + k + '_filtered.json', 'r') as f:
            images = json.load(f)
            
            for i in tqdm(images):
                file_name = data_folder + "/imgs/" + i["imgLarge"].split("/")[-1]
                urllib.request.urlretrieve("https://openi.nlm.nih.gov" + i["imgLarge"], file_name)