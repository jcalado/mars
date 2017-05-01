import requests

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def get_mars_photo_url(sol, api_key='DEMO_KEY'):
    params = {'sol': sol, 'api_key': api_key}
    response = requests.get(rover_url, params)
    response_dictionary = response.json()
    photos = response_dictionary['photos']

    for i in photos:
        print i['img_src']

photo_url = get_mars_photo_url(sol=1580)
print photo_url