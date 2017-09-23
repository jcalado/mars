import requests
import os
import urllib
import argparse


parser = argparse.ArgumentParser(description='Download NASA Curiosity Photos')
parser.add_argument('-d', '--dest', help= "Download Directory", required=True)
parser.add_argument('-s', '--sol', help= "Mars SOL Day(s)", required=True)
args = parser.parse_args()


rpath = args.dest
asol = args.sol.split("-")


rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def get_mars_photo_url(sol, api_key='DEMO_KEY'):
    params = {'sol': sol, 'api_key': api_key}
    response = requests.get(rover_url, params)
    response_dictionary = response.json()
    photos = response_dictionary['photos']

    dpath = r'%s/%s' %(rpath, sol_num)
    if not os.path.exists(dpath):
        os.makedirs(dpath)

    for i in photos:
        url = i['img_src']
        image = url.rsplit('/', 1)[1]
        directory = os.path.join(dpath, image)
        urllib.urlretrieve(url, directory)


def main():

    global asol, sol_num
    while ( asol[0] <= asol[1] ):
        asol[0] = int(asol[0])
        asol[1] = int(asol[1])
        sol_num = asol[0]
        get_mars_photo_url(sol_num)
        asol[0] += 1



if __name__ == '__main__':
    main()