import json
from query_openi import image_types, data_folder

if __name__ == '__main__':
    for k, v in image_types.items():
        output = []
        with open(data_folder + '/' + k + '.json', 'r') as f:
            response = json.load(f)
            for i in response["list"]:
                if k in i["image"]["caption"]:
                    output.append(i)

        print(k, len(output))

        with open(data_folder + '/' + k + '_filtered.json', 'w') as f:
            json.dump(output, f)