expand = 0.005;  #comprobar cuanto equivale 0.005 en metros
expand_xy = 0.035;

#given an array (initial_map) composed by array[latitude,longitude,latitude2,longitude2]
# where first coordinates -> latitude and longitude from coast points,
# second coordinates -> latitude and longitude direction to open sea(where the
#route points are going to be created).

# TODO: Rellenar sections
#section 0 = Mallorca
#section 1 = bahia palma

#return array[latitude, longitude, angleToOpenSea, section ,lat2, lon2]
#the point from coast and the direction to open sea to create the route points
def create_map(initial_map,section = 0):
  map = []
  for new_point in initial_map:
      angle = calculate_angle(new_point[0],new_point[1],new_point[2],new_point[3])
      newMapPoint = []
      newMapPoint.append(new_point[0],new_point[1],angle, section)
      map.append(newMapPoint)

  #// TODO: Export map into a File.txt

}


def lat_long_dist_of_two_points(latitudeFrom, longitudeFrom, latitudeTo, longitudeTo):
  pi = pi();
  x = sin(latitudeFrom * pi/180) *
  sin(latitudeTo * pi/180) +
  cos(latitudeFrom * pi/180) *
  cos(latitudeTo * pi/180) *
  cos((longitudeTo * pi/180) - (longitudeFrom * pi/180));
  x = atan((sqrt(1 - pow(x, 2))) / x);
  return abs((1.852 * 60.0 * ((x/pi) * 180)) / 1.609344);


#given 2 cartesian points return the angle between them where 0 represents North.
def calculate_angle(y,x,y2,x2):
  difx =   x2 - x;
  dify =   y2 - y;
  angle = atan2(difx, dify) * 180 /pi();
}

#bigMap -> list[latitude, longitude, angleToOpenSea, section ,lat2, lon2]
def calculate_distance_section(bigMap):
    dicc_distance_sectors = {}
    for point,i in enumerate(bigMap[:-1]): # TODO: revisar ese -1 (deberia ser el penultimo elemento), revisar tambien el enumerate
        if point[4] == bigMap[i+1][4]
            distance = lat_long_dist_of_two_points(point[0], point[1], bigMap[i+1][0], bigMap[i+1][1])
            dicc_distance_sectors[point[4]] += distance # TODO: revisar si esto funciona
    # TODO: guardar dicc_distance_sectors en un archivo
