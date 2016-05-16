import math
from googlemaps import *
import urllib
import xml.etree.ElementTree as ET
def deg2rad(deg):
  return deg * (3.14159265358979323846264338327950/180)
def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2): 
    R = int(6371)
    dLat = float(deg2rad(lat2-lat1))
    dLon = float(deg2rad(lon2-lon1)) 
    a = float(math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2))
    c = float(2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))
    d = float(R * c)
    return d
serviceurl='http://maps.googleapis.com/maps/api/geocode/xml?'
print "Enter 1 to find the Latitude and Longitude of a particular Place"
print "Enter 2 to find the distance between 2 places"
ch=int(raw_input())
if ch==1:
    print "Press Enter to exit"
    while True:
        address=raw_input('Enter Location: ')
        if len(address)<1:
            break
        url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
        print "Retrieving: ", url
        uh=urllib.urlopen(url)
        data=uh.read()
        tree=ET.fromstring(data)
        r=tree.findall('result')
        lat=r[0].find('geometry').find('location').find('lat').text
        lon=r[0].find('geometry').find('location').find('lng').text
        loc=r[0].find('formatted_address').text
        print 'Latitude', lat, 'Longitude', lon
        print 'location', loc
if ch==2:
    print "Press Enter to exit"
    while True:
       address1=raw_input("Enter address 1:") 
       address2=raw_input("Enter address 2:")
       url1=serviceurl+urllib.urlencode({'sensor':'false', 'address': address1})
       url2=serviceurl+urllib.urlencode({'sensor':'false', 'address': address2})
       uh1=urllib.urlopen(url1).read()
       uh2=urllib.urlopen(url2).read()
       tree1=ET.fromstring(uh1)
       tree2=ET.fromstring(uh2)
       r1=tree1.findall('result')
       r2=tree2.findall('result')
       lat1=r1[0].find('geometry').find('location').find('lat').text
       lon1=r1[0].find('geometry').find('location').find('lng').text
       lat2=r2[0].find('geometry').find('location').find('lat').text
       lon2=r2[0].find('geometry').find('location').find('lng').text
       print lat1, lon1
       print lat2, lon2
       d=getDistanceFromLatLonInKm(float(lat1),float(lon1),float(lat2),float(lon2))
       print d

       