import time
import concurrent.futures
import requests
import threading
import multiprocessing

img_urls = [
    'https://cdn.pixabay.com/photo/2014/11/10/13/18/goose-525420_960_720.jpg'
]

def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    #end = time.perf_counter()
    #print(f"Tasks ended in {round(end - start, 2)} second(s)")

T = []
for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))

for i in range(len(T)):
    T[i].start()

for i in range(len(T)):
    T[i].join()

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


#if __name__ == '__main__':
