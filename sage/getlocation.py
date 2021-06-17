import requests



#linkfor ip   'https://get.geojs.io/v1/ip.json
import socket



def getloc():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)

    r=requests.get('https://get.geojs.io/')

    iprequest=requests.get('https://get.geojs.io/v1/ip.json')
    ipadd=iprequest.json()['ip']
    print(ipadd,type(ipadd),type(IPAddr))

    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
    geo_req=requests.get(url)
    geo_data=geo_req.json()
    print(geo_data)

    print(geo_data['city'], geo_data['region'], geo_data['country'])
    print(geo_data['latitude'],geo_data['longitude'])



    return geo_data['latitude'],geo_data['longitude']
