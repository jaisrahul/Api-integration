import requests,json
from requests.exceptions import HTTPError
from db_connections import Db_Connection
from curd_operations import Curd_Operation


header_dic = {"app-id": "629e2b7fd3720c228ee845cc"}

def fetch_user_data():

    url = "https://dummyapi.io/data/v1/user?page=1&limit=5"
    try:
        response = requests.get(url,headers=header_dic)
        response.raise_for_status()  # If the response was successful, no Exception will be raised
        data = response.json()["data"] # reading json data
        
        columns = [key for key in data[0]] # fetch cloumns for db from data
        rows=[[ dic[key] for key in dic] for dic in data] # fetch rows for db from data
        
        schema_name = "dummyapi"
        table_name = "user"
        file_name = "C://Users//AMIT KUMAR PATHAK//OneDrive//Desktop//TailNode//part_A//create_user_table.pgsql" # change location accordings to file location
        
        db = Curd_Operation(schema_name, table_name)
        db.create_table(file_name)
        db.insert_many(columns, rows)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}') 

    else:
        print('Success!')

def fetch_user_postdata():
    
    schema_name = "dummyapi"
    table_name = "user"
    table2 = "post"
    primarykey="id"
    file_name = "C://Users//AMIT KUMAR PATHAK//OneDrive//Desktop//TailNode//part_A//create_post_table.pgsql" # change location accordings to file location
    
    db = Curd_Operation(schema_name, table_name,primarykey) 
    idlist = db.select(columns=["id"])          #fetching user_id
    
    try:
        for ids in idlist:
            user_id = ids[0]
        
            url = f"https://dummyapi.io/data/v1/user/{user_id}/post?limit=5"
            response = requests.get(url,headers=header_dic)
            response.raise_for_status()  # If the response was successful, no Exception will be raised
            data = response.json()["data"] # reading json data
    
            columns = [key for key in data[0]] # fetch cloumns for db from dict
            rows=[[ dic[key] if key!="owner" else dic[key]["id"] for key in dic] for dic in data] # fetch rows for db from dict
        
            
            db = Curd_Operation(schema_name, table2)
            db.create_table(file_name)
            db.insert_many(columns, rows)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}') 

    else:
        print('Success!')

