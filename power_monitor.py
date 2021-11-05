# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:00:00 2021

@author: Sr Main
"""


from pythonping import ping
devices = {"Sr_Blue_laser": 
               {"IP": "192.168.0.147",
                "Status": False},
           "Sr_Moglabs":
               {"IP": "192.168.0.240",
                "Status": False},
           "Sr_Red_laser":
               {"IP": "192.168.0.244",
                "Status": False},
           "Li_PC":
               {"IP": "172.28.171.6",
                "Status": False}}
for device in devices:
    try:
        response = ping(devices[device]["IP"], verbose=True)
        print(len(response._responses[0].message.packet.packet))
        devices[device]["Status"] = True
    except:
        print(device,"is not connected")
