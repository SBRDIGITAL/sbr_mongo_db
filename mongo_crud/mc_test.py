from asyncio import run

from mongo_crud.async_mongo import AsyncMCTest
from mongo_crud.mongo_sync import MCTest


def start_test():
    print('\nСинхронно:')
    MCTest.start_test()
    print('\nАсинхронно:')
    run(AsyncMCTest.start_test())
    
if __name__ == "__main__":
    start_test()