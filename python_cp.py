import numpy as np

with open("Loan.csv", "r") as file:
    D= file.read()
    #print(D)

D= np.genfromtxt("loan.csv",delimiter=",", usecols=8, filling_values=0)

Loan= np.array(D)

mean= np.mean(Loan)
print(mean)
median = np.median(Loan)
print(median)
standard_d = np.std(Loan)
print(standard_d)
maximum=np.max(Loan)
print(maximum)
minimum=np.min(Loan)
print(minimum)
varience = np.var(Loan)
print(varience)