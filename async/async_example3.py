import asyncio


async def fetch_data():
    print(f"Fetching Data : ...")
    data = {
        "name": "Joe Doe", 
        "first_book": "The Journay Without Destination"
    }
    #  mimic waiting by sleeping 2 secons
    await asyncio.sleep(2) 
    print("Data Fetching Finished !!!")
    return data
async def process_data(data):
    print(f" Processing The data Started !!!")
    await asyncio.sleep(2)
    print("Data Processing Finished !!")
    data["name"] = data["name"].upper()
    data["first_book"] = data["first_book"].upper()
    
    return f"Data After Processing : {data}"


data = asyncio.run(fetch_data())
asyncio.run(process_data(data))


print(data)