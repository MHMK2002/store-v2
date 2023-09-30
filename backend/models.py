import os

from pymongo import MongoClient


class Model(object):
    def __init__(self):
        self.client = MongoClient(os.environ.get('MONGO_URI'))
        self.db = self.Meta.db or self.__class__.__name__.lower()
        self.collection = self.Meta.collection or self.__class__.__name__.lower()

    def __enter__(self):
        self.db = self.client[self.db]
        self.collection = self.db[self.collection]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def create(self, data):
        return self.collection.insert_one(data)

    def find(self, query):
        return self.collection.find(query)

    def bulk_create(self, data):
        return self.collection.insert_many(data)

    def update(self, query, data):
        return self.collection.update_one(query, {'$set': data})

    def bulk_update(self, query, data):
        return self.collection.update_many(query, {'$set': data})

    def delete(self, query):
        return self.collection.delete_one(query)

    def bulk_delete(self, query):
        return self.collection.delete_many(query)

    class Meta:
        db = None
        collection = None
