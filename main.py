from db_connections import Db_Connection
from curd_operations import Curd_Operation
from dummyapi import fetch_user_data,fetch_user_postdata

""" Before running create database and schema according to create_db.pgsql and create_schema.pgsql respectively"""
if __name__ == "__main__":
    fetch_user_data()
    fetch_user_postdata()



