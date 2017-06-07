#coding: utf-8

import shelve
import datetime

DATA_FILE = 'guestbook.dat'
greeting_list = []

def save_data(name,comment,create_at):
    """保存提交的数据"""
    database = shelve.open(DATA_FILE)
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']
    greeting_list.insert(0,{
        'name':name,
        'comment':comment,
        'create_at':create_at,
    })

    database['greeting_list']=greeting_list

    database.close()

save_data('test','test comment',datetime.datetime(2016,10,31,10,0,0))