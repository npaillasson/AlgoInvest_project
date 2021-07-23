#! /usr/bin/env python3
# coding: utf-8

def display_results(choice_list, total_invest, total_earn, gain_rate):

    print(choice_list)
    print("amount invested: ", round(total_invest, 2), "€")
    print("amount earned: ", round(total_earn, 2), "€")
    print("gain rate: ", round(gain_rate, 2), "%")
