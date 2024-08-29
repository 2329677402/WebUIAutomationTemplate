"""
    实现功能：数据读取工具类，处理数据驱动测试的数据。
"""
import os
import pandas as pd
import pymysql
from openpyxl import Workbook, load_workbook


class DataReader:
    @staticmethod
    def load_excel_data(file_name):
        """
        功能：加载Excel数据文件
        """
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        return pd.read_excel(data_path)

    @staticmethod
    def load_csv_data(file_name: str, encoding='utf-8'):
        """
        功能：加载CSV数据文件
        """
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        return pd.read_csv(os.fspath(data_path), encoding=encoding)

    @staticmethod
    def load_sql_data(file_name, encoding='utf-8'):
        """
        功能：加载SQL数据文件
        """
        pass


if __name__ == '__main__':
    print(DataReader.load_excel_data('test_data.xlsx'))
    # print(DataReader.load_csv_data('test_data.csv'))
    # print(DataReader.load_sql_data('test_data.sql'))
