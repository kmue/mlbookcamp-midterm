# create service file as for hw7 to satisfy model deployment requirement for midterm project
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

class InsuranceHolder(BaseModel):
    Gender: str # 'Female' / 'Male'
    Age: int # in years, whole number
    Driving_License: int # 1 / 0
    Region_Code: int # whole number
    Previously_Insured: int # 1 / 0
    Vehicle_Age: str # '1-2 Year' / '< 1 Year' / '> 2 Years'
    Vehicle_Damage: str # 'Yes' / 'No'
    Annual_Premium: int # whole number
    Policy_Sales_Channel: int # whole number
    Vintage: int # nb of days

model_ref = bentoml.sklearn.get("insurance_response:latest")
dv = model_ref.custom_objects["dictVectorizer"]

model_runner = model_ref.to_runner()

svc = bentoml.Service("insurance_response_classifier", runners = [model_runner])

@svc.api(input = JSON(pydantic_model=InsuranceHolder), output = JSON())
def classify(customer_profile):
    customer_information = customer_profile.dict()
    vector = dv.transform(customer_information)
    prediction = model_runner.predict_proba.run(vector)
    # return prediction # trying this --> working but now no longer returning other "return" content
    # print(prediction)
    #return prediction[:,1]

    result = prediction[:,1]
    if result > 0.3:
        return { "status": "VERY LIKELY INTERESTED" }
    elif result > 0.2:
        return { "status": "LIKELY INTERESTED" }
    elif result > 0.1:
        return { "status": "MAYBE INTERESTED" }
    else:
        return { "status": "DO NOT FOLLOW UP"}