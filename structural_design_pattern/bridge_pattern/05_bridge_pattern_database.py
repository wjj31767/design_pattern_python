"""
数据库访问层（数据操作 vs 数据库类型）
场景描述
开发一个通用数据库访问框架，支持增删改查（CRUD）操作和不同数据库（MySQL、PostgreSQL、MongoDB），要求操作和数据库实现分离。
抽象与实现分离
抽象部分（数据操作）：定义 DataOperation 抽象类，声明操作接口（如 insert(), select()），持有数据库连接的引用。
"""


class DataOperation:
    def __init__(self, db_connection):
        self.db_connection = db_connection  # 桥接数据库连接

    def insert(self, data):
        raise NotImplementedError


class UserTable(DataOperation):
    def insert(self, user_data):
        formatted_data = self.format_data(user_data)
        self.db_connection.execute_sql(f"INSERT INTO users VALUES {formatted_data}")

    def format_data(self, data):
        # 数据格式化逻辑（与数据库无关）
        return data


class DBConnection:
    def execute_sql(self, sql):
        raise NotImplementedError


class MySQLConnection(DBConnection):
    def execute_sql(self, sql):
        print(f"MySQL 执行：{sql}")


class PostgreSQLConnection(DBConnection):
    def execute_sql(self, sql):
        print(f"PostgreSQL 执行：{sql}")
