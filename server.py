from typing import List, Dict, Union
from flask import Flask, request
from stats import Stats
from fizzbuzz import fizzbuzz

server: Flask = Flask(__name__)
stats: Stats = Stats()

@server.route("/")
def index() -> str:
    return "<h1>Possible routes:<h1><h2>/fizzbuzz for fizzbuzz endpoint<br><br>/stats for statistics endpoint</h2>"

@server.route("/fizzbuzz")
def read_data() -> List[str]:
    try:
        int1:  int = int(request.args.get("int1"))
        int2:  int = int(request.args.get("int2"))
        limit: int = int(request.args.get("limit"))
    except ValueError:
        #  Throw an error on the endpoint if types don't match.
        return ["int1, int2 and limit must be integers"]

    str1: str = request.args.get("str1")
    str2: str = request.args.get("str2")
    
    record: List[Union[int, str]] = [int1, int2, limit, str1, str2]

    #  Add the list of parameters to the database.
    stats.add_record(record)

    #  Spread the list to parameters as arguments to the fizzbuzz function.
    return fizzbuzz(*record)

@server.route("/stats")
def show_stats() -> Dict[str, Union[str, Union[int, Dict[str, str]]]]:
    return {
        "max_hits_params": stats.get_max(),
        "frequent_req_hits": stats.get_frequent()
    }


if __name__ == "__main__":
    server.run()
    stats.end()
