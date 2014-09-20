#
# convert our csv master file to geojson
#
#   to run this:
#   python json2geojson.py
#

import json
import csv

json_output = []

with open("../lafayette-co-public-art.csv") as f:
	reader = csv.reader(f)
	reader.next()
	for row in reader:
		artwork_json = {
		    "address": row[2],
		    "artist": row[4],
		    "collection": row[0],
			"latitude": float(row[6]) if row[6] else None,
			"longitude": float(row[7]) if row[7] else None,
		    "media": row[1],
		    "title": row[3],
		    "year": int(row[5]) if row[5] else None,
		    "image": row[8]
		}
		json_output.append(artwork_json)

with open('../lafayette-co-public-art.json', 'w') as f:
	f.write(json.dumps(json_output, sort_keys=True, indent=4, separators=(',', ': ')))