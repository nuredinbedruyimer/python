import asyncio


async def fetch_page(url):
    print(f"Fetch Page Started : ...")
    await asyncio.sleep((2))
    print(f"Page Fetched(Finished)")
    
    return url+"Fetched"
async def crawl_page(url):
    await fetch_page(url)
    crawled_url = url.upper()
    print(f"Crawled Page : ", crawled_url)
    return crawled_url

urls = ["https://test/get-me", "https://test/get-them", "https://test/get-us", "https://test/get-none"]



async def main():
    tasks = [asyncio.create_task(crawl_page(url))for url in urls]

    await asyncio.gather(*tasks)


asyncio.run(main())



