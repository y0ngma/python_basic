from matplotlib import pyplot as plt

X = [-5,5,5,-5]
Y = [1,1,-1,-1]
X_new=[]
for i in X:
    X_new.append(i*2)

X.append(X[0])
X_new.append(X_new[0])
Y.append(Y[0])

Y_new=[]
for i in Y:
    Y_new.append(i*2)

X.append(X[0])
X_new.append(X_new[0])
Y.append(Y[0])
Y_new.append(Y_new[0])



axes = plt.gca()
axes.set_xlim([-20,20])
axes.set_ylim([-5,5])
plt.plot(X,Y)
plt.show()
plt.plot(X_new, Y_new)
plt.show()


