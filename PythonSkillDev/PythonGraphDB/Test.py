import time
from loadbar import LoadBar


def test():
    bar = LoadBar(
        max=5
    )
    bar.start()
    for x in range(5):
        bar.update(step=x)
        time.sleep(1)
    bar.end()


if __name__ == "__main__":
    test()
