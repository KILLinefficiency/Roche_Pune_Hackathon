from typing import List

def fizzbuzz(x: int, y: int, limit: int, a: str, b: str) -> list[str]:
    fb_data: List[str] = list(map(str, range(1, limit + 1)))

    for n in range(1, limit + 1):
        if n % (x * y) == 0:
            fb_data[n - 1] = a + b
        elif n % x == 0:
            fb_data[n - 1] = a
        elif n % y == 0:
            fb_data[n - 1] = b

    return fb_data
