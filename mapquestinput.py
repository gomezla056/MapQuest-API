def number_of_locations() -> list:
    '''This function defines how many locations the user wishes to use
    and has the user input the addresses equal to how many locations the
    user defined'''
    locations = int(input("Enter number of locations to travel to (2 - 3): "))
    while locations < 2 or locations > 3:
        locations = int(input("Error: Please put a number 2 or 3.\nLocations: "))
    addresses = []
    for local in range(locations):
        local = input("Address of Location " + str(local + 1) + ": ")
        addresses.append(local)
    return addresses


def number_of_outputs() -> list:
    '''This function defines how many outputs the user wishes to use (up to five)
    and selects which outputs to print out in the user's specified order'''
    print("\nOptional arguments to use: STEPS, LATLONG, TOTALTIME, TOTALDISTANCE")
    outputs = int(input("Choose the number of optional arguments to use (0 - 4): "))
    while outputs < 0 or outputs > 4:
        outputs = int(input("Error: Please put a number between 0 and 4.\nOptional arguments: "))
    output_list = []
    for options in range(outputs):
        options = input("Option " + str(options + 1) + ": ").upper()
        output_list.append(options)
    return output_list
