import pymongo
import logging


class DataHandler:
    def __init__(self, client):
        self.client = client

    @staticmethod
    def initialize_data_handler():
        client = DataHandler(pymongo.MongoClient("mongodb+srv://ClusterAdmin:<clusteradmin12345>@testcluster.0uyyo"
                                                 ".mongodb.net/<TestCluster?retryWrites=true&w=majority"))
        db = client.test
        logging.info(db)
        return client

    def check_if_database_exists(self, database_name):
        db_list = self.client.list_database_names()
        if database_name in db_list:
            logging.info("The database exists.")
            return True
        else:
            return False

    def get_database_list(self):
        self.client.list_database_names()

    def insert_into_table(self, database_name, collection_name, reddit_user):
        mydb = self.client[database_name]
        mycol = mydb[collection_name]
