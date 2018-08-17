Majormode Perseus MicrORM Python Library is a small, little, mini, tiny, micro Object-Relational Mapping (ORM).

MicrORM is not a object-relational mapping in the sense it maps Pyth objects to a Relational DataBase Management System (RDBMS), but in the sense it maps results of SQL queries, executed on a RDBMS, to Python objects.

```
from majormode.perseus.utils import rdbms

with RdbmsConnection.acquire_connection() as connection:
    cursor = connection.execute('''
        SELECT a, b, c
          FROM foo
          WHERE a = %(a)s''',
        { 'a': 1 })
```
