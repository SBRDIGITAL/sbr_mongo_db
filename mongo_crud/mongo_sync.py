from pymongo import MongoClient

from .mc_settings import MongoCRUDHelper, Settings


class MongoCRUD:
    """
    ## Класс для выполнения базовых операций CRUD с коллекцией MongoDB.

    Атрибуты:
        client (MongoClient): Экземпляр клиента MongoDB.
        db (Database): Экземпляр базы данных.
        collection (Collection): Экземпляр коллекции, в которой хранятся документы.
    """
    def __init__(self, uri: str = Settings.URI, db_name: str = Settings.DB_NAME):
        """
        ## Инициализирует класс MongoCRUD с подключением к MongoDB.

        Аргументы:
            uri (str): URI для подключения к MongoDB.
            db_name (str): Имя базы данных, с которой будет работать класс.
        """      
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['test_collection']
        self.counter_collection = self.db['counters']

    def create(self, document: dict) -> None:
        """
        ## Создает новый документ в коллекции.

        Аргументы:
            document (dict): Документ, который будет добавлен в коллекцию.
        """
        result = self.collection.insert_one(document)
        print(f'Вставлен документ с id: {result.inserted_id}')

    def read(self,
        query: dict,
        mode: MongoCRUDHelper.QueryModes = 'one',
        max_len: int = None
    ) -> None:
        """
        ## Читает документы из коллекции по заданному запросу.

        Аргументы:
            query (dict): Запрос для поиска документов.
            mode (MongoCRUDHelper.QueryModes, optional): Режим чтения. 
                'one' - вернуть только один документ, 
                'many' - вернуть все документы, соответствующие запросу. 
                По умолчанию 'one'.
            max_len (int, optional): Максимальное кол-во документов для возврата в режиме 'many'. 
                По умолчанию None, что означает возврат всех документов.

        Вывод:
            None: Метод выводит найденные документы в консоль.
        """  
        if mode == 'one':
            document: dict | None = self.collection.find_one(query)
            if document:
                print(f'Найден документ: {document}')
            else:
                print('Документ не найден.')
        elif mode == 'many':
            documents: list[dict] = self.collection.find(query).to_list(length=max_len)
            if documents:
                print(f'Найдено документов: {len(documents)}')
                for doc in documents:
                    print(f'{doc=}')
            else:
                print('Документы не найдены.')

    def update(self, query: dict, update_values: dict) -> None:
        """
        ## Удаляет документ из коллекции по заданному запросу.

        Аргументы:
            query (dict): Запрос для поиска документа, который нужно удалить.
        """      
        result = self.collection.update_one(query, {'$set': update_values})
        print(f'Изменено {result.modified_count} документ(ов).')

    def delete(self, query: dict, mode: MongoCRUDHelper.QueryModes = 'one') -> None:
        """
        ## Удаляет документы из коллекции по заданному запросу.

        Аргументы:
            query (dict): Запрос для поиска документов, которые нужно удалить.
            mode (MongoCRUDHelper.QueryModes, optional): Режим удаления. 
                'one' - удалить только один документ, 
                'many' - удалить все документы, соответствующие запросу. 
                По умолчанию 'one'.

        Вывод:
            None: Метод выводит количество удаленных документов в консоль.
        """
        if mode == 'one':
            result = self.collection.delete_one(query)
        else:
            result = self.collection.delete_many(query)
        print(f'Удалено {result.deleted_count} документ(ов).')



class MCTest:

    @staticmethod
    def start_test():
        """ ## Пример использования CRUD операций """
        mongo_crud = MongoCRUD('mongodb://localhost:27017/', 'test_db')
        
        data = {
            'id': 0,
            'name': 'Alice'
        }
        
        data_2 = {
            'id': 1,
            'name': 'Bob'
        }
        
        # Пример использования CRUD операций
        mongo_crud.delete({'name': 'Alice'}, mode='many')  # Удаление документа
        mongo_crud.delete({'name': 'Bob'})  # Удаление документа
        mongo_crud.create(data)  # Создание документа
        mongo_crud.create(data_2)  # Создание документа
        mongo_crud.read({'name': 'Alice'})  # Чтение документа
        mongo_crud.read({'name': 'Alice'}, mode='many')  # Чтение документа
        mongo_crud.update({'name': 'Alice'}, {'age': 31})  # Обновление документа
        mongo_crud.read({'id': 0})  # Чтение обновленного документа
        mongo_crud.read({'id': 1})  # Чтение обновленного документа
        mongo_crud.delete({'name': 'Alice'})  # Удаление документа
        
        mongo_crud.read({'name': 'Alice'})  # Попытка чтения удаленного документа
        
        mongo_crud.update(
            query={
                '_id': 1,
            },
            update_values={
                'surname': 'coder'
            }
        )


if __name__ == "__main__":
    MCTest.start_test()