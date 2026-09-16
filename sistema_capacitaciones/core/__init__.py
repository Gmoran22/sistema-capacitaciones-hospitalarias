import pymysql

pymysql.install_as_MySQLdb()

# Desactivar la sintaxis RETURNING no soportada por MariaDB 10.4 de XAMPP
from django.db.backends.mysql.features import DatabaseFeatures
DatabaseFeatures.can_return_columns_from_insert = False
DatabaseFeatures.can_return_rows_from_bulk_insert = False