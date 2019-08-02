from module.modulepage import Element_page

def login(driver):
    try:
        element_page=Element_page(driver)
        element_page.kyObj().click()

        element_page.userObj().send_keys(element_page.user_value())
        element_page.passwdObj().send_keys(element_page.passwd_value())
        element_page.btnObj().click()

        element_page.zuzhiObj().click()
        element_page.bumenObj().click()

        element_page.iObj().click()
        element_page.xiaoObj().click()
        element_page.addObj().send_keys(element_page.bumen_value())
        element_page.addbumenObj().click()


    except Exception as e:
        raise e


