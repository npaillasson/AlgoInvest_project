#! /usr/bin/env python3
# coding: utf-8

max_invest = 500

invest = 0
choice_list = []
total_invest = 0
total_earn = 0
potential_lists = []
record_list = []
record_invest = 0


input_list = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
    ["Action-4", 70, 20],
    ["Action-5", 60, 17],
    ["Action-6", 80, 25],
    ["Action-7", 22, 7],
    ["Action-8", 26, 11],
    ["Action-9", 48, 13],
    ["Action-10", 34, 27],
    ["Action-11", 42, 17],
    ["Action-12", 110, 9],
    ["Action-13", 38, 23],
    ["Action-14", 14, 1],
    ["Action-15", 18, 3],
    ["Action-16", 8, 8],
    ["Action-17", 4, 12],
    ["Action-18", 10, 14],
    ["Action-19", 24, 21],
    ["Action-20", 114, 18]
]

#input_list = [
#    ["Action-1", 20, 5],
#    ["Action-2", 30, 10],
#    ["Action-3", 50, 15],
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
#]

print(len(input_list))



def bruteforce(potential_lists, total_invest, working_list=input_list,
               length=1, record_invest=record_invest, record_list=record_list):

    if length <= len(working_list):
        for index, element in enumerate(working_list):
            #print("total invest", total_invest, "element", element[2])
            current_value = total_invest + element[2]
            if current_value <= max_invest:
                if current_value > record_invest:
                    record_invest = current_value
                    record_list = potential_lists + element
            #print(potential_lists)
            next_list = list(working_list)
            del next_list[index]
            #print("next", next_list)
            bruteforce(potential_lists + element, total_invest=current_value,
                       length=length + 1, working_list=next_list)

    return (record_invest, record_list)

for value in input_list:
    value[2] = ((value[1] * value[2]) / 100)

test = bruteforce(potential_lists, total_invest, working_list=input_list)

print(test)
print("somme investie: ", total_invest)
print("somme gagnée: ", total_earn)
#print("pourcentage gain: ", ((100 * total_earn) / total_invest))