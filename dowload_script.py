import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.cs.cmu.edu/afs/cs/academic/class/15213-f20/www/lectures/'
folder_path = '/Users/huapengzhou/CSAPP/slides'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    file_link = link.get('href')
    if file_link.endswith('.pptx'):
        download_url = url + file_link
        file_response = requests.get(download_url)
        with open(os.path.join(folder_path, file_link), 'wb') as file:
            file.write(file_response.content)
