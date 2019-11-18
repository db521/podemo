
from pageobject.Addpage import Add
def add_bm(driver,name):
    try:
        adds=Add(driver)
        adds.bumen_obj().click()
        adds.zuzhi_obj().click()
        adds.input_obj().send_keys(name)
        adds.submit_obj().click()
    except Exception as e:
        raise e
