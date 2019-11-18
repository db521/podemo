#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json


class Read_Write(object):  # 读写操作

    def read_write(self, path):
        try:
            with open(path, 'r+', encoding="utf-8") as p:
                datadict = json.loads(p.read())

            return datadict

        except Exception as ep:
            raise ep
