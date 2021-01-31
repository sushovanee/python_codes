#!/usr/bin/env python

import os
import subprocess
import re
import shutil

# Network latency
"""
Here we will ping google at an interval of five seconds for five times and record the
min response time, average response time, and the max response time. 
"""
ping_result = subprocess.run(['ping', '-i 5', '-c 5', 'google.com'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')

min, avg, max = ping_result[-2].split('=')[-1].split('/')[:3]
statistics['network_latency'] = dict(
    {
        'min': min.strip(),
        'avg': avg.strip(),
        'max': max.strip(),
    }
)