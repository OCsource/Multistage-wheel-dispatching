# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# @author   : 关宅宅
# @time     : 2019-4-2 19:21
# @file     : process.py
# @Software : PyCharm Community Edition

class process(object):
    def __init__(self,id, startTime, serverTime):
        self.id = id
        self.startTime = startTime
        self.serverTime = serverTime
        self.endTime = 0
        self.getTime = 0

    def getEnd(self,time):
        self.endTime = time

    def __str__(self):
        return "id: "+ str(self.id) + "\n" + "startTime: " + str(self.startTime) + "\n" + "serverTime: " + str(self.serverTime) + "\n"