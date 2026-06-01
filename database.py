import pymysql

class Database():
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='22isp-1',
                charset='utfmb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            self.connection = None

    def get_user(self, login, password):
        try:
            with self.connetion.cursor() as cursor:
                sql = "SELECT id_user, role, full_name FROM users WHERE login=%s AND password=%s"
                cursor.execute(sql, (login, password))
                result = cursor.fetchone()
                return result
        except Exception as e:
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None