import time
import concurrent.futures
import requests

img_urls = [
    'https://cdn.pixabay.com/photo/2014/11/10/13/18/goose-525420_960_720.jpg',
    'https://cdn.pixabay.com/photo/2018/06/27/06/26/goose-3500908_960_720.jpg',
    'https://cdn.pixabay.com/photo/2020/05/12/08/53/fly-5161892_960_720.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")