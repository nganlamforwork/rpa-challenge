from RPA.Browser.Selenium import Selenium
import datetime
class investments_table:
    URL = "https://itdashboard.gov/drupal/summary/{}"

    def __init__(self, id):
        self._link = self.URL.format(id)
        self.browser = Selenium()
        self.browser.open_available_browser(self._link)

    def _wait_element(self,path):
        self.browser.wait_until_element_is_visible(
            locator=path,
            timeout=datetime.timedelta(seconds=60)
        )

    def _click_element(self,path):
        self._wait_element(path)
        self.browser.click_element_when_visible(path)

    def _show_all_rows(self):
        self.browser.wait_until_element_is_visible(
            locator='css:#investments-table-object_length > label > select',
            timeout=datetime.timedelta(seconds=60)
        )
        self.browser.click_element(
            locator='css:#investments-table-object_length > label > select'
        )

        self.browser.wait_until_element_is_visible(
            locator='css:#investments-table-object_length > label > select > option:nth-child(4)',
            timeout=datetime.timedelta(seconds=60)
        )
        self.browser.click_element(
            locator='css:#investments-table-object_length > label > select > option:nth-child(4)'
        )    

        self.browser.wait_until_element_is_visible(
            locator='css:#investments-table-object  tbody  tr:nth-of-type(11) td',
            timeout=datetime.timedelta(seconds=60)
        )

        return self.browser.get_webelement('css:#investments-table-object')

    def _get_all_rows(self, table):
        self.browser.wait_until_element_is_enabled(locator=[table, 'css:table tbody tr'])
        elements = self.browser.get_webelements(locator=[table, 'css:table tbody tr'])
        return elements

    def _get_values_in_row(self, row):
        elements = self.browser.get_webelements(locator=[row, 'css:td'])
        return elements
    
    def _close_browser(self):
        self.browser.close_browser()

    def _parse_values(self):
        table = self._show_all_rows()
        rows = self._get_all_rows(table)
        print(type(rows))

        investmentTable = []

        for row in rows:
            values = self._get_values_in_row(row)
            element = []
            for i,value in enumerate(values):
                if i == 0: 
                    check = self.browser.get_element_count(locator=[value, 'css:a'])
                    if check > 0:
                        _link = self.browser.get_element_attribute(locator=[value, 'css:a'], attribute='href')
                        _text = self.browser.get_webelement(locator=[value, 'css:a']).text
                    else:
                        _link = ''
                        _text = value.text
                    element.append(_link)
                else:
                    _text = value.text
                element.append(_text)
            investmentTable.append(element)
        return investmentTable
