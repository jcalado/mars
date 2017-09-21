import requests
import sys
import os
import urllib

sol_num = sys.argv[1]
rpath = sys.argv[2]
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
    get_mars_photo_url(sol_num)


if __name__ == '__main__':
    main()