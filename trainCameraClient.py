#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:38:39 2020

@author: kukurihime
"""

import CTrainCameraClient
import time
import sys
print('trainCameraClient Start!')
time.sleep(0.5)

argv = sys.argv
if len( argv ) == 1:
    argv.append("real") 

tcc = CTrainCameraClient.CTrainCameraClient(argv)
tcc.main()

print('trainCameraClient Finished!')



