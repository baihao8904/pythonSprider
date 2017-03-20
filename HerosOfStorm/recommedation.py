from math import sqrt

def MakeDict(path = "./heroAvility.txt"):
    file = open(path,'r')
    heros = {}
    for line in file.readlines():
        heros.setdefault(line.split("\t")[0],{})
        for i in range(2,6):
            if  len(line.split("\t")[i].split(":"))>len(line.split("\t")[i].split("：")):
                heros[line.split("\t")[0]][line.split("\t")[i].split(":")[0]]=\
                    float(line.split("\t")[i].split(":")[1])
            else:
                heros[line.split("\t")[0]][line.split("\t")[i].split("：")[0]] = \
                    float(line.split("\t")[i].split("：")[1])
    return heros

def sim_distance(dictData,hero1,hero2):
    same_item = {}
    for item in dictData[hero1]:
        if item in dictData[hero2]:
            same_item[item]=1
    sum_of_squares = sum([pow(dictData[hero1][item]-dictData[hero2][item] \
                    ,2) for item in same_item.keys()])
    return sum_of_squares

def topMatchs(dictData,hero,n=5,simfun=sim_distance):
    scores = [(simfun(dictData,hero,other),other,dictData[other]) for other in dictData if other!=hero]
    scores.sort(reverse=False)
    return scores[0:n]

if __name__ == '__main__':
    herolist = []
    _file = open('./heroAvility.txt', 'r')
    for line in _file.readlines():
        herolist.append(line.split('\t')[0])
    print('英雄列表：')
    for i in range(len(herolist)//15):
        print(' '.join(herolist[i*15:i*15+15]))
    print(' '.join(herolist[len(herolist)//15*15:]))
    heroData = MakeDict()
    while True:
        theHero = input('输入英雄名字,输入exit退出：')
        if theHero=='exit':
            break
        try:
            hero = str(theHero)
            for item in topMatchs(heroData,theHero,n=3):
                print(item)
        except:
            print('没有这个英雄')

