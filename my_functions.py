#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:36:33 2024

@author: manavjatakia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:52:34 2023

@author: manavjatakia
"""

def null_values(dataset):
    try:
        clean1 = dataset.isna().sum()
        return clean1
    except:
        print("\nWrong Input.")


def column_rename(dataset):
    try:
        clean2 = dataset.columns.str.replace(' ', '_').str.lower()
        return clean2
    except:
        print("\nWrong Input")


def descriptive(dataset):
    try:
        desc = print(dataset.describe())
        return desc
    except:
        print("\nWrong Input")