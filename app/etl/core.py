import pandas as pd
from app.etl.data_src.DataSrcFactory import DataSrcFactory
from app.etl.extract import __extract_from_csv,__extract_from_sqlite,__extract_from_mssql,__extract_from_html,__extract_from_json,__extract_from_xml,__extract_from_excel,__extract_from_video
from app.etl.helpers import __get_source_type, __filter
from app.etl.load import __load_to_csv, __load_to_sqlite, __load_to_mssql, __load_to_html, __load_to_json, __load_to_xml, __load_to_excel


result = None

# class flat_db():
#     def __init__(self,source_type):
#         self.source_type = source_type
#
#     def factory_method(self):
#         if self.source_type == 'csv':
#         return

def extract(source_type:str,data_source:str) -> pd.DataFrame:
    data = DataSrcFactory.createDataObj(source_type, data_source)
    data = data.extract(data_source)
    return data




def transform(data:pd.DataFrame, criteria:dict) -> pd.DataFrame:

    if type(data) == str:
        if criteria['FILTER']:
            pass
    else:
        # filtering
        if criteria['FILTER']:
            data = __filter(data, criteria['FILTER'])

        # columns
        if criteria['COLUMNS'] != '__all__':
            data = data.filter(items=criteria['COLUMNS'])

        # distinct
        if criteria['DISTINCT']:
            data = data.drop_duplicates()

        # ordering
        if criteria['ORDER']:
            column = criteria['ORDER'][0]
            data = data.sort_values(column, ascending=criteria['ORDER'][1] == 'ASC')

        # limit
        if criteria['LIMIT']:
            data = data[:criteria['LIMIT']]
    return data


def load(data:pd.DataFrame, data_destination:str,source_type:str):
    global result
    data_source = DataSrcFactory.createDataObj(source_type,data_destination)
    result = data_source.load(data,data_destination)
    if result is None:
        result = "Execution Done!"
    return data