import pymongo
import logging
import datetime
import json

class DataHandler:
    def __init__(self, client):
        self.client = client
        self.db_string = "reddit_data"
        self.reddit_users_col_string = "reddit_users"
        self.reddit_comment_history_string = "reddit_comment_history"
        self.db = self.client[self.db_string]
        self.reddit_users_col = self.db[self.reddit_users_col_string]
        self.reddit_comment_history = self.db[self.reddit_comment_history_string]

    @staticmethod
    def initialize_data_handler():
        client = DataHandler(
            pymongo.MongoClient("mongodb+srv://ClusterAdmin:clusteradmin12345@testcluster.0uyyo.mongodb.net"
                                "/reddit_data?retryWrites=true&w=majority"))

        logging.info(client)
        return client

    def get_reddit_user_pk(self, user_name):
        document = self.reddit_users_col.find_one({'user_name': user_name}, {'_id': 1})
        logging.info(document)
        return

    def user_exists(self, reddit_user):
        if self.reddit_users_col.count_documents({'user_name': reddit_user}, limit=1) != 0:
            return True
        else:
            return False

    # def comment_history_exists(self, reddit_user):
    #    if self.reddit_users_col.count_documents({'user_name': reddit_user}, limit=1) != 0

    def check_if_database_exists(self, database_name):
        db_list = self.client.list_database_names()
        if database_name in db_list:
            logging.info("The database exists.")
            return True
        else:
            return False

    def get_database_list(self):
        self.client.list_database_names()

    def insert_into_user_table(self, database_name, collection_name, reddit_user):
        x = datetime.datetime.now()
        data = {"user_name": reddit_user, "user_fully_scanned": 'N', "creation_date": x, "last_update_date": x}
        x = self.reddit_users_col.insert(data)

    def insert_into_comment_history_table(self, submission):
        self.get_reddit_user_pk(submission.author)
        x = datetime.datetime.now()
        # data = {"reddit_user_pk": , "subreddit":, "content":, "date_posted":, "creation_date":}
        # x = self.reddit_comment_history.insert(data)
