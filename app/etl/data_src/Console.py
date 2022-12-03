from app.etl.data_src.IDataTypes import IDataTypes

from enum import Enum


class ConsoleTypes(Enum):
    CONSOLE = 'console'
    OTHER = 'other'


class Console(IDataTypes):
    def __init__(self, type) -> None:
        super().__init__(type)

    def extract(self):
        raise NotImplementedError('Extract method not implemented for console')

    def load(self, data, file_path):
        if self.type == ConsoleTypes.CONSOLE:
            print(data)
        elif self.type == ConsoleTypes.OTHER:
            return data