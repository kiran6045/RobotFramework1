*** Settings ***
Library         RPA.Browser.Selenium
*** Variables ***
# Browser name and Link
${naukriURL}          https://www.naukri.com/
${Browser}            chrome
# Naukri Credentials
${Usernme}            Joysiril.m@gmail.com
${pwd}                Joysiril@30
# username,Pwd,button locators
${usr_loc}           xpath://input[@placeholder='Enter your active Email ID / Username']
${pwd_loc}           xpath://input[@placeholder='Enter your password']
${btn_loc}           xpath://button[@type='submit']
*** Keywords ***
Login to Naukri Website
    Open Browser                ${naukriURL}    ${Browser}
    Maximize Browser Window
#    Set Selenium Speed           1
    Set Browser Implicit Wait    2
    Click Element               id:login_Layer
    Input Text                  ${usr_loc}      ${Usernme}
    Input Password              ${pwd_loc}      ${pwd}
    Click Button                ${btn_loc}
Check highlighting popup asked for suggestion
    ${value}    Does Page Contain Button    xpath://form[@name='skip']//button
    Log To Console    ${value}
    IF  ${value}
            Click Button    xpath://form[@name='skip']//button
    END



