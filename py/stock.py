#!/home/sgl/.virtualenvs/ACME/bin/python3
#coding:utf-8


import matplotlib.pyplot as plt
import math
import csv

class StockInfo:

    def get_stock_info(self):
        self.u_principal_up = self.s_user_pp['principal_up']
        self.u_principal_down = self.s_user_pp['principal_down']
        # self.return_thred = self.s_user_pp['return_thred']
        self.other_cost = self.s_user_pp['other_cost']
        self.population = self.s_user_pp['population']
        self.cost_per_day_one = self.s_user_pp['cost_per_day_one']
        self.s_cost = 200 + 100 # time cost + transaction fee 

    def reader(self, fname):
        f = open('values.csv', 'r')

        with f:

            reader = csv.DictReader(f)

        for row in reader:
            print(row['min'], row['avg'], row['max'])

    def writer(self, fname, nms):
        f = open('numbers2.csv', 'w')

        with f:
            writer = csv.writer(f)

        for row in nms:
            writer.writerow(row) 

class StockAdvice:

    s_user_pp = {
        'principal_up' : 30000,        
        'principal_down' : 20000,
        'cost_per_day_one' : 100,
        'population': 3,
        'other_cost': 10000,
        # 'return_thred': 480,
    }

    # s_stock_info = {
    #     "open_price": 290,
    #     "last_close_price": 287.4,
    #     "ave_price": 323.6,
    #     "support_price": 280.4,
    #     "resistance_price": 348,
    #     "peak_price": 460,
    #     "profit_rate": 0.03618,
    #     "OC_rate": 0.0313,
    # }
    """
    prime 's' means the variable is used for a real transaction
    """
    def __init__(self,tag, trans_rate):
        super().__init__()
        self.tag = tag
        self.TRANS_RATE = trans_rate
        self.s_in = 0.0
        self.s_in_cost = 0.0
        self.s_out = 0.0
        self.s_Qty = 100
        self.s_principal = 25000
        self.s_all_principal = 50000
        # self.
        self.get_user_info()
    
    def get_user_info(self):
        tag = self.tag
        TRANS_RATE = self.TRANS_RATE
        self.u_principal_up = self.s_user_pp['principal_up'] *1.0 / TRANS_RATE
        self.u_principal_down = self.s_user_pp['principal_down'] *1.0 / TRANS_RATE
        # self.return_thred = self.s_user_pp['return_thred']
        self.other_cost = self.s_user_pp['other_cost'] *1.0 / TRANS_RATE
        self.population = self.s_user_pp['population']
        self.cost_per_day_one = self.s_user_pp['cost_per_day_one'] *1.0 / TRANS_RATE
        self.s_cost = (200 + 100) *1.0 / TRANS_RATE # time cost + transaction fee 

    def cal_in_cost(self, price, Qty, s_cost):
        
        in_cost = price + s_cost * 1.0 / Qty
        return in_cost

    def cal_Qty(self, price,  principal, tag = 1 ):
        """
        tag means which stock market, default is HongKong
        1: HK;  2: US;  3:CHN;  4:SG
        """
        if tag == 1 or 3:
            qty = math.ceil( principal*1.0 / price / 100 ) * 100
        if tag == 2 :
            qty = math.ceil( principal*1.0 / price )
        return qty
    
    def cal_return_required(self, cost_per_day_one, population, other_cost):
        """
        e.g.： return thred is 400HKD, 
        return per year is 400 * (52 weeks * 5 workdays -15 official holiday) = 92000, 
        return per month is 92000/12=7666.6, return per day is 92000/365= 252.05 
        """

        all_cost = cost_per_day_one * population * 365 + other_cost
        s_dayline = 52 * 5 - 15
        return_req = all_cost / s_dayline 
        return return_req, all_cost

    """
    reference for a given stock, if 400 return required, how high is the rate of rise and how many Qty needed?
    Given: stock in price, stock qty, and profit thread
    out: return rate  
    why return thred is 400, return per year is 400 * (52 weeks * 5 workdays -15 official holiday) = 92000, return per month is 92000/12=7666.6, return per day is 92000/365  
    """
    def rise_rate_with_in_out( self, price, Qty, return_thred ):
        # s_Qty = s_principal / s_in_cost 
        # return_thred = self.return_thred
        return_all = return_thred + self.s_cost
        # all_other_cost
        print("all return: %f" % return_all)
        rise_rate = return_all * 1.0 / ( price * Qty )
        # principal = Qty * in_cost
        return rise_rate#, principal

    def return_rate_with_in_out( self, price ):
        tag = self.tag
        # 1. cal return required for the family
        cost_per_day_one = self.cost_per_day_one
        population = self.population
        other_cost = self.other_cost
        return_req, all_cost = self.cal_return_required( cost_per_day_one, population, other_cost)
        print("===== return required: %f, and all year profit: %f=====" % ( return_req, all_cost ) )
        # principal_up = 20000
        # principal_down = 30000
        # 2. cal quantity
        principal_up = self.u_principal_up
        principal_down = self.u_principal_down
        Qty_up = self.cal_Qty( price, principal_up, tag ) - 1 
        Qty_down = self.cal_Qty( price, principal_down, tag ) 
        # Qty = 100
        # print(principal_down,principal_up)
        # print(Qty_up,Qty_down)
        principal_l = []
        rise_rate_l = []
        in_cost_l = []
        qty_l = []
        # get info 
        s_cost = self.s_cost
        for i in range(Qty_down,Qty_up+1):
            Qty = i 
            in_cost = self.cal_in_cost( price, Qty,s_cost )
            rise_rate_i = self.rise_rate_with_in_out( price, Qty, return_req )
            principal_i = Qty * price
            if principal_i >= principal_down and principal_i <= principal_up:
                principal_l.append( Qty * price )
                rise_rate_l.append( rise_rate_i )
                in_cost_l.append(in_cost)
                qty_l.append(Qty)
                break
        return rise_rate_l, principal_l,in_cost_l,qty_l
    
    def check_profit_line(self, out_price, profit_price, peak_price ):
        if out_price <= profit_price and out_price<=peak_price :
            print("JUST DO IT!")
        elif out_price <= profit_price or out_price<=peak_price:
            print("LOOK LOOK!")
        else:
            print("BE CAREFUL!")

    def profit_line(self, stockCode):
        s_profit_rate = 0.1593
        aver_price = 155.2
        support_price = 114.6
        resistance_price = 162.8
        profit_price = support_price + (resistance_price-support_price)* s_profit_rate
        return profit_price

    def draw(self, x, y):
        pass

