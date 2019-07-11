#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login


# def elem

def loginStep(driver, user, passwd):
    try:
        # 登陆操作
        logins = login(driver)

        logins.elemObj().click()
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd)
        logins.subObj().click()
        logins.companyObj().click()
        logins.useraddObj().click()
        # 添加操作
        user1 = logins.add_userObj()
        pwd1 = logins.add_firpwdObj()
        pwd2 = logins.add_secpwdObj()
        real = logins.add_realnameObj()

        logins.add_chosenObj().click()
        logins.add_deptObj().click()
        logins.add_nameObj().send_keys(user1)
        logins.add_pwd1Obj().send_keys(pwd1)
        logins.add_pwd2Obj().send_keys(pwd2)
        logins.add_realObj().send_keys(real)
        logins.add_roleObj().click()
        logins.add_topObj().click()
        logins.add_choObj().click()
        logins.add_groupObj().click()
        logins.add_verifyObj().send_keys(passwd)
        logins.saveObj().click()


    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver

    dri = webdriver.Chrome()
    dri.get('http://118.24.211.165:8081')
    exam = login(dri)
    user = exam.userObj()
    passwd = exam.pwdObj()
    loginStep(dri, user, passwd)
