"""
A python tool to help create large scale inputs for cs 170 project
@Gabriel Guan
"""
import re
import os

import networkx as nx

import utils

import random


def RcompleteGraph(endV,filePath, startV=0, weight=1):
    with open(filePath,'a') as file:
        for i in range(startV, endV+1):
            for j in range(i+1, endV+1):
                if random.random() >= .8:
                    file.write(str(i) + ' ' + str(j) +' ' + str(round(random.uniform(1,99),3)) +'\n')
        file.close()

def completeGraph(endV,filePath, startV=0, weight=1):
    with open(filePath,'a') as file:
        for i in range(startV, endV+1):
            for j in range(i+1, endV+1):
                file.write(str(i) + ' ' + str(j) +' ' + str(float(weight)) +'\n')
        file.close()

def randomGraph(endV,filePath):
    with open(filePath,'a') as file:
        startV = 0
        List = [i for i in range(startV, endV+1)]
        for i in range(startV, endV+1):
            numNei = random.randint(startV, endV)
            random.shuffle(List)
            for j in range(numNei):
                if i != j:
                    file.write(str(i) + ' ' + str(List[j]) +' ' + str(round(random.uniform(1,99),3)) +'\n')

        file.close()






def completeGraphList(endV,filePath, startV, weight):
    with open(filePath,'a') as file:
        for i in range(startV, endV+1):
            count = 1
            for j in range(i+1, endV+1):
                file.write(str(i) + ' ' + str(j) +' ' + str(float(weight[count])) +'\n')
                count += 1
        file.close()


def circle(endV,filePath, startV=0, weight=1):
    with open(filePath,'a') as file:
        for i in range(startV, endV+1):
            if i == endV:
                file.write(str(startV) + ' ' + str(i) + ' ' + str(float(weight)) + '\n')
            else:
                j = i+1
                file.write(str(i) + ' ' + str(j) + ' ' + str(float(weight)) + '\n')
        file.close()

"""
def Btree(endV,filePath, startV=0, weight=1):
    with open(filePath,'a') as file:
        file.write(str(0) + ' ' + str(1) +' ' + str(float(weight)) +'\n')
        file.write(str(0) + ' ' + str(2) +' ' + str(float(weight)) +'\n')
        ptr1 = 2
        list = [2] + [0 for _ in range(endV - startV)]
        for i in range(startV+1, endV+1):
            if list[i] == 2:
                pass
            file.write(str(i-1) + ' ' + str(i) +' ' + str(float(weight)) +'\n')

            for j in range(i+1, endV+1):
                if j <= endV and not (j in list) :
                    file.write(str(i) + ' ' + str(j) +' ' + str(float(weight)) +'\n')
                list[i] += 1
                if list[i] == 2:
                    break
        file.close()
"""

def Btree(endV,filePath, startV=0, weight=1):
    with open(filePath,'a') as file:
        file.write(str(0)+ ' ' + str(1) +' ' + str(float(weight)) +'\n')
        file.write(str(0)+ ' ' + str(2) +' ' + str(float(weight)) +'\n')
        for i in range(3, endV +1):
            file.write(str(int(i/2))+ ' ' + str(i) +' ' + str(float(weight)) +'\n')
        file.close()



def writeHead(V,filePath):
    with open(filePath,'w') as file:
        file.write(str(V) + '\n')
        file.close()

"""
firstGraph = '100.in'
writeHead(100, firstGraph)
completeGraphList(99,firstGraph,0,range(101))
"""


# Write 25V
firstGraph = '100cc.in'
writeHead(25, firstGraph)
completeGraph(99,firstGraph)

"""
# Write 50V
firstGraph = '50cr.in'
writeHead(50, firstGraph)
completeGraph(49,firstGraph)

# Write 100V
firstGraph = '100cr.in'
writeHead(100, firstGraph)
completeGraph(99,firstGraph)

"""

"""
firstGraph = '25Tree.in'
writeHead(25, firstGraph)
Btree(24,firstGraph)

firstGraph = '50Tree.in'
writeHead(50, firstGraph)
Btree(49,firstGraph)

firstGraph = '100Tree.in'
writeHead(100, firstGraph)
Btree(99,firstGraph)

"""

"""
firstGraph = '25C.in'
writeHead(25, firstGraph)
circle(24,firstGraph)

firstGraph = '50C.in'
writeHead(50, firstGraph)
circle(49,firstGraph)

firstGraph = '100C.in'
writeHead(100, firstGraph)
circle(99,firstGraph)
"""

# Write 25V
firstGraph = '25r.in'
writeHead(25, firstGraph)
randomGraph(24,firstGraph)

# Write 50V
firstGraph = '50r.in'
writeHead(50, firstGraph)
randomGraph(49,firstGraph)

# Write 100V
firstGraph = '100r.in'
writeHead(100, firstGraph)
randomGraph(99,firstGraph)
