from app.dependencies import mongo_client
from app.dependencies import settings

uri = f'{settings.MONGO_CONNECTION}://{settings.MONGO_ROOT_USERNAME}:{settings.MONGO_ROOT_PASSWORD}@{settings.MONGO_HOST}'

if settings.MONGO_CONNECTION != 'mongodb+srv':
    uri += f':{settings.MONGO_PORT}'

client = mongo_client.MongoClient(uri)
client.admin.command('ping')

db = client.get_database(settings.MONGO_DB)
