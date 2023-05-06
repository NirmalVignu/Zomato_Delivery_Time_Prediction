## End to End ML Project on Zomato Delivery Time Prediction

### created an environment
```
conda create -p venv python==3.8

conda activate venv/
```
### Install all the neccessary libraries
```
pip install -r requirements.txt
```
### Model Report

```
Model Name	         R2_Score
LinearRegression	 0.5043255791789477
Lasso	             0.4287658503279863
Ridge	             0.5043254023788882
Elasticnet	         0.42359160220793335
DecisionTreeRegressor0.49928105822682345
SVR                  0.5825173935671815


Best Model:SVR (Support Vector Regressor)
R2_Score:0.5825173935671815
```
```
The models giving very less score as so there is need to do hyper parameter tuning for which i will update this repo further in upcoming days
```