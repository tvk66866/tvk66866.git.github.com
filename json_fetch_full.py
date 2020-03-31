#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from flask_cors import CORS
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='pyml')

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json(force=True)
	# print(request.status_code)
	result = '77.8'
	print(data)
	# for item in data:
	# 	# loop over every row
	# 	result = item['blood_pressure']
	# print(result)	

	obs_data = pd.read_excel('fhir_Observation_data.xlsx')
	obs_transform = obs_data.pivot_table(values = 'obs_value', index = 'patient_name', columns='obs_name',aggfunc='mean',)
	obs_transform.columns = obs_transform.columns.str.replace('.','_').str.replace("/","_")
	select_col = obs_transform.notnull().sum().sort_values(ascending=False)[0:11].index
	
	select_obs = obs_transform[select_col]
	model = XGBClassifier()
	X = select_obs.drop(['Body Weight','Body Mass Index'], axis=1)
	y = select_obs['Body Weight']
	y.replace(np.NaN,y.mean(),inplace=True)
	model.fit(X, y)
	prod_ds = pd.DataFrame(data)
	prod_col = prod_ds.columns
	for col in prod_col:
   	    prod_ds[col] = prod_ds[col].astype(float)
	y_pred = model.predict(prod_ds)

	return str(round(y_pred[0],2))



if __name__ == '__main__':
	# run!
	app.run()