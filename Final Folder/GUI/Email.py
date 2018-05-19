# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:02:39 2018

@author: user
"""

import smtplib
 
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
# Authentication
s.login("musicmetalmania@gmail.com","musicmetalmania123")
 
# message to be sent
message = "Digital Marketing Welcomes you to our World"
 
# sending the mail
s.sendmail("musicmetalmania@gmail.com", "bhavanatangirala25@gmail.com", message)
 
# terminating the session
s.quit()