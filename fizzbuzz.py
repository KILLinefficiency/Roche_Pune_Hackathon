from typing import List

def fizzbuzz(x: int, y: int, limit: int, a: str, b: str) -> list[str]:
    fb_data: List[str] = []

    for n in range(1, limit + 1):
        if n % (x * y) == 0:
            fb_data.append(a + b)
        elif n % x == 0:
            fb_data.append(a)
        elif n % y == 0:
            fb_data.append(b)
        else:
            fb_data.append(str(n))

    return fb_data
