import oracledb
#from sqlalchemy import create_engine
#from sqlalchemy.dialects import oracle
from configparser import ConfigParser
#from sqlalchemy import Connection

configur = ConfigParser()
configur.read("././configs/config.ini") #using Absolute Path because of relative path issue

def oracle_get_conn() -> oracledb.connect:
    try:
        conn = oracledb.connect(user= configur.get('ORACLE_DB','user'),
                                password=configur.get('ORACLE_DB','password'),
                                host=configur.get('ORACLE_DB','host'),
                                port=configur.get('ORACLE_DB','port'),
                                service_name=configur.get('ORACLE_DB','service_name'))
        
        return conn
    except Exception as e:
        raise e

# def oracle_get_conn():
#     try:
#         engine = create_engine(
#             f'oracle+oracledb://:@',
#             thick_mode=False,
#             connect_args={
#             "user": configur.get('ORACLE_DB','user'),
#             "password": configur.get('ORACLE_DB','password'),
#             "host": configur.get('ORACLE_DB','host'),
#             "port": configur.get('ORACLE_DB','port'),
#             "service_name": configur.get('ORACLE_DB','service_name')
#         })
#         connection = engine.connect()
#         connection = connection.execution_options(
#         isolation_level="AUTOCOMMIT"
#         )
#         return connection
#     except Exception as e:
#         raise e