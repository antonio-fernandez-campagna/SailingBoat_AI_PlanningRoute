diference_distance_section = 50

def create_route():
    pass

#current_point -> index on current section
#current_section -> index
# sections --> list[] of sections

def expand_route(current_point_index, current_section_index, sections, sentido):
    total_group_points = []

    map = []## TODO: importar mapa de la seccion actual
    for i in range(0,depth_algorithm): # TODO: revisa
        if sentido = 0:
            current_point_index += 1
        else:
            current_point_index -= 1
        if current_point_index == 0 or current_point_index == len(current_section_index):
                current_section_index = sections.indexOf(current_section_index) + 1
                map = []## TODO: importar mapa de la seccion actual

        new_points_list = []
        group_points = create_points(map[current_point_index])
        total_group_points.append(group_points)

    return total_group_points

def calculate_route(weather_map):
    for group in weather_map:
        for point in group:
            

#group_points -> list of list containing latitude and longitude
# TODO:
def API_get_weather(group_points):
    pass


# point --> list[y latitde, x longitude, angleToOpenSea, section, latitude2,longitude2]
# (item from map)
def create_points(point, maxPoints = 5, increment = 0.01):
    groupOfPoints = []

    if point[4] is not empty():
        dist = lat_long_dist_of_two_points(point[0], point[1], point[4], point[5])
        distance_in_coordinates = dist * 0.01 / 0.69 #conversion 0.01 coordinate = 0.69milles
        maxPoints = increment / distance_in_coordinates


    for i in enumerate(maxPoints):
        newLat = newLat + sin(point[2]) * increment
        newLong = newLong + cos(point[2]) * increment
        groupOfPoints.append(lat,long)

    return groupOfPoints


#start -> array[latitude,longitude]
#destination -> array[latitude, longitude]
#returns the index closest points of my map given start and destination from the user
def find_start_and_destination(BigMap,start,destination):
    closest_point_start = 0
    closest_point_destination = 0
    #calculate error from user given point to first element of array
    previous_total_error_start = abs(BigMap[0][0] - start[0]) + abs(BigMap[0][1] - start[1])
    previous_total_error_destination =  abs(BigMap[0][0] - destination[0]) + abs(BigMap[0][1] - destination[1])

    i = 1
    for point in BigMap:
        lat_distance = abs(point[0] - start[0])
        lon_distance = abs(point[1] - start[1])

        #start point
        actual_total_error_start = abs(point[0] - start[0]) + abs(point[1] - start[1])

        #destination point
        actual_total_error_destination =  abs(point[0] - destination[0]) + abs(point[1] - destination[1])

        if (actual_total_error_start > previous_total_error_start):
          closest_point_start = i

        if ($actual_total_error_destination > previous_total_error_destination) :
          closest_point_destination = i

        i+=1


    return closest_point_start, closest_point_destination

# TODO: indicar rutas directas si se va de punta a punta de la isla
#bigMap --> array[y latitde, x longitude, angleToOpenSea, section, latitude2,longitude2]
#start -> index of start position in array list
#destination -> index of destination position in array list
def calculate_sections(bigMap,start,destination):

    total_distance_left_right = 0
    total_distance_right_left = 0

    sections = start

    index1 = start
    index2 = destination

    if index1 > inde2:
        index1 = destination
        index2 = start

    sections_left_right = []
    sections right_left = []
    if index1 != index2:
        if index1 < index2:
            for i in range(index1,index2): # TODO: revisar si la i = start o empieza en 0
                sections_left_right.append(i)
        else:
            for i in range(0, index1):
                sections_right_left.append(i)
            for i in range(inde2:)
                sections_left_right.append(i)

        sections = calculate_sectors(sections_left_right, sections_right_left)
        if sections is not False:
            if index1 != start:
                sentido = 1  #means sense of array direction is right to left
                sections.reverse() # TODO: revisar

    return sections, sentido

#returns best sections for the route due on the distance,
#if returns false means there is no best route
def calculate_sectors(sections_left_right, sections_right_left):
    file = {} #{1: 10, 2: 5, etc} # TODO: read file from distance
    distance_left_right = 0
    distance_right_left = 0
    for section in sections_left_right:
        distance_left_right += file[section]
    for section in sections_right_left:
        distance_right_left += file[section]

    if abs(distance_left_right - distance_right_left) > diference_distance_section:
        sections = min_value(distance_left_right,distance_right_left) # TODO: revisar esta funcion si existe
    else:
        sections = false #means it should calculate both routes

    return sections


# TODO: indicar atajos
def getAtajos(arg):
    ## TODO: leer archivo en formato lista[[1,3,5],[7,9]]] | ie. atajos entre section 2, 3 y 5 y otro entre7, 9
    list_atajos = []
    for


#return distance in miles between 2 points
def lat_long_dist_of_two_points(latitudeFrom, longitudeFrom, latitudeTo, longitudeTo):
  pi = pi();
  x = sin(latitudeFrom * pi/180) *
  sin(latitudeTo * pi/180) +
  cos(latitudeFrom * pi/180) *
  cos(latitudeTo * pi/180) *
  cos((longitudeTo * pi/180) - (longitudeFrom * pi/180));
  x = atan((sqrt(1 - pow(x, 2))) / x);
  return abs((1.852 * 60.0 * ((x/pi) * 180)) / 1.609344); #return in miles

#given 2 cartesian points return the angle between them where 0 represents North.
def calculate_angle(y,x,y2,x2):
  difx =   x2 - x;
  dify =   y2 - y;
  angle = atan2(difx, dify) * 180 /pi();
}
