from util.method import open_file
from moudle.login import logining
def test_login():
    try:
        from selenium import webdriver
        driver=webdriver.Chrome()
        urls=open_file('urls.json')
        driver.get(urls['url'])
        users=open_file('user.json')
        logining(driver,users['user'],users['passwd'])

    except Exception as e:
        raise e

if __name__ == '__main__':
    test_login()