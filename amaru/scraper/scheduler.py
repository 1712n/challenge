import os
import time
import logging
import schedule
from pygelf import GelfUdpHandler


def run_graylog():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.addHandler(GelfUdpHandler(host='graylog', port=12201))


if __name__ == '__main__':
    run_graylog()
    logging.info('Scheduler initialised')
    os.system('scrapy crawl slowmist-spider')
    logging.info('Scraped initial data')
    # TODO: set this magic number in conf file
    schedule.every(60).minutes.do(lambda: os.system('scrapy crawl slowmist-spider'))
    logging.info('Next job is set to run at: ' + str(schedule.next_run()))


while True:
    schedule.run_pending()
    time.sleep(1)



