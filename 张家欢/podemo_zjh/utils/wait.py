#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium.webdriver.support.ui import WebDriverWait


class ExplicitWait(object):  # 显示等待加元素定位

    def explicitWait(self, driver, locateProperty, locatorValue):
        try:
            # 显示等待加元素定位
            elements = WebDriverWait(driver, 15, 0.5).until(
                lambda x: x.find_element(by=locateProperty, value=locatorValue))
            return elements

        except Exception as ep:
            raise ep
