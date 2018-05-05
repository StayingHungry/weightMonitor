#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/5 16:16
# @Author  : nanganglei
# @File    : sendMessage.py


import requests
import json

path_total = "stock_total.png"
path_part = "stock_part.png"



Secret = "mto9vGr1xjxxttCFaX1KlWgqr1sALUP8zHbpnqRolQw"
Secret_app_1000002 = "40Sn3F8dcTgwKh9Ah33w-mu0MqlUZARXxawFFEcsfOg"
Secret_app_1000003 = "YZD70w-ltuLhFOesq04KBMPgbTFJJh9x9_guBuxqTdQ"



def get_token4appfor1000003():
    ID = "ww731cd4a99c6e7ff5"
    gurl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(ID, Secret_app_1000003)
    r = requests.get(gurl)
    dict_result = (r.json())
    # print dict_result['access_token']
    return dict_result['access_token']



def get_token4app():
    ID = "ww731cd4a99c6e7ff5"
    gurl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(ID, Secret_app_1000002)
    r = requests.get(gurl)
    dict_result = (r.json())
    # print dict_result['access_token']
    return dict_result['access_token']
def get_token():  ##获取TOKEN
    ID = "ww731cd4a99c6e7ff5"

    gurl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(ID, Secret)
    r = requests.get(gurl)
    dict_result = (r.json())
    return dict_result['access_token']

def get_media_ID(path):  ##上传到临时素材  图片ID
    Gtoken = get_token()
    img_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=image".format(Gtoken)
    files = {'image': open(path, 'rb')}
    r = requests.post(img_url, files=files)
    re = json.loads(r.text)
    return re['media_id']


def send_text(text):  ##发送文字
    post_data = {}
    msg_content = {}
    msg_content['content'] = text  ## 消息内容，最长不超过2048个字节
    post_data['touser'] = "@all"
    # post_data['toparty'] = "@all"
    post_data['msgtype'] = 'text'
    post_data['agentid'] = 1000003
    post_data['text'] = msg_content
    post_data['safe'] = '0'  #表示是否是保密消息，0表示否，1表示是，默认0
    Gtoken = get_token4appfor1000003()
    purl1="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(Gtoken)
    json_post_data = json.dumps(post_data,False,False)
    # print json_post_data
    request_post = requests.post(purl1,data=json_post_data.encode(encoding='UTF8'))
    print (request_post.content)
    return request_post


def  send_tu(path):  ##发送图片
    img_id = get_media_ID(path)
    post_data1 = {}
    msg_content1 = {}
    msg_content1['media_id'] = img_id
    post_data1['touser'] = "@all"
    post_data1['toparty'] = 1
    post_data1['msgtype'] = 'image'
    post_data1['agentid'] = 1000002
    post_data1['image'] = msg_content1
    post_data1['safe'] = '0'
    Gtoken = get_token4app()
    purl2="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(Gtoken)
    json_post_data1 = json.dumps(post_data1,False,False)
    request_post = requests.post(purl2,data=json_post_data1.encode(encoding='UTF8'))
    return request_post

def get_user(user_id): ##获取用户
    Gtoken = get_token()
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={}&userid={}".format(Gtoken,user_id)
    print (url)
    request_user = requests.get(url)
    print (request_user.content)

def get_department(id=""):
    Gtoken = get_token()
    url = "https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={}&id={}".format(Gtoken,id)
    request_department = requests.get(url)
    # print request_department.content

