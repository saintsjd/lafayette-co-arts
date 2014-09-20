#
# convert our csv master file to geojson
#
#   to run this:
#   python json2geojson.py
#

import json
import csv

geojson = {
	"type": "FeatureCollection",
	"features": []
}

with open("../lafayette-co-public-art.csv") as f:
	reader = csv.reader(f)
	reader.next()
	
	for row in reader:
		artwork_geojson = {
			"type": "Feature",
			"geometry": {
				"type": "Point", 
				"coordinates": [ float(row[7]) if row[7] else None, float(row[6]) if row[6] else None ]
			},
			"properties": {
			    "collection": row[0],
			    "media": row[1],
			    "address": row[2],
			    "title": row[3],
			    "artist": row[4],
			    "year": int(row[5]) if row[5] else None,
			    "image": row[8]
			}
		}
		geojson['features'].append(artwork_geojson)

with open('../lafayette-co-public-art.geojson', 'w') as f:
	f.write(json.dumps(geojson, sort_keys=True, indent=4, separators=(',', ': ')))