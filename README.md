# set_studio_metadata
A script to set Eluvio Studio metadata (with only titles and latest hashes being extracted)

## Installation
```
git clone https://github.com/eluv-io/elv-utils-js
cd elv-utils-js
npm install
```

## Configuration Setup
* Create `config.json`
* Copy and paste the script provided below

```
{
    "config_url": "URL for the configuration",
    "private_key": "Private key",
    "mez_lib_id": "Mezzanine library ID",
    "utilities_path": "/path/to/utilities",
    "media_catalog_id": "Media catalog ID"
}
```

## Command
```
python studio_set_metadata.py
```
Copy the output metadata from `media.json` and paste it on the Media Catalog or use MetaSet utility to set metadata

## Process
* Extract titles of all content IDs and store them in `title.json`
* Extract latest hashes of all content IDs and store them in `latest_hash.json`
* Create metadata and store it in `media.json`
```
{
    "asset_metadata": {
        "info": {
            "description": "",
            "id": "iq__4GTwdvyifajEUfnJMc8g4sX5iyCv",
            "media": {
                "mvid12FCjEU254BsRpzqe97VS7cmcUZ": {
                    "associated_media": [],
                    "attributes": {},
                    "catalog_title": "The Wild Bunch (4/10) - 1969",
                    "clip": false,
                    "description": "\"If they move, kill 'em!\" Beginning and ending with two of the bloodiest battles in screen history, Sam Peckinpah's classic revisionist Western ruthlessly takes apart the myths of the West...",
                    "description_rich_text": "",
                    "headers": [],
                    "id": "mvid12FCjEU254BsRpzqe97VS7cmcUZ",
                    "label": "The Wild Bunch (4/10) - 1969",
                    "live_video": false,
                    ...

                "mvid12YFwoq4xprd1FwY1f7B1TL1jTc": {
                    "associated_media": [],
                    "attributes": {},
                    "catalog_title": "Holy Smoke (10/12) - 1999",
                    "clip": false,
                    "description": "It's said that sex and religion are two subjects that no one can discuss without arguing; writer/director Jane Campion tackles both head-on in this satiric comedy drama...",
                    "description_rich_text": "",
                    "headers": [],
                    "id": "mvid12YFwoq4xprd1FwY1f7B1TL1jTc",
                    "label": "Holy Smoke (10/12) - 1999",
                    "live_video": false,
                    ...

            "media_collections": {},
            "media_lists": {},
            "name": "music_green_main",
            "permission_sets": [],
            "tags": [],
            "title": "music_green_main"
        }
    },
    "description": "",
    "name": "Media Catalog - music_green_main"
}
```
