# Loading CSV file througt a function 
import csv
import numpy as np
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

def loadCsv(filename):
	file=open(filename,"r")
	i=0
	field=[] #initialization

	#reading from file and storing in field
	for line in file:
		i=i+1
		data=line.strip()
		field.append(data.split(","))
	return field

def CountPosClass(target):
	count=0
	for i in range(len(target)):
		#print target[i],count
		if target[i]==np.unique(target)[0]: count=count+1
	return count

def ProbPosClass(CountPos,target):
	return CountPos/float(len(target))

def CountPosVarClassPos(variable,target):
	count=np.zeros(shape=[5,5])
	#print count
	for j in range(variable.shape[1]):
		uniq_features=np.unique(variable[:,j])
		#print uniq_features 
		k=0	
		for uniq_feature in uniq_features:
			#print k, uniq_feature
			for i in range(variable.shape[0]):
				#print uniq_feature, variable[i][j]
				if (variable[i][j]==uniq_feature and target[i]==np.unique(target)[0]): count[k][j]+=1
			k+=1	
	
	return count


filename = 'Flying_Fitness.csv'
dataset = loadCsv(filename)


# Seperate Target and Variables array
target=[]

for i in range(1,(len(dataset))):
	target.append(dataset[i][1])

variable2=np.array(dataset)
variable1=np.delete(variable2,0,0)
variable=np.delete(variable1,np.s_[:2],1)

#calculate counts and Porb
CountPos=CountPosClass(target)
ProbPos=ProbPosClass(CountPos,target)

CountPosVar=CountPosVarClassPos(variable,target)
ProbPosVar=CountPosVar/CountPos

#print ProbPosVar
#print ProbNegVar

uniq_features=[]
for j in range(variable.shape[1]):
	uniq_features.append(np.unique(variable[:,j]))
#print uniq_features[2][0]

#calculate Predictor for each obs 
def PredicClass(variable,uniq_features,ProbPosVar,threhold):
	prediction=[]
	Pos=1
	for j in range(variable.shape[1]):
		for i in range(variable.shape[0]):
			k=len(uniq_features[j])-1
			for m in range(k):
				if variable[i][j]==uniq_features[j][m]:
					Pos=ProbPosVar[m][j]*Pos
				#print i,j,k, variable[i][j], uniq_features[j][k], ProbPosVar[k][j], ProbNegVar[k][j], Pos, Neg		
			if Pos>threshold: prediction.append(1) 
			else: prediction.append(0)
	return prediction

#Calculate TPR FPR for threshold
TPRs=[]
FPRs=[]
TP = 0 
FN = 0 
FP = 0 
TN = 0
thresholds = np.linspace(0.00, 1, num=20)
TP = 0 
FN = 0 
FP = 0 
TN = 0
for threshold in thresholds:
	prediction=PredicClass(variable,uniq_features,ProbPosVar,threshold)
	for i in range (len(target)):
		#print target[i],prediction[i]
		if (target[i] == np.unique(target)[1] and prediction[i]== 0):TP+=1
		elif (target[i] == np.unique(target)[1] and prediction[i]== 1):FN+=1
		elif (target[i] == np.unique(target)[0] and prediction[i]== 0):FP+=1
		elif (target[i] == np.unique(target)[0] and prediction[i]== 1):TN+=1
	#print threshold, TP, FN, FP, TN, np.unique(target)[0]
	TPRs.append(float(TP)/float(TP+FN))
	FPRs.append(float(FP)/float(FP+TN))
	#print TPRs,FPRs

#draw random line
x = [0.0, 1.0]
plt.plot(x, x, label='random')
#draw ROC
plt.plot(FPRs, TPRs, color='blue', linewidth=2, label='ROC')
plt.show()

