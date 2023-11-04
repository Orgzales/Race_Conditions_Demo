import requests
import threading
import time

name = 'Orion'
#url = 'http://52.91.76.219:5000/test'
#url = 'http://52.91.76.219:5000/test_fast'
url = 'http://52.91.76.219:5000/test_fixed'
name_data = {'username': name}

def send_request():
    global name_data
    global name
    for x in range(100):
        time.sleep(0.5)
        name = 'Orion' + str(x)
        name_data = {'username': name}
        response = requests.post(url, data=name_data)
        print(response.text)

threads = [threading.Thread(target=send_request) for x in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()