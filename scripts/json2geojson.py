#
# convert our json file format to geojson
#
#   to run this:
#   python json2geojson.py
#

import json

geojson = {
	"type": "FeatureCollection",
	"features": []
}

with open("../lafayette-co-public-art.json") as f:
	art_json = json.loads(f.read())
	for artwork in art_json:
		artwork_geojson = {
			"type": "Feature",
			"geometry": {
				"type": "Point", 
				"coordinates": [ artwork['longitude'], artwork['latitude'] ]
			},
			"properties": {
			    "collection": artwork['collection'],
			    "media": artwork['media'],
			    "address": artwork['address'],
			    "title": artwork['title'],
			    "artist": artwork['artist'],
			    "year": artwork['year'],
			    "image": artwork['image']
			}
		}
		geojson['features'].append(artwork_geojson)

with open('../lafayette-co-public-art.geojson', 'w') as f:
	f.write(json.dumps(geojson, sort_keys=True, indent=4, separators=(',', ': ')))