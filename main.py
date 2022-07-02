import requests
from pathlib import Path

file = "img.jpg"

link = requests.post(url=r'https://file.io', files={'file': Path(file).read_bytes()})
a = link.json()
print(a["link"])