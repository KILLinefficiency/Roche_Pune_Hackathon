from flask import Flask, request
from fizzbuzz import fizzbuzz

server: Flask = Flask(__name__)

@server.route("/fizzbuzz")
def read_data() -> list[str]:
    try:
        int1:  int = int(request.args.get("int1"))
        int2:  int = int(request.args.get("int2"))
        limit: int = int(request.args.get("limit"))
    except ValueError:
        return ["int1, int2 and limit must be integers"]

    str1: str = request.args.get("str1")
    str2: str = request.args.get("str2")

    return fizzbuzz(int1, int2, limit, str1, str2)

@server.route("/statistics")
def show_stats() -> str:
    pass


if __name__ == "__main__":
    server.run()
