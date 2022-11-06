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

Both notebook.ipynb and train.py should easily be executable after pulling the mlbookcamp-midterm repository. The dataset is included as part of the repository.

## Model deployment

The final model was exported using BentoML (see: train.py).

In addition, the following files are required for deployment:

- service.py configures the service interface: Expected/allowed inputs and data types, their transformation for prediction, prediction output along with business indications on how to proceed with the obtained prediction output (predicted interest of the insuranceholder customer profile passed as input).

- bentofile.yaml adds metainformation about the project to the service interface as well as which non-standard packages are being used. In this case: pydantic for service.py, sklearn for random forest classifier model.

## Dependency and environment management

A list of the required dependencies and environment (python version, required packages, requirements.txt, basic dockerfile etc.) was created automatically when exporting using BentoML and saved to the bento.

The following steps need to be done in order to prepare the model for deployment as a local service:

1) In the bash terminal, open the project folder /mlbookcamp-midterm

2) Build a BentoML "bento" from the above prepared file by entering "bentoml build". This will create a bento file which includes all necessary information for dependency and environment management.

The resulting bento file from step 2) is identified by a service name (as defined in service.py) + service tag (assigned during and displayed after the build process).

3) Test the bento locally by entering "bentoml serve". This command starts a so-called BentoServer on your current machine so the model service can easily be accessed in the browser (under http://0.0.0.0:3000 by default).

## Containerization

After making sure locally that the bento file results in a service that works as it should, you can easily containerize the service using BentoML once again.

In order to do this, you need to enter "bentoml containerize" along with the name and tag of the bento you want to containerize. An easy shortcut to containerize the most recently created bento (which is likely to be what you want to do) is to use the tag "latest". The full command to containerize the latest version of bento "insurance_response_classifier" would therefore be "bentoml containerize insurance_response_classifier:latest".

## Deployment

As a result of the containerization process, BentoML will provide you with instructions how to then use the Docker image you just created. With Docker installed, you can again test the functionality of the image by following these instructions. The only difference is that now the exact tag is part of the Docker image name and will need to be passed explicitly, e.g. as follows:

docker run -it --rm -p 3000:3000 insurance_response_classifier:ay3vrzs576p4tq4x serve --production

This will launch a (local) Docker instance running the same service which you can again test in your browser under (by default) http://0.0.0.0:3000.

The video file "docker deployment screen capture 20221106.mov" provided as part of the repository shows how I launch and interact with the running service as described above.





