# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:09:28 2018

@author: user
"""
import pickle 

pickle.dump(inv_mon_name, open("inv_mon_name.p", "wb"))
pickle.dump(inv_monsoldper_name, open("inv_monsoldper_name.p", "wb"))
pickle.dump(l, open("l.p", "wb"))
pickle.dump(lis_inv, open("lis_inv.p", "wb"))
pickle.dump(lis_inv_sold_per, open("lis_inv_sold_per.p", "wb"))

inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
inv_monsoldper_name = pickle.load(open("inv_monsoldper_name.p", "rb"))
l = pickle.load(open("l.p", "rb"))
lis_inv = pickle.load(open("lis_inv.p", "rb"))
lis_inv_sold_per = pickle.load(open("lis_inv_sold_per.p", "rb"))



pickle.dump(data, open("4yrsBMW.p", "wb"))
data= pickle.load(open("4yrsBMW.p", "rb"))