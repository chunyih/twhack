from flask import Flask, request
import urllib2
app = Flask(__name__)


@app.route('/map/')
def get_duration():
    return ok
    #return get_location(get_location(request.args.get(ref)))

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

if __name__ == "__main__":
    app.run()
