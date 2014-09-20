all: ../lafayette-co-public-art.json ../lafayette-co-public-art.geojson 

../lafayette-co-public-art.json: ../lafayette-co-public-art.csv csv2json.py
	python csv2json.py

../lafayette-co-public-art.geojson: ../lafayette-co-public-art.csv csv2geojson.py
	python csv2geojson.py
