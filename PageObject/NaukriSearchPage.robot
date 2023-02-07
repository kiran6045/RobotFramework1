*** Settings ***
Library         RPA.Browser.Selenium

*** Variables ***
# Search Keyword
${Keyword_search}     Automation test engineer
#Search box locators
#${Search_box}         xpath://div[@title='Search input textbox']
${Search_box}         xpath://input[@name='qp']
${Searchbtn_loc}      //button[@type='submit']
#Locators for roles, company , description
${Roles_loc}         xpath:(//article[@class='jobTuple']//child::div[@class='info fleft']/a)
${company_loc}       xpath:(//article[@class='jobTuple']//child::div[@class='info fleft']/div[@class='companyInfo subheading']/a[@class='subTitle ellipsis fleft'])
${descrip_loc}       xpath:(//article[@class='jobTuple']//child::div[@class='ellipsis job-description'])
${next_loc}          xpath://a[@class='fright fs14 btn-secondary br2']//span[contains(text(),'Next')]
#Locators for input search box,button


*** Keywords ***
Search required details by entering Keyword
    Sleep    2
    Input Text              ${Search_box}     ${Keyword_search}
    Sleep    1
    Double Click Element    ${Searchbtn_loc}
    Sleep    1



