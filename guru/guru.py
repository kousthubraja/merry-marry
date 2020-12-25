import requests
import shutil
from bs4 import BeautifulSoup

BASE_URL = 'https://gurudevamatrimony.com'
PHOTO_DIR = 'photos/'

url = 'https://gurudevamatrimony.com/search/page/1/?from=18&to=26&hfrom=122&hto=210&gender=f&mstatus=u&jathakam=0&wphoto=wpho&order=-1'
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, allow_redirects=False, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

cards = soup.find_all('div', {'data-animate': 'rollIn'})
for card in cards:
    header = card.find('div', {'class': 'prof-header'})
    if header is None:
        continue
    name = header.find('h2').text
    age = header.find('span').text
    profile_id = card.find('a', {'class': 'id-cx'}).text

    link = soup.find('a', {'id': 'img-view'})
    img_url = link.find('img')['src']
    img_url = BASE_URL + img_url
    response = requests.get(img_url)

    file_name = age + '_' + name + '_' + profile_id + '.jpg'

    with open(PHOTO_DIR + file_name, 'wb') as f:
        f.write(response.content)

    del response
    print(age, name, profile_id, img_url)