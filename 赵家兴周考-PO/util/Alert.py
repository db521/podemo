def alert_accept(driver):
    try:
        return driver.switch_to_alert().accept()
    except Exception as e:
        raise e