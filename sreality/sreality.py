#!/usr/bin/env python3

import json
import requests
from .constants import *

class Sreality:
    API_BASE = "https://sreality.cz/api/cs/v2/estates"

    def __init__(self):
        pass

    def _stringify_argument(self, argument):
        if isinstance(argument, list):
            return "|".join([str(x) for x in argument])

        return argument

    def fetch(self, limit=None, **kwargs):
        if not "category_main_cb" in kwargs:
            kwargs["category_main_cb"] = CategoryMainCB.ALL
        if not "page" in kwargs:
            kwargs["page"] = 1

        for key, val in kwargs.items():
            kwargs[key] = self._stringify_argument(val)

        page_limit = 0 if limit is None else kwargs["page"] + limit

        while True:
            res = requests.get(Sreality.API_BASE, params=kwargs)
            print(res.url)
            if res.status_code != 200:
                raise StopIteration()
            jtree = json.loads(res.text)
            #results = jtree["result_size"]
            estates = jtree["_embedded"]["estates"]
            print("Page: ", jtree["page"])

            yield estates

            kwargs["page"] += 1
            if page_limit and kwargs["page"] == page_limit:
                raise StopIteration()
