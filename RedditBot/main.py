import logging
from master import Master
from worker import Worker

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info("Instantiating worker")

Master.createWorker(10, 5,'all', 'hot')


