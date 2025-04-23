import asyncio

async def tasks(task_name, delay):
    print(f"{task_name} Started")
    #  sleep this function call for 2 second intentionaly before it finishs its task
    await asyncio.sleep(delay)
    print(f"{task_name} Finished")

async def main():
    await asyncio.gather(
        tasks("Call API 1", 2), 
                tasks("Call API 2", 3)
,        tasks("Call API 3", 1)

    )
    
asyncio.run(main())
    