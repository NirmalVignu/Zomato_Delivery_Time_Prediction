from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
from src.pipeline.training_pipeline import train_model


app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('form.html')
    else:
        data=CustomData(
                    Delivery_person_ID=request.form.get('Delivery_person_ID'),
                    Delivery_person_Age=float(request.form.get('Delivery_person_Age')),
                    Delivery_person_Ratings=float(request.form.get('Delivery_person_Ratings')),
                    Restaurant_latitude=float(request.form.get('Restaurant_latitude')),
                    Restaurant_longitude=float(request.form.get('Restaurant_longitude')),
                    Delivery_location_latitude=float(request.form.get('Delivery_location_latitude')),
                    Delivery_location_longitude=float(request.form.get('Delivery_location_longitude')),
                    Weather_conditions=request.form.get('Weather_conditions'),
                    Road_traffic_density=request.form.get('Road_traffic_density'),
                    Vehicle_condition=int(request.form.get('Vehicle_condition')),
                    Type_of_order=request.form.get('Type_of_order'),
                    Type_of_vehicle=request.form.get('Type_of_vehicle'),
                    multiple_deliveries=float(request.form.get('multiple_deliveries')),
                    Festival=request.form.get('festival'),
                    City=request.form.get('city'),
                    Order_Date_Year=int(request.form.get('order_date_year')),
                    Order_Date_Month=int(request.form.get('order_date_month')),
                    Order_Date_Day=int(request.form.get('order_date_day')),
                    Time_Orderd_hrs=int(request.form.get('time_ordered_hrs')),
                    Time_Orderd_min=int(request.form.get('time_ordered_min')),
                    Time_Order_picked_hrs=int(request.form.get('time_picked_hrs')),
                    Time_Order_picked_min=int(request.form.get('time_picked_min')),
)
        final_new_data=data.get_data_as_dataframe()
        if None in final_new_data.values:
            print('None values found in data')
            print(final_new_data.values)
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)


@app.route('/model_train',methods=['GET','POST'])
def model_train():
    
    report=train_model()
    best_model_score = max(sorted(report.values()))

    best_model_name = list(report.keys())[list(report.values()).index(best_model_score)]
    final={'report':report,'best_model_name':best_model_name,'best_model_score':best_model_score}
    return render_template('train_model.html',final=final)
    

# @app.route('/predict',methods=['GET','POST'])
# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('form.html')
#     else:
#         data=CustomData(
#             carat=float(request.form.get('carat')),
#             depth = float(request.form.get('depth')),
#             table = float(request.form.get('table')),
#             x = float(request.form.get('x')),
#             y = float(request.form.get('y')),
#             z = float(request.form.get('z')),
#             cut = request.form.get('cut'),
#             color= request.form.get('color'),
#             clarity = request.form.get('clarity')
#         )
#         final_new_data=data.get_data_as_dataframe()
#         predict_pipeline=PredictPipeline()
#         pred=predict_pipeline.predict(final_new_data)

#         results=round(pred[0],2)

#         return render_template('results.html',final_result=results)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
