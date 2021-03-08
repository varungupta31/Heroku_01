# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:24:32 2021

@author: varun
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())