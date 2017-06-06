# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import pandas as pd

df_train=pd.read_csv('/home/licheng/')

df_test=pd.read_csv('/home/licheng/')

df_test_negative=df_test.loc[df_test['Type'] == 0][['Clump Thickness','Cell Size']]

df_test_positive=df_test.loc[df_test['Type'] == 1][['Clump Thickness','Cell Size']]

import matp