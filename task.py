from RPA.Excel.Files import Files
from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem

from investments_table import investments_table
from list_agencies import list_agencies
from download_PDFs import download_PDFs
from excel_exporter import excel_exporter

import time

def get_list_agencies():
    agencies = list_agencies()
    print(agencies._parse_agencies())
    agencies._close_browser()

def get_investments_table(num):
    investments = investments_table(num)
    table = investments._parse_values()
    print(table)
    investments._close_browser()
    return table

def get_download_PDFs(num,table):
    PDFs = download_PDFs(num,table)
    PDFs._download_all_PDFs()
    time.sleep(120)

def main():
    get_list_agencies()
    table = get_investments_table('393')
    get_download_PDFs('393',table)

    excel = excel_exporter()

if __name__ == "__main__":
    main()
