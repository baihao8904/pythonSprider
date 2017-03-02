#-*- coding:utf-8 -*-
from math import sqrt

def MakeDict(path = "./heros.txt"):
    file = open(path,'r',encoding='utf-8')
    heros = {}
    for line in file.readlines():
        heros.setdefault(line.split("\t")[2],{})
        for i in range(len(line.split("\t")[4].split(","))):
            heros[line.split("\t")[2]][line.split("\t")[4].split(",")[i].split("：")[0]]=\
                float(line.split("\t")[4].split(",")[i].split("：")[1].strip())
    return heros

def sim_distance(DictData,hero1,hero2):
    same_item = {}
    for item in DictData[hero1]:
        if item in DictData[hero2]:
            same_item[item]=1
    sum_of_squares = sum([pow(DictData[hero1][item]-DictData[hero2][item],2) for item in same_item.keys()])
    return 1/(1+sqrt(sum_of_squares))

def topMatchs(DictData,hero,n=5,sim_fun=sim_distance):
    scores = [(sim_fun(DictData,hero,other),other) for other in DictData if other!=hero]
    scores.sort(reverse=True)
    return scores[0:n]

if __name__ == '__main__':
    while True:
        hero = input("please input a hero name or exit:")
        if hero=="exit":
            break
        try:
            hero = str(hero)
            heroData = MakeDict()
            print(topMatchs(heroData,hero,n=3))
        except:
            print('no this hero')