import operator

print('- ' * 50)
score_dict = {'김자바':[40,80], '이합격':[80,77], '박이썬':[95,87], '고길동':[82,34]}


tot = 0
for i, (key,data) in enumerate(score_dict.items()):
    for a in range(0,2,1):
        tot += score_dict[key][a]
    print(i,key, data[0], data[1], 'Total:',tot )
    tot = 0 #반드시 초기화작업


print('- ' * 50 )
print()
def myHap(data):                            
    for i,j in data.items():
        hap = 0                             
        for k in j:                         
            hap = hap+k                       
        j.append(hap)                       
    return data


def myAvg(d):                            
    for i, j in score_dict.items():
        avg = 0                             
        for k in j:
            avg = round(j[2]/2, 2)         
        j.append(avg)                       
    return d


def myRank(data):   
    for i, j in data.items():
        j.append(1)                         
        for v in data.values():
            if j[3] < v[3]:
