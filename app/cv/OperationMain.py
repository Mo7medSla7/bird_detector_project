import threading
from queue import Queue

import pandas as pd
from app.cv.DetailsExtractor import DetailsExtractor
from app.cv.folderReader import FolderReader

def getDetails(folderPath):
    lock = threading.Semaphore(0)
    SENTINEL = object()  #SENTINEL OBJECT
    queue = Queue()
    res = []
    reader = FolderReader(folderPath,queue,SENTINEL)
    extractor = DetailsExtractor(queue,SENTINEL,lock,res)
    reader.start()
    extractor.start()
    lock.acquire()
    return res

def filterColumns(colunms:list,data):
    wantHead = colunms.__contains__('head')
    wantLeg = colunms.__contains__('leg')
    wantWing = colunms.__contains__('wing')
    wantTail = colunms.__contains__('tail')
    res = []
    for item in data:
        tempDict = {}
        if wantHead:
            tempDict['HEAD'] = item['HEAD']
        if wantLeg:
            tempDict['LEG'] = item['LEG']
        if wantWing:
            tempDict['Wing'] = item['Wing']
        if wantTail:
            tempDict['TAIL'] = item['TAIL']
        res.append(tempDict)
    return pd.DataFrame(res)
