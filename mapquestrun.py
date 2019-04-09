import mapquestinput
import mapquestapi


def output(list_of_outputs: list, result: 'json') -> str:
    '''This function gathers a list of the outputs the user gives and
    identifies which output(s) to display
    '''
    try:
        for item in list_of_outputs:
            if item == 'LATLONG':
                print('LATLONGS')
                _longitude_and_latitude(result)
            if item == 'STEPS':
                print('DIRECTIONS')
                _steps_and_directions(result)
            if item == 'TOTALTIME':
                _total_time(result)
            if item == 'TOTALDISTANCE':
                _total_distance(result)
    except:
        mapquestapi.display_error(result)


def _longitude_and_latitude(result: 'json') -> None:
    '''Displays the longitude and latitude of the locations the user
    has inputted
    '''
    for long_and_lat_results in result['route']['locations']:
        latitude = float(long_and_lat_results['latLng']['lat'])
        longitude = float(long_and_lat_results['latLng']['lng'])
        if latitude > 0:
            lat_direction = 'N'
        else:
            lat_direction = 'S'
        if longitude > 0:
            long_direction = 'E'
        else:
            long_direction = 'W'
        print(str(latitude) + " " + lat_direction + " " + str(longitude) + " " + long_direction)
    print('\n')


def _steps_and_directions(result: 'json') -> None:
    '''Displays the directions to the desire location in a
    step by step format
    '''
    for steps in result['route']['legs']:
        for direction in steps['maneuvers']:
            print(direction['narrative'])
    print('\n')


def _total_time(result: 'json') -> None:
    '''Displays the total amount of time to reach the destination
    '''
    total = int(result['route']['time'])
    print('TOTAL TIME: ' + str(total/60) + ' minutes')
    print('\n')


def _total_distance(result: 'json') -> None:
    '''Displays the total distance the user has to travel to the
    desired location
    '''
    length_of_route = str(float(result['route']['distance']))
    print('TOTAL DISTANCE: ' + length_of_route + ' miles')
    print('\n')


if __name__ == '__main__':
    directions = mapquestapi.obtain_result(mapquestapi.direction_route_url(mapquestinput.number_of_locations()))
    output(mapquestinput.number_of_outputs(), directions)
