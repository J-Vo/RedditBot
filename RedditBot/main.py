import logging
from master import Master
from worker import Worker
from dataHandler import DataHandler

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info("Instantiating worker")

client = DataHandler.initializeDataHandler()



