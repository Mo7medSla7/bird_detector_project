from enum import Enum

from app.cv.main import ClsMotion
from app.etl.data_src.IDataTypes import IDataTypes


class MediaTypes(Enum):
    """Media Types"""
    IMAGES = "images"
    VIDEO = "video"

class Media(IDataTypes):
    """Media"""
    def __init__(self,type,path):
        self.type = type
        self.obj = ClsMotion(path)
    def extract(self,path):
        if self.type == MediaTypes.VIDEO:
            # getPose() => read frames,perform the model on those frames to dict
            # res = ThreadingMain().readAndDetect(path)
            # return res
            pass

        elif self.type == MediaTypes.IMAGES:
            # getDetails(folderPath) => loop each file transform name to dict
            data = self.obj
            return data
    def load(self,data,path):
        #has no load
        pass
