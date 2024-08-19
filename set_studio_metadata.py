import subprocess
import os
import json
import re

def read_json_file(file_path):
    data = dict()
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    return data

def write_data(data, json_file):
    json_object = json.dumps(data, indent=4)
    with open(json_file, 'w') as file: file.write(json_object)

config_json_file = './config.json'
config_data = read_json_file(config_json_file)

os.environ['FABRIC_CONFIG_URL'] = config_data["config_url"]
os.environ['PRIVATE_KEY'] = config_data["private_key"]
mez_lib_id = config_data["mez_lib_id"]
utilities_path = config_data["utilities_path"]
media_catalog_id = config_data["media_catalog_id"]


def read_file_txt(file_txt):
    lines = set()
    if os.path.exists(file_txt):
        file = open(file_txt, 'r')
        line = file.readline()
        while line != '':
            lines.add(line.strip())
            line = file.readline()
    return lines

def get_metadata(object_id):
    try:
        command = ['node', 'MetaGet.js', '\\', '--objectId', object_id, '\\', '--path', '/public']
        result = subprocess.run(command, capture_output=True, text=True, cwd=utilities_path, check=True)
        split_lines = result.stdout.strip().split('\n')
        for i in range(len(split_lines)):
            if split_lines[i] == '{':
                start = i
            if split_lines[i] == '}':
                end = i + 1
        return json.loads('\n'.join(split_lines[start : end]))
    except:
        print('Cannot extract metadata from', object_id)


pattern = r'^(\S+)(\s+)(.*?)$'
info_types = {
    'title': ['--name'], 
    'latest_hash': ['--hash']
}

def get_info_of(type, lib_id):
    json_file = f'{type}.json'
    data = read_json_file(json_file)
    try:
        command = ['node', 'LibraryListObjects.js', '\\', '--libraryId', lib_id, '\\'] + info_types[type]
        result = subprocess.run(command, capture_output=True, text=True, cwd=utilities_path, check=True)
        split_lines = result.stdout.strip().split('\n')

        for i in range(len(split_lines)):
            if 'Found' in split_lines[i]:
                print(split_lines[i])
            if 'objectId' in split_lines[i]:
                j = i + 1
                while j < len(split_lines) and split_lines[j] != '' and split_lines[j] != 'Done.':
                    matching = re.match(pattern, split_lines[j].strip())
                    try:
                        extracted_data = [part for part in matching.groups() if part.strip() != '']
                        data[extracted_data[0]] = extracted_data[1]
                    except:
                        data[split_lines[j].strip()] = ''
                    j += 1
                print(len(data), 'objects')
                break
        print('Successfully extracted list of', type)
        write_data(data, json_file)
        return data
    
    except:
        print('Cannot extract list of objects')



def write_metadata():
    get_info_of('title', mez_lib_id)
    get_info_of('latest_hash', mez_lib_id)
    metadata = get_metadata(media_catalog_id)
    media = metadata['asset_metadata']['info']['media']
    
    title = read_json_file('title.json')
    latest_hash = read_json_file('latest_hash.json')

    for object_id in title:
        try:
            movie_id = 'mvid' + object_id[4:][:22]
            if movie_id in media:
                print(movie_id, 'already existed')
                movie_id = 'mvid' + object_id[5:][:22]
            media[movie_id] = {
                    "associated_media": [],
                    "attributes": {},
                    "catalog_title": title[object_id],
                    "clip": False,
                    "description": "",
                    "description_rich_text": "",
                    "headers": [],
                    "id": movie_id,
                    "label": title[object_id],
                    "live_video": False,
                    "media_catalog_id": "iq__4GTwdvyifajEUfnJMc8g4sX5iyCv",
                    "media_link": {
                        ".": {
                            "container": "hq__GZ2wHcSjAHHsFt4gARiryhf2RtX1ZZ15UfuAd9pdCuBzhi4sjDFei1cxCN9RqMamtiFUy66zmg"
                        },
                        "/": f"/qfab/{latest_hash[object_id]}/meta/public/asset_metadata"
                    },
                    "media_type": "Video",
                    "offerings": [],
                    "override_settings_when_viewed": False,
                    "permissions": [],
                    "player_profile": "",
                    "public": True,
                    "subtitle": "",
                    "tags": [],
                    "title": title[object_id],
                    "type": "media",
                    "viewed_settings": {
                        "description": "",
                        "description_rich_text": "",
                        "headers": [],
                        "subtitle": "",
                        "title": ""
                    }
                }
        except:
            pass

    write_data(metadata, 'media.json')

if __name__ == "__main__":
    write_metadata()
