# -*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template,request
import time
from sendMessage import send_text
import json
app = Flask(__name__)


@app.route('/weight')
def weightMonitor():
    fileData = open("D:\\python_projects\\weightMonitor\\weight.txt",'r')
    hasUpload = False
    curTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    curTimeHour = time.strftime('%H',time.localtime(time.time()))
    print curTimeHour
    datas = fileData.readlines()
    dates = []
    weights = []
    print type(datas)

    for data in datas:
        dates.append(data.strip().split(" ")[0])
        weights.append(data.strip().split(" ")[1])
        if curTime in data:
            hasUpload = True
            break

    if (curTimeHour == '16' or curTimeHour == '22' or curTimeHour == '23') and (hasUpload == False):
        print "daole"
        send_text(u"南刚雷今天的体重数据还没有上传！！！")
    # print dates
    # print weights

    return render_template("weight.html",hasUpload=hasUpload,dates=dates,weights=weights)

@app.route("/upload",methods=['POST','GET'])
def uploadData():
    print 1
    curTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    fileData = open("D:\\python_projects\\weightMonitor\\weight.txt",'a')
    # date = request.form.get('date')
    weight = request.form.get('weight')
    # print date
    # print weight
    fileData.write(curTime + " " + weight + "\n")
    fileData.close()
    return "success"
if __name__ == '__main__':
    app.run(host="10.129.152.64",port=8083,debug=True)