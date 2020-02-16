import requests
import os
import urllib.request
import argparse

parser = argparse.ArgumentParser(description='Download NASA Curiosity Photos')
parser.add_argument('-d', '--dest', help="Download Directory", required=True)
parser.add_argument('-s', '--sol', help="Mars SOL Day(s)", required=True)
args = parser.parse_args()

rpath = args.dest
asol = args.sol.split("-")

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def solrange(start, end):
    if start > end:
        return range(end, start + 1)
    else:
        return range(start, end + 1)


def get_mars_photo_url(sol, api_key='DEMO_KEY'):
    params = {'sol': sol, 'api_key': api_key}
    response = requests.get(rover_url, params)
    response_dictionary = response.json()
    photos = response_dictionary['photos']

    dpath = r'%s/%s' % (rpath, sol)
    if not os.path.exists(dpath):
        os.makedirs(dpath)

    for i in photos:
        url = i['img_src']
        image = url.rsplit('/', 1)[1]
        directory = os.path.join(dpath, image)
        urllib.request.urlretrieve(url, directory)


def main():
    global asol
    if len(asol) == 1:
        get_mars_photo_url(sol=asol[0])
    else:
        asol = [int(i) for i in asol]
        for i in solrange(asol[0], asol[1]):
            get_mars_photo_url(sol=i)


if __name__ == '__main__':
    main()