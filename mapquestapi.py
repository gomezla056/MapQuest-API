import json
import urllib.parse
import urllib.request


Map_Quest_API_Key = 'ksrs2ay4kGqR93L8PggDPa3zWQDcweba'

Map_Quest_Base_Route_URL = 'http://open.mapquestapi.com/directions/v2'

Map_Quest_Base_Elevation_URL = 'http://open.mapquestapi.com/elevation/v1'


def direction_route_url(locations: list) -> str:
    '''This function returns the URL needed for directions to the user's
    desired location
    '''
    if len(locations) == 2:
        query_parameters = [
            ('key', Map_Quest_API_Key),
            ('from', locations[0]),
            ('to', locations[1])
            ]
        return Map_Quest_Base_Route_URL + '/route?' + urllib.parse.urlencode(query_parameters)
    elif len(locations) == 3:
        query_parameters = [
            ('key', Map_Quest_API_Key),
            ('from', locations[0]),
            ('to', locations[1]),
            ('from', locations[1]),
            ('to', locations[2])
            ]
        return Map_Quest_Base_Route_URL + '/route?' + urllib.parse.urlencode(query_parameters)


def elevation_route_url(lat_and_long: list) -> str:
    '''This function returns the URL need for the elevations of the user's
    desired location(s)
    '''
    query_parameters = [
        ('key', Map_Quest_API_Key),
        ('shapeFormat', raw),
        ('latLngCollection', lat_and_long)
        ]
    return Map_Quest_Base_Elevation_URL + '/profile?' + urllib.parse.urlencode(query_parameters)
         

def obtain_result(url: str) -> 'json':
    '''This function reads a URL and returns it as a json object
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    finally:
        if response is not None:
            response.close()


def display_error(result: 'json') -> None:
    '''Displays an error if the user does not enter a valid location or MapQuest cannot input such
    a location or locations
    '''
    if result['info']['messages'] == ['We are unable to route with the given locations.']:
        print('We are unable to route with the given locations.')
    else:
        pass
