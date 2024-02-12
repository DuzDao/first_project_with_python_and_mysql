import mysql.connector
from tqdm import tqdm

class MySQLConnector():
    def __init__(self, config):
        self.host = config["mysql_info"]["host"]
        self.user = config["mysql_info"]["user"]
        self.password = config["mysql_info"]["password"]
        self.any_database = config["mysql_info"]["any_database"] #name of any exist database
        self.database = config["mysql_info"]["database"]
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.any_database
        ) # get connection
        self.cur = self.conn.cursor() # get the cursor
    
    def create_database(self):
        self.cur.execute("DROP DATABASE IF EXISTS {}".format(self.database))
        self.cur.execute("CREATE DATABASE {}".format(self.database))
        self.conn.close()
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        ) # get connection
        self.cur = self.conn.cursor()

    def create_table(self, queries: list):
        for query in queries:
            self.cur.execute(query)
        self.conn.commit()
        print("Table Created Done!")
    
    def insert_data(self, queries:list, dfs: list):
        for i in tqdm(range(len(dfs)), desc="Inserting..."):
            for _, row in dfs[i].iterrows():
                try:
                    self.cur.execute(queries[i]%(tuple(row)))
                except:
                    continue
        self.conn.commit()
        print("Data Inserted Done!")
            

    