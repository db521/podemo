# -*- coding: utf-8 -*-


def x(a=3,*args,**kwargs):
    """
    args=[1,2,3,4]
    kargs={
    x:3,
    b:4
    }
    :param a:
    :param args:
    :param kwargs:
    :return:
    """
    dict=kwargs

    return a+1


x(5,[1,2,3,4],x=3,b=4)
