#!/usr/bin/env python3

from sreality import *


if __name__ == "__main__":
    sr = Sreality()

    args = {
        "category_main_cb" : CategoryMain.HOUSE,
        "room_count_cb" : [ 2, 3, 4 ]
    }

    for page in sr.fetch(limit=2, **args):
        for estate in page:
            print("{} - {} ({})".format(estate["name"], estate["locality"], estate["price"]))
