#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np


class QTable(object):

    def __init__(self):
        self.table = np.array((6, 2))


class Qlearning(object):

    def __init__(self):
        self.action_list = [-1, 1]

    def choice_next(self, q_table, state):



        i_state = np.random.random()
        if i_state < 0.2:
            action = np.random.choice([0, 1])
        else:
            action = np.argmax(q_table[state])



        return self.action_list[action]



    def run(self):


        epoch = 100
        max_iter = 100
        q_table = np.random.random((6, 2))
        alpha = 0.1
        gamma = 0.1
        for e in range(epoch):

            i = 0
            state = 0
            while state != 6 and i < max_iter:
                action = self.choice_next(q_table, state)

                if state == 0 and action < 0:
                    action = 0
                state_ = state + action
                r = 0
                if state_ == 6:
                    q_target = 1
                else:
                    q_target = r + gamma * q_table[state_].max()

                loc = 1 if action>0 else 0
                q_predict = q_table[state][loc]

                update_value = alpha*(q_target-q_predict)

                q_table[state][loc] += update_value

                state = state_
                i += 1
            print(i)

        return q_table


if __name__ == "__main__":
    ql = Qlearning()
    print(ql.run())
