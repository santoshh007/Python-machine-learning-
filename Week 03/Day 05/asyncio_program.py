import asyncio
import requests
import aiohttp
from timer import timer
from concurrent.futures import ThreadPoolExecutor

URL = 'https://httpbin.org/uuid'

async def fetch_uuid(Session, url):
  async with Session.get(url) as response:
    print(response.json()['uuid'])


async def func():
  async with aiohttp.ClientSession()as session:
    tasks= [fetch_uuid(session,URL) for _in range(100)]
    await asyncio.gather(*tasks)

@timer(1,1)
def main():
  asyncio.run(func())