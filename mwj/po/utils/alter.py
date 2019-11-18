
def Alter(driver):
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        raise e