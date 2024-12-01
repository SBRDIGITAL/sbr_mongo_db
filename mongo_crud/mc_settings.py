from typing import Literal


class MongoCRUDHelper:
    QueryModes = Literal['one', 'many']
    
class Settings:
    URI = 'mongodb://localhost:27017/'
    DB_NAME = 'test_db'