# AlgoInvest_project

***

This project is entirely coded in python 3.

This project is realized in the framework of a training on [OpenClassrooms](https://openclassrooms.com/fr/).
This project allows you to retrieve a list of the best stocks to invest in to maximize your profit after two years.


## Table of contents
1. [General information](#general-information)
3. [Installation/usage](#installation)

***

## General Information

This project has two algorithms to calculate the list of best actions.

* the **bruteforce** algorithm : which calculates all the possibilities and keeps the best (can take a long time)
* the **optimized** algorithm: which sorts stocks according to their gain/cost ratios

The proposed list of actions must meet three constraints:

1. each share can be purchased only once
2. Impossible to buy a fraction of a share
3. Do not spend more than a certain investment amount (by default 500 euros)


To use this program you need to provide a CSV file containing the list of all actions to be analyzed.

example of csv format (with coma as separator)

header => share-name,cost (€),benefit after two years (%)

data => example-share,13,2

## Installation

To use this script you need a bash Terminal.

To get this project on your computer you can clone it:
```
$ git clone https://github.com/npaillasson/AlgoInvest_project
```
To execute the script simply use:
```
$ python3 algoinvest.py --file [path to your csv file]
```
by default the algorithm used is the optimized one, however it is possible to launch the bruteforce script instead with
```
$ python3 algoinvest.py --file [path to your csv file] --bruteforce
```
by default the maximum investment amount is 500€, but it is possible to change it with 
```
$ python3 algoinvest.py --file [path to your csv file] --max-invest [your new max amount]
```
the program cleans the input data:
* If an action appears twice, only the first occurrence is kept.
* If a share has a price less than or equal to 0, the share will be ignored
* If a share has a profit percentage less than or equal to 0, the share will be ignored

by default the user is not warned to improve the readability. However to make these errors appear, just use
```
$ python3 algoinvest.py --file [path to your csv file] --verbose
```
To get help use
```
$ python3 algoinvest.py --help
```