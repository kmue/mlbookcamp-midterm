# mlbookcamp-midterm
ML Bookcamp Midterm Project

For the ML Bookcamp midterm project, I am going to analyze a health insurance cross selling dataset.

## Dataset and problem description

The dataset (here downloaded from kaggle, originally provided via Analytics Vidhya) describes a sample of
existing health insurance policyholders along with their response to an offer for additional insurance for a motor vehicle.

The customer information includes details about

- demographics (gender, age, region code type, whether or not the customer holds a driving license)

- vehicles (vehicle age, previous damage)

- policy (annual premium for the marketed vehicle coverage and marketing channel used to address the customer)

- "vintage" (number of days the policyholder has been a customer with the insurance company)

- target variable: response (1: customer is interested, 0: customer is not interested)

The goal is to predict a yes/no target variable which indicates whether a policyholder agreed to also obtain vehicle
insurance coverage from the insurance company.

## EDA, model training and parameter tuning

All of this can be found in the jupyter notebook file notebook.ipynb

## Exporting notebook to script

For the relevant part of the training process for the final model as well as and exporting the same using BentoML please refer to file train.py

## Reproducibility

Both notebook.ipynb and train.py should easily be executable after pulling the mlbookcamp-midterm repository. The dataset is part of the repository.

## Model deployment

The final model was exported using BentoML (cf. train.py).

In addition, the following files are required for deployment:

- service.py configures the service interface: expected/allowed inputs and data types, their transformation for prediction, prediction output along with business indications on how to proceed with the obtained prediction output (predicted interest of the insuranceholder customer profile passed as input)

- bentofile.yaml adds metainformation about the project to the service interface as well as which non-standard packages are being used (here: pydantic for service.py, sklearn for random forest classifier model)

## Dependency and environment management

A list of the required dependencies and environment (python version, required packages, requirements.txt, basic dockerfile etc.) was created automatically when exporting using BentoML and saved to the model file.

The following steps describe how to deploy the model as a local service:

- TO DO

- TO DO

- TO DO

## Containerization

TO DO

## Cloud deployment

TO DO





