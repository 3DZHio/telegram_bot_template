def select(
    columns: str, table: str, conditions: str, offset: str = "0", limit: str = "1"
) -> str:
    """SELECT"""
    return f"SELECT {columns} FROM {table} WHERE {conditions} OFFSET {offset} LIMIT {limit};"


def insert(table: str, columns: str, values: str) -> str:
    """INSERT"""
    return f"INSERT INTO {table} ({columns}) VALUES ({values});"


def update(table: str, column: str, value: str, conditions: str) -> str:
    """UPDATE"""
    return f"UPDATE {table} SET {column} = {value} WHERE {conditions};"
