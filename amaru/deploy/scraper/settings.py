#  Conf. docs:
#  http://doc.scrapy.org/en/latest/topics/settings.html

BOT_NAME = 'scamscraper'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'pipelines.MongoDBPipeline': 100}

# --------------------------------MONGO-----------------------------------------#
MONGO_URI = "mongodb://root:rc7aFsJj64g@scamsdb:27017/?authSource=admin"

MONGO_DB_NAME = "admin"
MONGO_COLLECTION_NAME = "hacks"
