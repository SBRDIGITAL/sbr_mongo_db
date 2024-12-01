from mongo_crud import mc_test
from mongo_crud.async_mongo import AsyncMongoCRUD
from mongo_crud.mongo_sync import MongoCRUD



if __name__ == "__main__":
    mc_test.start_test()
    # mongo_crud = MongoCRUD(uri='your_uri', db_name='your_db_name')
    # amongo_crud = AsyncMongoCRUD(uri='your_uri', db_name='your_db_name')