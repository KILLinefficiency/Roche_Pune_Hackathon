import os
import sqlite3 as sql

class Stats:
    def __init__(self):
        self.db = "stats_db.db"
        if not os.path.exists(self.db):
            self.connection = sql.connect(self.db)
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE TABLE stats(int1 INT, int2 INT, lim INT, str1 TEXT, str2 TEXT, hits INT);")
        else:
            self.connection = sql.connect(self.db)
            self.cursor = self.connection.cursor()

    def add_record(self, data: list[str]):
        self.present_data = self.cursor.execute("SELECT * FROM stats WHERE int1 = ? AND int2 = ? AND lim = ? AND str1 = ? AND str2 = ?;", tuple(data))
        if len(self.present_data.fetchall()) == 0:
            self.cursor.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, 0)", tuple(data))
            print(self.cursor.execute("SELECT * FROM stats;").fetchall())
        else:
            self.cursor.execute("UPDATE stats SET hits = hits + 1 WHERE int1 = ? AND int2 = ? AND lim = ? AND str1 = ? AND str2 = ?;", tuple(data))
            print(self.cursor.execute("SELECT * FROm stats;").fetchall())

    def get_max(self):
        self.max_hits = self.cursor.execute("SELECT MAX(hits) FROM stats;").fetchone()[0]
        self.params = self.cursor.execute("SELECT int1, int2, lim, str1, str2 FROM stats WHERE hits = ?", (self.max_hits,)).fetchone()
        return {
            "int1": self.params[0],
            "int2": self.params[1],
            "lim" : self.params[2],
            "str1": self.params[3],
            "str2": self.params[4]
        }

    def end(self):
        self.connection.commit()
        self.connection.close()

s = Stats()
s.add_record(["1", "1", "1", "d", "e"])
s.add_record(["2", "2", "2", "d", "e"])
s.add_record(["2", "2", "2", "d", "e"])
print(s.get_max())
s.end()
