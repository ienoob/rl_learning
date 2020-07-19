#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Time : 2020/7/19 17:13
    @Author  : jack.li
    @Site    : 
    @File    : rl_brain.py

"""
import numpy as np
import pandas as pd


class QLearningTable(object):


    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.learning_rate = learning_rate
