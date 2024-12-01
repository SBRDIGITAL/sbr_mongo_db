## Методичка по запуску и настройке MongoDB с использованием Docker

### Шаг 1: Установка Docker и Docker Compose

1. **Скачайте и установите Docker Desktop**:
   - Перейдите на [официальный сайт Docker](https://www.docker.com/products/docker-desktop) и скачайте установщик для Windows.
   - Установите Docker Desktop, следуя инструкциям на экране.

2. **Проверьте установку**:
   - Откройте командную строку (CMD) или PowerShell и выполните команды:
     ```bash
     docker --version
     docker-compose --version
     ```

### Шаг 2: Создание проекта

1. **Создайте директорию для проекта**:
   - Создайте новую папку на вашем компьютере, например `mongo_db`.

2. **Перейдите в созданную папку**:
   ```bash
   cd path\to\mongo_db
   ```

3. **Создайте директории для хранения данных**:
   - Создайте директории для хранения данных MongoDB. Это может быть сделано вручную или с помощью командной строки:
   ```bash
   mkdir -p data/db/mongo1
   mkdir -p data/db/mongo2
   mkdir -p data/db/mongo3
   ```

### Шаг 3: Создание файла `docker-compose.yml`

1. **Создайте файл `docker-compose.yml`**:
   - В корне проекта создайте файл с именем `docker-compose.yml` и добавьте следующий код:

   ```yaml
    services:
        mongo1:
            image: mongo:latest
            container_name: mongo1
            ports:
            - "27017:27017"
            volumes:
            - mongo1-data:/data/db
            networks:
            - mongo-cluster
            command: ["mongod", "--replSet", "rs0"]

        mongo2:
            image: mongo:latest
            container_name: mongo2
            ports:
            - "27018:27017"
            volumes:
            - mongo2-data:/data/db
            networks:
            - mongo-cluster
            command: ["mongod", "--replSet", "rs0"]

        mongo3:
            image: mongo:latest
            container_name: mongo3
            ports:
            - "27019:27017"
            volumes:
            - mongo3-data:/data/db
            networks:
            - mongo-cluster
            command: ["mongod", "--replSet", "rs0"]

    volumes:
        mongo1-data:
        mongo2-data:
        mongo3-data:

    networks:
        mongo-cluster:
   ```

### Шаг 4: Запуск контейнеров

1. **Запустите Docker Compose**:
   - В командной строке выполните следующую команду для запуска контейров:
   ```bash
   docker-compose up -d
   ```
   или
   ```bash
   docker-compose up --build --force-recreate
   ```

2. **Проверьте, что контейнеры запущены**:
   - Выполните команду:
   ```bash
   docker ps
   ```
   или
   ```bash
   docker-compose ps
   ```

### Шаг 5: Подключение к MongoDB

1. **Подключитесь к первому экземпляру MongoDB**:
   - Выполните команду:
   ```bash
   docker exec -it mongo1 mongosh
   ```

### Шаг 6: Инициализация репликационного набора

1. **Инициализируйте репликационный набор**:
   - Введите следующую команду в `mongosh`:
   ```javascript
   rs.initiate({
     _id: "rs0",
     members: [
       { _id: 0, host: "mongo1:27017" },
       { _id: 1, host: "mongo2:27017" },
       { _id: 2, host: "mongo3:27017" }
     ]
   });
   ```

2. **Проверьте статус репликационного набора**:
   - Введите команду:
   ```javascript
   rs.status();
   ```

### Шаг 7: Использование MongoDB

1. **Создайте и активируйте виртуальное окружение**
2. **Установите зависимости из requirements.txt**
3. **Запустите файл `main.py`**
4. **В консоли должно появиться что-то похожее на:**
```bash
    Синхронно:
    Удалено 0 документ(ов).
    Удалено 1 документ(ов).
    Вставлен документ с id: 674c751123641122fd84ae5a
    Вставлен документ с id: 674c751123641122fd84ae5b
    Найден документ: {'_id': ObjectId('674c751123641122fd84ae5a'), 'id': 0, 'name': 'Alice'}
    Найдено документов: 1
    doc={'_id': ObjectId('674c751123641122fd84ae5a'), 'id': 0, 'name': 'Alice'}
    Изменено 1 документ(ов).
    Найден документ: {'_id': ObjectId('674c751123641122fd84ae5a'), 'id': 0, 'name': 'Alice', 'age': 31}
    Найден документ: {'_id': ObjectId('674c751123641122fd84ae5b'), 'id': 1, 'name': 'Bob'}
    Удалено 1 документ(ов).
    Документ не найден.
    Изменено 0 документ(ов).

    Асинхронно:
    Удалено 0 документ(ов).
    Удалено 1 документ(ов).
    Вставлен документ с id: 674c751123641122fd84ae5d
    Вставлен документ с id: 674c751123641122fd84ae5e
    Найден документ: {'_id': ObjectId('674c751123641122fd84ae5d'), 'id': 0, 'name': 'Alice'}
    Найдено документов: 1
    doc={'_id': ObjectId('674c751123641122fd84ae5d'), 'id': 0, 'name': 'Alice'}
    Изменено 1 документ(ов).
    Найден документ: {'_id': ObjectId('674c751123641122fd84ae5d'), 'id': 0, 'name': 'Alice', 'age': 31}
    Найден документ: {'_id': ObjectId('674c751123641122fd84ae5e'), 'id': 1, 'name': 'Bob'}
    Удалено 1 документ(ов).
    Документ не найден.
    Изменено 0 документ(ов).
```