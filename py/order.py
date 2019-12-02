#!/usr/bin/python
#coding:utf-8

import time

menu = {"fired meat" : 30, "tomato fired egg" : 15, "seaweed and egg soup" :10, "steak" : 50}
time = {"fired meat" : 30, "tomato fired egg" : 15, "seaweed and egg soup" :10, "steak" : 50}
i = 0
nPrice = []
nOrder = []
nName = []
totalPrice = 0

def order(name, num):
    print('点餐' + str(name) + ',' + str(num) +'份,' + '总计：' + str(menu[name]*num))
    if name in nName:
        index = nName.index(name)
        nOrder[index][1] += num
        nPrice[index] += menu[name]*num
    else:
        nName.append(name)
        nPrice.append(menu[name]*num)
        nOrder.append([name,num])
    

def remove(name, num):
    print('删除'+str(name)+str(num)+'份')
    index = nName.index(name)
    nOrder[index][1] -=num
    nPrice[index] -= menu[name]*num

def total():
    global totalPrice
    if nPrice:
        for price in nPrice:
            totalPrice += price
        print('总计：' + str(totalPrice))
    else:
        totalPrice = 0
        print('总计：0')

def cook():
    if nOrder: 
        for order in nOrder:
            for k in range(0 , order[1]):    
                print( '正在烧' + str(order[0]) + ',第' + str(k+1) + '份...')
        print ('已完成！' )           
    else:
        print( '没有需要烧的菜！')

def deliver(name, address, telephone):
    print( '正送餐给位于'+str(address)+'的'+str(name)+'...')
    print ('已到，请来接餐！dialing'+str(telephone)+'...')
    print( '见到您很高兴，请您查验外卖...')

def payMoney(money):
    print( '付款'+str(money)+'...')

def checkThings():
    if nOrder: 
        for order in nOrder:
            for k in range(0,order[1]):    
                print( '正在check' + str(order[0]) + ',第' + str(k+1) + '份...')
        print( '已check完成！')            
    else:
        print( 'no order！')

def change(money, totalPrice):
    print( '找零'+str(money - totalPrice)+'元。')

if __name__ == "__main__":
    print('please review the menu:')
    for key in menu:
        print( key+",每份"+ str(menu[key]) + "元")
    guestA = input("今天的第"+ str(i+1) +"位客人：")
    addressA = input('位于：')
    telephone = input('电话：')
    order("steak", 3)
    remove('steak', 1)
    total()
    cook()
    deliver(guestA, addressA,telephone)
    checkThings()
    money = int(input('给钱：'))
    payMoney(money)
    change(money, totalPrice)
    print( '完成'+str(guestA)+'的交易，欢迎下次致电或亲自光临！')

    

