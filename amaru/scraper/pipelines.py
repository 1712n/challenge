# Pipelines docs:
# http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from dataclasses import asdict
from scrapy.utils.project import get_project_settings


settings = get_project_settings()


class MongoDBPipeline:
    def __init__(self):
        conn = pymongo.MongoClient(
            settings.get('MONGO_URI')
        )
        db = conn[settings.get('MONGO_DB_NAME')]
        self.collection = db[settings['MONGO_COLLECTION_NAME']]

    # TODO: Start from last saved value, paginated querying, improve logging
    def process_item(self, item, spider):
        self.collection.insert_one(asdict(item))
