import asyncio
import random

async def fetch_data(url):
    delay = random.randint(1, 4)
    print(f"Fetching Data From {url} Take {delay} Seconds")
    await asyncio.sleep(delay)
    
    return f"Content From The Endpoint {url}"

async def main():
    urls = ["https://example1.exp", "https://example2.exp", "https://example3.exp"]
    
    results = await asyncio.gather( *(fetch_data(url) for url in urls))
    for result in results:
        print(result)
    
    
asyncio.run(main())
    
    
    