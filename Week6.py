#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:52:34 2023

@author: manavjatakia
"""

def clean_one(dataset):
    try:
        clean1 = dataset.isna().sum()
        return clean1
    except:
        print("\nWrong Input.")


def clean_two(dataset):
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