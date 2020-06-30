import json
import requests
import os

jcenter_url = os.environ.get('JCENTER_URL')
instance_user = os.environ.get('INSTANCE_USER')
instance_password = os.environ.get('INSTANCE_PASSWORD')

def open_misc_file():
    with open('./packages.json') as mf:
        json_content = json.loads(mf.read())
        for c in json_content:
            url = jcenter_url + c['path'] + c['name']
            print(url)
            r = requests.get(url, auth=(instance_user, instance_password))
            print(r.status_code)

if __name__ == "__main__":
    open_misc_file()
