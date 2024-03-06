from timer import timer
import requests
from concurrent.futures import ThreadPoolExecutor

URL = 'https://httpbin.org/uuid'

def fetch_uuid(Session, url):
  with Session .get(url) as response:
    print(response.json()['uuid'])

@timer(1,5)
def main():
  with ThreadPoolExecutor(max_workers=100) as executor:
    with requests.Session() as session:
      executor.map(fetch_uuid, [session] * 100, [URL] * 100)
      executor.shutdown(wait=True)