#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:39:32 2020

@author: kukurihime
"""

import CTrainCameraMQTTPub
import CTrainStatus
import CTrainCameraView
import CRealtimeKeyInput
import time

class CTrainCameraClient:
    def __init__(self, argv):
        self.ts = CTrainStatus.CTrainStatus(argv)
        self.tcmp = CTrainCameraMQTTPub.CTrainCameraMQTTPub(self.ts)
        self.tcv = CTrainCameraView.CTrainCameraView(self.ts)
        
        self.tcv.start()
        
        self.rki = CRealtimeKeyInput.CRealtimeKeyInput()
        self.rki.setDaemon(True)
        self.rki.start()
        
        self.tcmp.connect()
        
    def main(self):
        
        key = ''
        while not key == 'q':
            if self.rki.hasNewKey():
                key = self.rki.getKey()
                self.ts.setCommand(key)
                self.tcmp.sendCommand(key)
                
            time.sleep(0.1)
        
        self.tcv.join()
        self.rki.stop()
        time.sleep(3)
        
        self.tcmp.disconnect()
        