import mapquestinput
import mapquestapi
import mapquestoutput


if __name__ == '__main__':
    directions = mapquestapi.obtain_result(mapquestapi.direction_route_url(mapquestinput.number_of_locations()))
    mapquestoutput.output(mapquestinput.number_of_outputs(), directions)
