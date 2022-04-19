import json
import requests

def query(image_type, limit=100):
    response = requests.get("https://openi.nlm.nih.gov/api/search?m=1&n=" + str(limit) + "&query=&it=xg,xm," + image_type + "&lic=by")
    return response.json()

data_folder = './data'

image_types = { 'CT': 'c', 'X-ray': 'x', 'PET': 'p', 'MRI': 'm', 'Ultrasound' : 'u' }

if __name__ == '__main__':
    
    for k, v in image_types.items():
        response = query(image_type = v, limit = 1000)

        with open(data_folder + "/" + k + '.json', 'w') as f:
            json.dump(response, f)