def main():
    
    # print(stk.s_user_pp)
    tag = 2  # 1: HK;  2: US;  3:CHN;  4:SG
    if tag == 2:
        USD2HKD = 7.77
        trans_rate = USD2HKD        
    if tag == 1:
        trans_rate = 1
    if tag == 3:
        trans_rate = 1.0/0.85

    stk = StockAdvice(tag,trans_rate)
    stkinfo = StockInfo()
    price = 130.2
    peak_price = 135.48
    # 1. buy and sell point
    rise_rate_l, principal_l, in_cost_l, qty_l = stk.return_rate_with_in_out( price )
    profit_price = stk.profit_line('pdd')
    # if tag == 2:  
    print("***** for price: %f ******" % (price) )
    if len(rise_rate_l) == 0:
        print("you should expand your budget!")
    else:
        for i in range(len(rise_rate_l)):
            out = price*(1 + rise_rate_l[i])
            print(" balance price:  %.2f , \n out price: %.2f ,\n purchase Qty: %d ,\n rise rate: %.2f%% ,\n principal: %d" 
            %( in_cost_l[i], out, qty_l[i], rise_rate_l[i]*100, principal_l[i] ) )
            if tag == 2:
                print("USD to HKD: %f" % (principal_l[i]* trans_rate) )
            print("profit line: %f \npeak price now: %f" % (profit_price, peak_price))            
            out_price = out
            stk.check_profit_line(out_price, profit_price, peak_price )
        print("===")


    # 2. whether can buy?
    # 3. estimate  

if __name__ == '__main__':
    main()
    