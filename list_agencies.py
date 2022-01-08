from RPA.Browser.Selenium import Selenium
import datetime
class list_agencies:
    def __init__(self):
        self.browser = Selenium()
        self.browser.open_available_browser("https://itdashboard.gov/")

    def _wait_element(self,path):
        self.browser.wait_until_element_is_visible(
            locator=path,
            timeout=datetime.timedelta(seconds=60)
        )

    def _click_element(self,path):
        self._wait_element(path)
        self.browser.click_element_when_visible(path)

    def _get_list_agencies(self):
        self._click_element('css:#node-23>div>div>div>div>div>div>div>a')
        self._wait_element('css:#agency-tiles-widget > div > div:nth-child(1) > div:nth-child(2) > div > div > div')
        agencies = self.browser.get_webelements('css:#agency-tiles-widget > div > div > div > div > div > div')
        return agencies
    
    def _get_agency_name(self,agency):
        self.browser.wait_until_element_is_visible(
            locator=[agency, 'css:span:nth-of-type(1)']
        )
        return self.browser.get_webelement(locator=[agency, 'css:span:nth-of-type(1)']).text
    
    def _get_agency_amount(self,agency):
        self.browser.wait_until_element_is_visible(
            locator=[agency, 'css:span:nth-of-type(2)']
        )
        return self.browser.get_webelement(locator=[agency, 'css:span:nth-of-type(2)']).text

    def _get_agency_id(self,agency):
        self.browser.wait_until_element_is_visible(
            locator=[agency, 'css:a']
        )
        link = self.browser.get_element_attribute(locator=[agency, 'css:a'], attribute='href')
        id = link.split('/')[-1]
        return id

    def _close_browser(self):
        self.browser.close_browser()

    def _parse_agencies(self):
        agencies_array = self._get_list_agencies()
        agencies = []
        id = 0
        for agency_e in agencies_array:
            id += 1
            agency = {
                'title': self._get_agency_name(agency_e),
                'amount': self._get_agency_amount(agency_e),
                'id': self._get_agency_id(agency_e)
            }
            agencies.append(agency)
        return agencies
