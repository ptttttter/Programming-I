maya_dict={'pop':1,'no':2,'zip':3,'zotz':4,'tzec':5,'xul':6,'yoxkin':7,'mol':8,'chen':9,'yax':10,'zac':11,'ceh':12,'mac':13,'kankin':14,'muan':15,'pax':16,'koyab':17,'cumhu':18,'uayet':19}
tzolkin_list=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
n=int(input());print(n)
for _ in range(0,n):
    d,m,y=input().split()
    date=int(y)*365+(maya_dict[m]-1)*20+int(d[:-1])
    print(date%13+1,tzolkin_list[date%20],date//260)