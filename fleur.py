import math

matriceConf = [[0,0,0],[0,0,0],[0,0,0]]
fleur = []
test = []
apprentissage = []

def Main():
    f=open(r"C:\Users\rpaup\Documents\GitHub\DataScience-IA\IA3-ml_data_iris.txt",'r')
    CreateList(f)
    k = DefK()
    print(f"{k} is the most optimal number of neighbour to take for the KNN function")

def KNN(flower, k):
    nearN=[]
    for i in apprentissage:
        distance=math.sqrt((flower['sl']-i['sl'])**2+(flower['sw']-i['sw'])**2+(flower['pl']-i['pl'])**2+(flower['pw']-i['pw'])**2)
        nearN.append(dict(distance=distance, cl=i['cl']))
    nearN=sorted(nearN, key=lambda x: x['distance'])
    countFlower = dict()
    for i in range(0,k):
        if nearN[i]['cl'] in countFlower :
              countFlower[nearN[i]['cl']] += 1
        else :
            countFlower[nearN[i]['cl']] = 1
    return max(countFlower, key=countFlower.get)

def CreateList(f):
    for item in f:
        item = item.replace('\n', '')
        data = item.split(',')
        fleur.append(dict(sl=float(data[0]), sw=float(data[1]), pl=float(data[2]), pw=float(data[3]), cl=data[4]))
        print(fleur)
    listSize = len(fleur)/3
    print(listSize)

    for i in range(0, int(listSize*0.2)) :
        apprentissage.append(fleur[i])
        apprentissage.append(fleur[int(listSize + i)])
        apprentissage.append(fleur[int(listSize*2 + i)])
    
    for i in range(int(listSize*0.2), int(listSize)):
        test.append(fleur[i])
        test.append(fleur[int(listSize + i)])
        test.append(fleur[int(listSize*2 + i)])

def FillMatriceConf(s,v):
    x=0
    y=0
    match s:
        case 'Iris-virginica':
            x=2
        case 'Iris-versicolor':
            x=1
        case  'Iris-setosa':
            x=0

    match v:
        case 'Iris-virginica':
            y=2
        case 'Iris-versicolor':
            y=1
        case  'Iris-setosa':
            y=0
    matriceConf[x][y]+=1

def DefK():
    listError=dict()
    for k in range(1,31):
        for f in test :
            FillMatriceConf(KNN(f, k), f['cl'])
        listError[k] = countMatriceConf()
    print(listError)
    return min(listError, key=listError.get)

def countMatriceConf():
    global matriceConf
    nbError = matriceConf[0][1] + matriceConf[0][2] + matriceConf[1][0] + matriceConf[1][2] + matriceConf[2][0] + matriceConf[2][1] 
    matriceConf = [[0,0,0],[0,0,0],[0,0,0]]
    return nbError

Main()