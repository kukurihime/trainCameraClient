#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:41:39 2020

@author: kukurihime
"""
import paho.mqtt.client as mqtt
import time

import CTrainStatus

class CTrainCameraMQTTPub:
    def __init__(self, ts):
        self.ts = ts
        if self.ts.getSystemMode() == 'dummy':
            self.host = '127.0.0.1'
        else:
            self.host = '192.168.11.71'
            
        self.port = 1883
        self.topic = 'trainCamera/command'
        self.keepalive = 60
        
        self.client = mqtt.Client(protocol = mqtt.MQTTv311)
        
    def connect(self):
        self.client.connect(self.host, port = self.port, keepalive = self.keepalive)
        
    def disconnect(self):
        self.client.disconnect()
    
    def sendCommand(self, command):
        self.client.publish(self.topic, command)    
    

            
            