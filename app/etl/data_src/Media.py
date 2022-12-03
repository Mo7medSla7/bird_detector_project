from enum import Enum

from app.cv.ThreadingMain import readAndDetect
from app.etl.data_src.IDataTypes import IDataTypes


class MediaTypes(Enum):
    """Media Types"""
    IMAGE = "image"
    VIDEO = "video"

class Media(IDataTypes):
    """Media"""
    def __init__(self,type):
        super().__init__(type)

    def extract(self,path):
        res = readAndDetect(path)
        return res

    def load(self,path):
        #not implemented
        pass
