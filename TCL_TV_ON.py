# TinyTuya Example
# -*- coding: utf-8 -*-
"""
 TinyTuya - Tuya Cloud IR Functions

 This example uses the Tinytuya Cloud class and functions
 to send IR blaster commands

 Author: uzlonewolf
 For more information see https://github.com/jasonacox/tinytuya

""" 
import os
import tinytuya
import colorsys
import time
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def tv_toggle():
    
  tinytuya.set_debug()

  # Set this to the actual blaster device, not a virtual remote
  device_id = os.environ['TUYA_IR_DEVICE_ID']
  
  # Connect to Tuya Cloud - uses tinytuya.json
  c = tinytuya.Cloud()
  
  
  
  
  
  # Keys from a virtual remote can also be sent
  #
  # See https://developer.tuya.com/en/docs/cloud/ir-control-hub-open-service?id=Kb3oe2mk8ya72
  #   for API documentation
  
  remote_id = os.environ['TUYA_IR_REMOTE_ID']
  
  
  # Finally, send the 'Power' key
  post_data = {
      "key": "Power", #"power",
      "category_id": '2',
      "remote_index": '1512'
  }
  print('Send key result:')
  res = c.cloudrequest( '/v2.0/infrareds/%s/remotes/%s/command' % (device_id, remote_id), post=post_data )
  print( json.dumps(res, indent=2) )
  
  
  
  # The actual value sent by the above key can be found by checking the device logs
  print('Device logs:')
  logs = c.getdevicelog(device_id, evtype='5', size=3, max_fetches=1)
  print( json.dumps(logs, indent=2) )
