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

## Process
* Extract titles of all content IDs and store them in `title.json`
* Extract latest hashes of all content IDs and store them in `latest_hash.json`
* Create metadata and store it in `media.json`
