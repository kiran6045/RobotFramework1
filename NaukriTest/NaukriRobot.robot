***** Settings ***
Library         RPA.Browser.Selenium
# imported user defined library
Library        ../CustomLib/User_defined_Library.py
# points to another robot file to access the defined keyword
Resource       ../PageObject/NaukriLoginPage.robot
Resource       ../PageObject/NaukriSearchPage.robot



#*** Variables ***
#${filename}     NaukriData_2022-12-26_22.31.06.677001.xlsx


*** Test Cases ***
NaukriTask
   Login to Naukri Website
   Check highlighting popup asked for suggestion
   Search required details by entering Keyword
   ${Count}       Get Element Count         ${Roles_loc}
   IF    ${Count} <= 0
        log   Locator is changed or page is not loaded properly
   ELSE
         ${filename}     Get All Values    ${Roles_loc}    ${descrip_loc}     ${company_loc}    ${next_loc}
         Set Global Variable    ${filename}
         Log To Console         ${filename}
   END






    
    
