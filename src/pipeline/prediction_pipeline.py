import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                Delivery_person_ID:str,
                Delivery_person_Age:float,
                Delivery_person_Ratings:float,
                Restaurant_latitude:float,
                Restaurant_longitude:float,
                Delivery_location_latitude:float,
                Delivery_location_longitude:float,
                Weather_conditions:str,
                Road_traffic_density:str, 
                Vehicle_condition:int,  
                Type_of_order:str, 
                Type_of_vehicle:str, 
                multiple_deliveries:float,
                Festival:str, 
                City:str, 
                Order_Date_Year:int,  
                Order_Date_Month:int,  
                Order_Date_Day:int,  
                Time_Orderd_hrs:int,  
                Time_Orderd_min:int,  
                Time_Order_picked_hrs:int,  
                Time_Order_picked_min:int):
        self.Delivery_person_ID=Delivery_person_ID
        self.Delivery_person_Age=Delivery_person_Age
        self.Delivery_person_Ratings=Delivery_person_Ratings
        self.Restaurant_latitude=Restaurant_latitude
        self.Restaurant_longitude=Restaurant_longitude
        self.Delivery_location_latitude=Delivery_location_latitude
        self.Delivery_location_longitude=Delivery_location_longitude
        self.Weather_conditions=Weather_conditions
        self.Road_traffic_density= Road_traffic_density
        self.Vehicle_condition= Vehicle_condition
        self.Type_of_order= Type_of_order
        self.Type_of_vehicle= Type_of_vehicle
        self.multiple_deliveries=multiple_deliveries
        self.Festival= Festival
        self.City= City
        self.Order_Date_Year=  Order_Date_Year
        self.Order_Date_Month= Order_Date_Month 
        self.Order_Date_Day=  Order_Date_Day
        self.Time_Orderd_hrs=  Time_Orderd_hrs
        self.Time_Orderd_min=  Time_Orderd_min
        self.Time_Order_picked_hrs=  Time_Order_picked_hrs
        self.Time_Order_picked_min=Time_Order_picked_min
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Delivery_person_ID':[self.Delivery_person_ID],
                'Delivery_person_Age':[self.Delivery_person_Age],
                'Delivery_person_Ratings':[self.Delivery_person_Ratings],
                'Restaurant_latitude':[self.Restaurant_latitude],
                'Restaurant_longitude':[self.Restaurant_longitude],
                'Delivery_location_latitude':[self.Delivery_location_latitude],
                'Delivery_location_longitude':[self.Delivery_location_longitude],
                'Weather_conditions':[self.Weather_conditions],
                'Road_traffic_density':[self.Road_traffic_density],
                'Vehicle_condition':[self.Vehicle_condition],
                'Type_of_order':[self.Type_of_order],
                'Type_of_vehicle':[self.Type_of_vehicle],
                'multiple_deliveries':[self.multiple_deliveries],
                'Festival':[self.Festival],
                'City':[self.City], 
                'Order_Date_Year':[self.Order_Date_Year],  
                'Order_Date_Month':[self.Order_Date_Month], 
                'Order_Date_Day':[self.Order_Date_Day],  
                'Time_Orderd_hrs':[self.Time_Orderd_hrs],  
                'Time_Orderd_min':[self.Time_Orderd_min],  
                'Time_Order_picked_hrs':[self.Time_Order_picked_hrs],  
                'Time_Order_picked_min':[self.Time_Order_picked_min],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)