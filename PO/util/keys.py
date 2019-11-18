from selenium.webdriver.common.keys import Keys

def Key_Enter():
    try:
        return Keys.ENTER
    except Exception as e:
        raise e