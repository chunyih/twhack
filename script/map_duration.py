from flask import Flask, request, send_from_directory
import urllib2

import duration_query

app = Flask(__name__, static_url_path='')
duration = duration_query.DurationQuery()

@app.route('/')
def root():
    return send_from_directory('..', 'index.html')

@app.route('/')
def root():
    return send_from_directory('..', 'index.html')

@app.route('/script.js')
def js():
    return send_from_directory('..', 'script.js')

@app.route('/map/')
def get_duration():
    return get_location(get_html(request.args.get('ref')))

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
    return "{0}".format([longitude, latitude])

def get_string(doc, match, skip=0, length=1):
    index = doc.index(match)
    start_ind = index + len(match) + skip;
    return doc[start_ind:start_ind+length]

if __name__ == "__main__":
    app.debug = True
    app.run()
