from sklearn.preprocessing import MinMaxScaler
d = 0.5
p = 10
r = 1
scaler = MinMaxScaler()
data1=[]
data=[]

data.append(d)
data.append(p)
data.append(r)
print(data)
data1.append(data)
scaler.fit(data1)
data1 = scaler.transform(data1)
print(data1)
x = (0.55*data[0][0])+(0.1*data[0][1])+(0.35*data[0][2])
print(x)