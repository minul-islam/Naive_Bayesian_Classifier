# Loading CSV file througt a function 
import csv
import sqlite3
import numpy as np
conn=sqlite3.connect('PilotFitness.db')
c=conn.cursor()
from collections import Counter, defaultdict

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

filename = 'Flying_Fitness.csv'
dataset = loadCsv(filename)

c.execute('CREATE TABLE flying_fitness( Target INTEGER, Attribute1 INTEGER,Attribute2 INTEGER,Attribute3 INTEGER,Attribute4 INTEGER,Attribute5 INTEGER,Attribute6 INTEGER)') 

for row in dataset:
	print tuple(row)
	c.execute('INSERT INTO flying_fitness VALUES(?,?,?,?,?,?,?)', tuple(row))
	
c.execute('SELECT * from flying_fitness')
print c.fetchall()

conn.commit()
conn.close()

