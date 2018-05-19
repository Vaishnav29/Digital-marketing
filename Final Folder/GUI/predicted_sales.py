import pandas as pd
import numpy as np
import pickle
inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
inv_monsoldper_name = pickle.load(open("inv_monsoldper_name.p", "rb"))
l = pickle.load(open("l.p", "rb"))
lis_inv = pickle.load(open("lis_inv.p", "rb"))
lis_inv_sold_per = pickle.load(open("lis_inv_sold_per.p", "rb"))

def predicted_sales(year,mon,pname):
    lis = [0,0,0]
    count = year - 2014
    diction = ((year-2014)*12+mon)-1
    
    for i in range(3):
        try:
            li = lis_inv_sold_per[inv_monsoldper_name[diction-1-i]][pname][1]
        except:
            li = 0
            pass
        lis[i] = li
    while(count!=0):
        for i in range(4):
            try:
                li = lis_inv_sold_per[inv_monsoldper_name[diction-12-i]][pname][1]
            except:
                li = 0
                pass
            lis.append(li)
                
        diction-=12
        count -=1
    return lis
