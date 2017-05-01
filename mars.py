import requests
import sys

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def get_mars_photo_url(sol, api_key='DEMO_KEY'):
    params = {'sol': sol, 'api_key': api_key}
    response = requests.get(rover_url, params)
    response_dictionary = response.json()
    photos = response_dictionary['photos']

    for i in photos:
        print i['img_src']

def main():
    if sys.argv < 1:
        print('To few arguments, please specify a SOL Day')

    sol_num = sys.argv[1]
    get_mars_photo_url(sol_num)

if __name__ == '__main__':
    main()