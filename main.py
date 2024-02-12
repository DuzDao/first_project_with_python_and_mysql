import pandas as pd

from utils import get_config
from mysql_queries.create_queries import ACCOUNTSCOUNTRY_TABLE_CREATE, ACCOUNTS_DATA_TABLE_CREATE, ACCOUNTSERIES_DATA_TABLE_CREATE
from mysql_queries.insert_queries import INSERT_ACCOUNTSCOUNTRY, INSERT_ACCOUNTSDATA, INSERT_ACCOUNTSERIES
from mysql_module.connection import MySQLConnector


def main(config):
    connector = MySQLConnector(config=config)
    connector.create_database()
    connector.create_table(queries=[ACCOUNTSCOUNTRY_TABLE_CREATE, ACCOUNTS_DATA_TABLE_CREATE, ACCOUNTSERIES_DATA_TABLE_CREATE])

    #insert data
    df_acc_country = pd.read_csv(config["data"]["path"] + "/account_country.csv")
    df_acc_data = pd.read_csv(config["data"]["path"] + "/account_data.csv")
    df_acc_series = pd.read_csv(config["data"]["path"] + "/account_series.csv")

    connector.insert_data(
        queries=[INSERT_ACCOUNTSCOUNTRY, INSERT_ACCOUNTSERIES, INSERT_ACCOUNTSDATA], 
        dfs=[df_acc_country, df_acc_series, df_acc_data]
    )

if __name__ == "__main__":
    config = get_config("configs/config.yaml")
    main(config)