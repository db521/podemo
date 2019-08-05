from pageobject.zhou_lo import Zhou_log
import json

def To_log(driver):

    try:

        with open('D:\PO\zhoukao\config\login.json','r',encoding='utf-8') as f:
            u_ele = json.loads(f.read())
            user = u_ele['user']
            password = u_ele['password']

        logins = Zhou_log(driver)
        logins.read_Element().click()
        logins.read_Login_User().send_keys(user)
        logins.read_Login_Password().send_keys(password)
        logins.read_Login_Button().click()

    except Exception as e:
        raise e
