from module.login import Element_page

def login(driver):
    try:
        element_page = Element_page(driver)
        element_page.kyObj().click()
        element_page.nameObj().send_keys(element_page.name_value())
        element_page.pwdObj().send_keys(element_page.pwd_value())
        element_page.butObj().click()
        element_page.zuObj().click()

    except Exception as e:
        raise e