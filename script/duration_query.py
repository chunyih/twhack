from datetime import datetime

import googlemaps

API_KEY = 'AIzaSyCavOkaUq13RcTsSpO29Ne1t7zQMl9VXmE'
VALID_MODES = ('transit', 'driving', 'bicylcing', 'walking')


class DurationQuery(object):
    def __init__(self):
        self._gmaps = googlemaps.Client(key=API_KEY)
        self._mode = 'transit'
        self._destination = 'Palo Alto, CA'
        self._departure_time = None

    def get_duration(self, origin):
        if not self._departure_time:
            departure_time = datetime.now()
        out = self._gmaps.directions(
            origin,
            self._destination,
            mode=self._mode,
            departure_time=departure_time
        )
        duration = out[0]['legs'][0]['duration']['value']
        duration_in_mins = float(duration) / 60.0
        return duration_in_mins

    def get_duration_from_lat_lng(self, lat=0, lng=0):
        origin = {'lat': lat, 'lng': lng}
        return self.get_duration(origin)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, val):
        if val not in VALID_MODES:
            raise ValueError('Mode %s is not valid' % val)
        self._mode = val

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, val):
        self._destination = val

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, val):
        self._departure_time = val
