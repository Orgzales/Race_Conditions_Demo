import requests
import threading

name = 'Orion'
#url = 'http://52.91.76.219:5000/test'
#url = 'http://52.91.76.219:5000/test_fast'
url = 'http://52.91.76.219:5000/test_fixed'
name_data = {'username': name}


def send_request():
    for x in range(100):
        response = requests.post(url, data=name_data)
        print(response.text)

threads = [threading.Thread(target=send_request) for x in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()