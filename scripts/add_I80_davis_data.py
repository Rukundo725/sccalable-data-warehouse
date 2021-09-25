import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    conn = mysql.connect(host='localhost', user='root', password='password',
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def emojiDB(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
    cur.execute(dbQuery)
    conn.commit()

def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTables(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)
    sqlFile = 'mysql/I80_davis_schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return


def insert_to_I80_davis_t_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    df = df.where((pd.notnull(df)), None)
    df = df.astype(object).where(pd.notnull(df), None)


    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (timestamp,ID,avg_speed,avg_flow,avg_occ,avg_freeflow_speed,samples_below_100pct_ff,
         samples_below_95pct_ff,samples_below_90pct_ff,samples_below_85pct_ff,samples_below_80pct_ff,
         samples_below_75pct_ff,samples_below_70pct_ff,samples_below_65pct_ff,samples_below_60pct_ff,
         samples_below_55pct_ff,samples_below_50pct_ff,samples_below_45pct_ff,samples_below_40pct_ff,
         samples_below_35pct_ff,samples_below_30pct_ff,samples_below_20pct_ff,samples_below_25pct_ff,
         samples_below_15pct_ff,samples_below_10pct_ff)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], row[14], row[15],row[16], row[17], row[18], (row[19]), (row[20]), row[21],row[22], 
                row[23], row[24])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def insert_to_richards_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    df = df.where((pd.notnull(df)), None)
    df = df.astype(object).where(pd.notnull(df), None)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (timestamp,flow1,occupancy1,flow2,occupancy2,flow3,occupancy3,totalflow,weekday,hour,minute,second)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def insert_to_station_summary_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------
    """

    conn, cur = DBConnect(dbName)

    df = df.where((pd.notnull(df)), None)
    df = df.astype(object).where(pd.notnull(df), None)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (ID,flow_99,flow_max,flow_median,flow_total,n_obs)
             VALUES(%s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], row[4], row[5])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def insert_to_weekday_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    df = df.where((pd.notnull(df)), None)
    df = df.astype(object).where(pd.notnull(df), None)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (ID,hour,minute,second,Unnamed: 4,totalflow)
             VALUES(%s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], row[4], row[5])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def insert_to_I80_median_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    df = df.where((pd.notnull(df)), None)
    df = df.astype(object).where(pd.notnull(df), None)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (ID,weekday,hour,minute,second,flow1,occupancy1,mph1,flow2,
        occupancy2,mph2,flow3,occupancy3,mph3,flow4,occupancy4,mph4,flow5,occupancy5,mph5,totalflow)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], row[14], row[15],row[16], row[17], row[18], row[19], row[20])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def insert_to_I80_stations_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    
    df = df.where((pd.notnull(df)), None)
    df = df.astype(object).where(pd.notnull(df), None)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (ID,Fwy,Dir,District,County,City,State_PM,Abs_PM,Latitude,
        Longitude,Length,Type,Lanes,Name,User_ID_1,User_ID_2,User_ID_3,User_ID_4)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], row[14], row[15],row[16], row[17])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    """

    Parameters
    ----------
    *args :

    many :
         (Default value = False)
    tablename :
         (Default value = '')
    rdf :
         (Default value = True)
    **kwargs :


    Returns
    -------

    """
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} records fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    createDB(dbName='I80_davis')
    emojiDB(dbName='I80_davis')
    createTables(dbName='I80_davis')

    richards = pd.read_csv('data/richards.csv')
    I80_stations = pd.read_csv('data/I80_stations.csv')
    station = pd.read_csv('data/station_summary.csv')
    weekday = pd.read_csv('data/weekday.csv')
    I80_median = pd.read_csv('data/I80_median.csv')
    I80_davis = pd.read_csv('data/I80_davis.csv')
    
    insert_to_I80_davis_t_table(dbName='I80_davis', df=I80_davis, table_name='I80_davis_t')
    insert_to_richards_table(dbName='I80_davis', df=richards, table_name='richards')
    insert_to_station_summary_table(dbName='I80_davis', df=station, table_name='station_summary')
    insert_to_weekday_table(dbName='I80_davis', df=weekday, table_name='weekday')
    insert_to_I80_stations_table(dbName='I80_davis', df=I80_stations, table_name='I80_stations')
    insert_to_I80_median_table(dbName='I80_davis', df=I80_median, table_name='I80_median')
    
