#! /usr/bin/env python3
# coding: utf-8

max_invest = 500

invest = 0
choice_list = []
total_invest = 0
total_win = 0
potential_lists = []
record_list = []
record_invest = 0
record_win = 0

input_list = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
#    ["Action-4", 70, 20],
#    ["Action-5", 60, 17],
#    ["Action-6", 80, 25],
#    ["Action-7", 22, 7],
#    ["Action-8", 26, 11],
#    ["Action-9", 48, 13],
#    ["Action-10", 34, 27],
#    ["Action-11", 42, 17],
#    ["Action-12", 110, 9],
#    ["Action-13", 38, 23],
#    ["Action-14", 14, 1],
#    ["Action-15", 18, 3],
#    ["Action-16", 8, 8],
#    ["Action-17", 4, 12],
#    ["Action-18", 10, 14],
#    ["Action-19", 24, 21],
#    ["Action-20", 114, 18]
]


print(len(input_list))



def bruteforce(potential_lists, total_invest, total_win=total_win , working_list=input_list,
               length=1, record_invest=record_invest, record_list=record_list,
               record_win=record_win):

    if length <= len(working_list):
        for index, element in enumerate(working_list):
            #print("total invest", total_invest, "element", element[2])
            current_invest_value = total_invest + element[1]
            current_win_value = total_win + element[2]
            potential_lists += element
            if current_invest_value <= max_invest:
                if current_win_value > record_win:
                    record_win = current_win_value
                    record_invest = current_invest_value
                    record_list = potential_lists
            #print(potential_lists)
            next_list = list(working_list)
            del next_list[index]
            #print("next", next_list)
            bruteforce(potential_lists + element, total_win=current_win_value,
                       total_invest=current_invest_value, length=length + 1, working_list=next_list,
                       record_list=record_list, record_win=record_win, record_invest=record_invest)

    return (record_invest, record_list, record_win)

for value in input_list:
    value[2] = ((value[1] * value[2]) / 100)

test = bruteforce(potential_lists, total_invest, working_list=input_list)

print(test)
#print("pourcentage gain: ", ((100 * total_earn) / total_invest))


from typing import List

MAX_INVEST = 500
input_list = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
]


class Action:
    def __init__(self, name: str, cost: float, percentage: float):
        self.name = name
        self.cost = cost
        self.percentage = percentage
        self.benefit = self.cost * self.percent / 100


class Combinaison:
    def __init__(self, actions: List[Actions]):
        self.actions = actions
        self.benefit = sum([action.benefit for action in list_actions])
        self.cost = sum([action.cost for action in actions])


def make_combinaisons(number: int, actions: List[Action]) -> List[Combinaison]:
    combinaisons = []
    #  code here :)
    return [comb for comb in combinaisons if comb.cost <= MAX_INVEST]


def main():
    actions = [Action(input[0], input[1], input[2]) for input in input_list]

    current_best_combinaison = None

    for number in range(len(actions)):
        number = number + 1
        combinaisons = make_conbinaisons(number, actions)
        for combinaison in combinaisons:
            if current_best_combinaison and current_best_combinaison.benefit < combinaison.benefit:
                current_best_combinaison = combinaison


main()