from robot.api.deco import library, keyword
from RPA.Browser.Selenium import Selenium
from robot.libraries.BuiltIn import BuiltIn
from openpyxl import Workbook
from openpyxl.styles import Font
import datetime as datetime


@library(scope='GLOBAL', auto_keywords=True)
class User_defined_Library:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.filename = None
        # Library to be used in RPA framework  RPA.Browser.Selenium
        self.selLib = BuiltIn().get_library_instance('RPA.Browser.Selenium')


    # retrives data from webpage and fills in excel
    @keyword
    def get_all_values(self, Rolelocator, desXpath, companyXpath, next_loc):
        self.selLib = BuiltIn().get_library_instance('RPA.Browser.Selenium')
        # function that provides excel formation
        self.write_excel()
        print("----------------------------------------------------------------")
        a = self.selLib.get_webelement("//a[@class='fleft fs14 btn-secondary br2 previous']")
        print(a.get_attribute("disabled"))
        b = self.selLib.get_webelement("//a[@class='fright fs14 btn-secondary br2']")
        print(b.get_attribute("disabled"))
        # Fetching data from page and entering into excel
        self.fetchDataInPage(Rolelocator, desXpath, companyXpath)
        #  Fetch all the data for required input
        self.reser(Rolelocator, desXpath, companyXpath, next_loc)
        # creating file name and saving filename in specified folder
        self.create_filename()
        self.save_file()
        return self.filename

    def reser(self, Rolelocator, desXpath, companyXpath, next_loc):
        self.selLib.execute_javascript('window.scrollTo(0,600)')
        print(self.selLib.does_page_contain_element(next_loc))
        b = self.selLib.get_webelement("//a[@class='fright fs14 btn-secondary br2']")
        print(b.get_attribute("disabled"))
        if None == b.get_attribute("disabled"):
            self.selLib.click_element(next_loc)
            self.fetchDataInPage(Rolelocator, desXpath, companyXpath)
            self.reser(Rolelocator, desXpath, companyXpath, next_loc)
        else:
            return

    #  fetches data from the page and adds in excel
    def fetchDataInPage(self, Rolelocator, desXpath, companyXpath):
        count = self.selLib.get_element_count(Rolelocator)
        print(count)
        for i in range(1, count):
            Role = self.selLib.get_webelement(Rolelocator + "[" + str(i) + "]")
            print(Role.text)
            Roledescription = self.selLib.get_webelement(desXpath + "[" + str(i) + "]")
            print(Roledescription.text)
            company = self.selLib.get_webelement(companyXpath + "[" + str(i) + "]")
            print(company.text)
            # adds data to excel in row wise
            self.ws2.append([Role.text, Roledescription.text, company.text])

    # header in excel
    def color_Txt(self):
        self.txtfont = Font(color="00000000", bold=True, size=15)
        return self.txtfont

    def write_excel(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws2 = self.wb.create_sheet("Mysheet", 0)
        self.ws2.title = "Data"
        self.ws2.sheet_properties.tabColor = "1072BA"
        self.ws2['A1'].font = self.color_Txt()
        self.ws2['B1'].font = self.color_Txt()
        self.ws2['c1'].font = self.color_Txt()
        self.ws2['A1'] = "Role"
        self.ws2['B1'] = "Role Description"
        self.ws2['c1'] = "Company name"

    def save_file(self):
        self.wb.save('Datafiles/' + self.filename)

    def create_filename(self):
        self.filename = "NaukriData_" + str(datetime.datetime.now().date()) + '_' + str(
            datetime.datetime.now().time()).replace(':', '.') + '.xlsx'

  