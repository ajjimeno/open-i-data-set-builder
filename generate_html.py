import json
from query_openi import image_types, data_folder
from tqdm import tqdm
import urllib.request

if __name__ == '__main__':
    print ('<html><body>')

    for k, v in image_types.items():
        print ('<h1>' + k + '</h1>')

        with open(data_folder + '/' + k + '_filtered.json', 'r') as f:
            images = json.load(f)

            for i in images:
                print('<img src="./data/imgs/' + i["imgLarge"].split("/")[-1] + '"/>')
                print('<br/>')
                print('<b>PMC:</b><a target=_new href=' + i["pmc_url"] + '>' + i["pmcid"] + '</a>')
                print('<br/>')
                print('<b>Problems:</b>' + i["Problems"])
                print('<br/>')
                print('<b>Caption:</b>' + i["image"]["caption"])
                print('<br/>')

    print('</body></html>')