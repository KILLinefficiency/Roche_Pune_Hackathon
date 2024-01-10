import os
from typing import List, Union
import sqlite3 as sql

class Stats:
    def __init__(self):
        self.db = "stats_db.db"
        if not os.path.exists(self.db):
            self.connection = sql.connect(self.db, check_same_thread=False)
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE TABLE stats(int1 INT, int2 INT, lim INT, str1 TEXT, str2 TEXT, hits INT, stamp DATETIME);")
            self.connection.commit()
        else:
            self.connection = sql.connect(self.db, check_same_thread=False)
            self.cursor = self.connection.cursor()

    def add_record(self, data: List[Union[int, str]]):
        self.present_data = self.cursor.execute("SELECT * FROM stats WHERE int1 = ? AND int2 = ? AND lim = ? AND str1 = ? AND str2 = ?;", tuple(data))
        if len(self.present_data.fetchall()) == 0:
            self.cursor.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, 0, CURRENT_TIMESTAMP)", tuple(data))
            print(self.cursor.execute("SELECT * FROM stats;").fetchall())
        else:
            self.cursor.execute("UPDATE stats SET hits = hits + 1, stamp = CURRENT_TIMESTAMP WHERE int1 = ? AND int2 = ? AND lim = ? AND str1 = ? AND str2 = ?;", tuple(data))
            print(self.cursor.execute("SELECT * FROM stats;").fetchall())
        self.connection.commit()

    def get_max(self):
        self.max_hits = self.cursor.execute("SELECT MAX(hits) FROM stats;").fetchone()[0]
        self.params = self.cursor.execute("SELECT int1, int2, lim, str1, str2 FROM stats WHERE hits = ?;", (self.max_hits,)).fetchone()
        self.fields = ["int1", "int2", "limit", "str1", "str2"]
        if self.params == None:
            self.params = [0] * 5
        return dict(zip(self.fields, self.params))

    def get_frequent(self):
        self.recent = self.cursor.execute("SELECT MAX(stamp) FROM stats;").fetchone()[0]
        self.recent_hits = self.cursor.execute("SELECT hits FROM stats WHERE stamp = ?;", (self.recent,)).fetchone()
        if self.recent_hits == None:
            self.recent_hits = [0]
        return self.recent_hits[0]

    def end(self):
        self.connection.close()