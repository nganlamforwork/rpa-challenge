from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem
import datetime
import os
class download_PDFs:
    def __init__(self,id,table):
        self.browser = Selenium()
        self.files = FileSystem()
        self._id = id
        self._table = table

    def _wait_element(self,path):
        self.browser.wait_until_element_is_visible(
            locator=path,
            timeout=datetime.timedelta(seconds=60)
        )

    def _click_element(self,path):
        self._wait_element(path)
        self.browser.click_element_when_visible(path)

    def _get_links(self):
        links = []
        for row in self._table:
            links.append(row[0])
        return links

    def _open_link(self,link):
        self.browser.set_download_directory(
            directory="{}/output".format(os.getcwd()),
            download_pdf=True
        )
        self.browser.open_available_browser(link)
    
    def _download_PDF(self):
        self._wait_element('css:#business-case-pdf > a')
        self._click_element('css:#business-case-pdf > a')

    def _wait_for_completed_download(self,name):
        while self.files.does_file_not_exist(
            "{}/output/{}.pdf".format(os.getcwd(),name)
        ): 
            continue

    def _download_all_PDFs(self):
        links = self._get_links()
        
        for link in links:
            if link is not "":
                self._open_link(link)
                self._download_PDF()
                self._wait_for_completed_download(link.split('/')[-1])
                self.browser.close_browser()
