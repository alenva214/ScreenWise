import pymysql.cursors

DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'screen_time_tracker',
    'cursorclass': pymysql.cursors.DictCursor
}
