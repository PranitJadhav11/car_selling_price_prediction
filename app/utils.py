import numpy as np
import pickle
import json
import os
import CONFIG

class Prediction():
    def __init__(self):
        print(os.getcwd())
    
    def load_raw(self):

        with open(CONFIG.MODEL_PATH,"rb") as model_file:
            self.model = pickle.load(model_file)

        with open(CONFIG.COLUMNS_PATH,"r") as col_file:
            self.col = json.load(col_file)

        with open(CONFIG.ENCODE_PATH,"r") as enc_file:
            self.encoded_data = json.load(enc_file)
        return "Load Raw Success"
        

    def predict_price(self,data):
        self.load_raw()
        self.data = data

        user_input = np.zeros(len(self.col["column_names"]))
        array = np.array(self.col["column_names"])

        car_name = self.data['car_Name']
        year = self.data['year']
        present_Price = self.data["present_Price"]
        kms_Driven = self.data['kms_Driven']
        Fuel_Type = self.data['Fuel_Type']
        Seller_Type = self.data['Seller_Type']
        Transmission = self.data['Transmission']
        Owner = self.data['Owner']
         

        user_input[0] = int(year)
        user_input[1] = int(present_Price)
        user_input[2] = int(kms_Driven)
        user_input[3] = int(Fuel_Type)
        user_input[4] = int(Seller_Type)
        user_input[5] = int(Transmission)
        user_input[6] = int(Owner)
        car_name = 'Car_Name_'+ car_name
        car_name = np.where(array == car_name)[0]
        user_input[car_name] = 1
        
        print(f"{user_input=}")
        print(len(user_input))

        car_price = np.around(self.model.predict([user_input])[0])
        print(f"Predicted Price = {car_price}")

        return car_price
    

if __name__ == "__main__":
 
    pred_obj = Prediction()
    pred_obj.load_raw()
    
 