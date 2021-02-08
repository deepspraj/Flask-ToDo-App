import pandas as pd
import geocoder


def locationFinder():
    myloc = geocoder.ip('me')
    
    gb = pd.read_csv('C:/Users/91837/Downloads/IN.txt', sep = '\t', header = None, quoting = 3, names = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation', 'dem', 'timezone', 'modification_date'])
    i = 0

    while True:
        if abs(gb.latitude[i]-myloc.latlng[0]) <= 0.01:
            if abs(gb.longitude[i]-myloc.latlng[1]) <= 0.01:
                return (f'{gb.name[i]}, {gb.country_code[i]}')    
        i += 1
