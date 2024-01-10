from typing import List, Dict, Union
from flask import Flask, request
from stats import Stats
from fizzbuzz import fizzbuzz

server: Flask = Flask(__name__)
stats: Stats = Stats()

@server.route("/fizzbuzz")
def read_data() -> List[str]:
    try:
        int1:  int = int(request.args.get("int1"))
        int2:  int = int(request.args.get("int2"))
        limit: int = int(request.args.get("limit"))
    except ValueError:
        return ["int1, int2 and limit must be integers"]

    str1: str = request.args.get("str1")
    str2: str = request.args.get("str2")
    
    record: List[Union[int, str]] = [int1, int2, limit, str1, str2]
    stats.add_record(record)

    return fizzbuzz(*record)

@server.route("/stats")
def show_stats() -> Dict[Union[str, any]]:
    return {
        "max": stats.get_max(),
        "frequent": stats.get_frequent()
    }


if __name__ == "__main__":
    server.run()
    stats.end()
