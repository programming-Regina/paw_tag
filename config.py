import os

DB_HOST = os.getenv("MYSQLHOST", "127.0.0.1")
DB_USER = os.getenv("MYSQLUSER", "root")
DB_PASSWORD = os.getenv("MYSQLPASSWORD", "")
DB_NAME = os.getenv("MYSQLDATABASE", "paw_tag")
DB_PORT = int(os.getenv("MYSQLPORT", 3306))