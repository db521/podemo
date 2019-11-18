#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pageobject.loginobj import *


class LoginStep(object):  # 登录步骤，输入用户名密码，点击登录

    def loginstep(self, driver01, users, passwd):
        try:
            Login(driver01).uelementfunction().send_keys(users)
            Login(driver01).pelementfunction().send_keys(passwd)
            Login(driver01).sbelementfunction().click()

        except Exception as ep:
            raise ep
