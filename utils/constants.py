#!/usr/bin/env python
# encoding: utf-8
"""
Constants

"""
import re
import glob

# file root path
BASE_FOLDER = "./row_data"

# date
START_DATE = '2019-04-01'
END_DATE = '2019-04-04'

# get list of city
CITY_ANTWERP = 'ANTWERP'
GET_CITIES = [re.search(r".*/([A-Z]+)", s).group(1)
              for s in glob.glob(f"{BASE_FOLDER}/*/")]


# column name of channels
CHANNELS = [(0, 'volume_NE'), (1, 'speed_NE'), (2, 'volume_NW'), (3, 'speed_NW'),
            (4, 'volume_SE'), (5, 'speed_SE'), (6, 'volume_SW'), (7, 'speed_SW'), (8, 'incidents')]
VOLUMECHANNELSELS = [(0, 'volume_NE'), (2, 'volume_NW'),
                     (4, 'volume_SE'), (6, 'volume_SW')]

# overpass parameters
ADMIN_LEVELS = [8, 10]
ADMIN_LEVEL_9 = 9
ADMIN_LEVEL_8 = 8
ADMIN_LEVEL_10 = 10

# 



