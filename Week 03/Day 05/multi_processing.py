import requests
from timer import timer 
from multiprocessing.pool import Pool

URL = 'https://httpbin.org/uuid'

def fetch_uuid(Session, url):
  with Session .get(url) as response:
    print(response.json()['uuid'])

@timer(1,1)
def main():
  with Pool() as pool:
    with requests.Session() as session:
      pool.starmap(fetch_uuid,[(session,URL) for _ in range(100)])