# open links.txt and save each pdf to a folder
# Usage: python save.py

import os
import requests
import shutil

# create a folder to save pdfs
if not os.path.exists('pdfs'):
    os.makedirs('pdfs')

# open links.txt
with open('links.txt', 'r') as f:
    links = f.readlines()

# download each pdf
for link in links:
    link = link.strip()
    # get the two numbers before the word budget for the year
    year = link.split('budget')[0][-2:]
    filename = link.split('/')[-1]
    response = requests.get(link, stream=True)
    with open('pdfs/' + year + '.pdf', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

print('PDFs saved to pdfs folder')