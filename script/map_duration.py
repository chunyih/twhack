from flask import Flask, request, send_from_directory
import urllib2
import json
import duration_query

app = Flask(__name__, static_url_path='')
obj_duration = duration_query.DurationQuery()

json_file = '../data.json'
with open(json_file, 'r') as fin:
    json_data = json.loads(fin.read())

@app.route('/')
def root():
    return send_from_directory('..', 'index.html')

@app.route('/script.js')
def js():
    return send_from_directory('..', 'script.js')

@app.route('/map/')
def get_duration():
    location = get_location_from_json(request.args.get('ref'))
    if location:
        lng, lat = location
    else:
        return 'Error'
    # lng, lat = get_location(get_html(request.args.get('ref')))
    time = obj_duration.get_duration_from_lat_lng(lat, lng)
    # temp = get_location_from_json(request.args.get('ref'))

    maxTime = float(request.args.get('maxTime')) if request.args.get('maxTime') != '' else 60

    return str(time <= maxTime)

def get_location_from_json(ref):
    tmp = ref.split('/')[-1][:-5]
    for ele in json_data[0]:
        if ele['PostingID'].find(tmp) != -1:
            return [ele['Longitude'], ele['Latitude']]
    return None

craigslist_url_head = 'http://sfbay.craigslist.org'
def get_html(ref):
    """
    return html document of the given 'craigslist' reference.
    """
    response = urllib2.urlopen(craigslist_url_head+ref)
    return response.read()

def get_location(doc):
    """
    return tuple: (longtitude, latitude) on given craiglist 
    """
    longitude = float(get_string(doc, 'data-longitude', skip=2, length=11))
    latitude = float(get_string(doc, 'data-latitude', skip=2, length=9))
    return [longitude, latitude]

def get_string(doc, match, skip=0, length=1):
    index = doc.index(match)
    start_ind = index + len(match) + skip;
    return doc[start_ind:start_ind+length]

if __name__ == "__main__":
    app.debug = True
    app.run()
