ACCOUNTSCOUNTRY_TABLE_CREATE = """
                        create table if not exists AccountsCountry (
                            country_code varchar(100),
                            short_name varchar(100),
                            table_name varchar(100),
                            long_name varchar(100),
                            currency_unit varchar(100),
                            primary key(country_code)
                        );
"""

ACCOUNTS_DATA_TABLE_CREATE = """
                        create table if not exists AccountsData (
                            country_name varchar(100),
                            country_code varchar(100),
                            indicator_name varchar(100),
                            indicator_code varchar(100),
                            year_1995 float,
                            year_2000 float,
                            year_2005 float,
                            year_2010 float,
                            year_2014 float
                        );
"""

ACCOUNTSERIES_DATA_TABLE_CREATE = """
                        create table if not exists AccountSeries (
                            series_code varchar(100),
                            topic varchar(100),
                            indicator_name varchar(100),
                            short_definition varchar(100)
                        );
"""