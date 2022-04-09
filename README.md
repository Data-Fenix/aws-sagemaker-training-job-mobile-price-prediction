# Build ML Training Pipeline for Mobile Price Prediction Model usning AWS SageMaker Pipeline

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Contributing](#Contributing)
  * [License](#license)
  * [Credits](#credits)

## Demo
![full](https://github.com/Data-Fenix/aws-sagemaker-pipeline/blob/main/demo/full.gif)

## Overview

Previously we developed a mobile price prediction model using regression technique (To see that project, please click here) and now the business intends to deploy that model into production, which can be used for real time predictions for the latest customer base. To fulfill the requirement we choose AWS cloud platform to deploy this model. 
According to the business requirements and considering the cost factor, two separate pipelines are developed for training and inference jobs(Will discuss more details in the business requirement and the solution section). Following sections show how to deploy training pipelines in AWS Sagemaker and the uniqueness of this is, we use **“bring your own code concept to orchestrate the ML workflow”**.
 
## Dataset

##### Independent Features
* Unnamed: 0 - Index column and this is an unnecessary column
* Brand me — Brand of the mobile phone and the model.
* Ratings — Consumer rating for the mobile phone
* RAM — RAM size of the mobile
* ROM — ROM (Internal Memory) size of the mobile
* Mobile_Size — Size of the mobile in inches
* Primary_Cam — Pixel size of the back camera
* Selfi_Cam — Pixel size of the front/selfi camera
* Battery_Power — Battery capacity of the mobilr in mAh
##### Dependent Features
* Price — Price of the mobile

## Motivation

When I was searching about AWS Sagemaker, I struggle a lot as lack of references in this feild. It has some references, but there are missing few things. Therefore I need to fullfil that gap. So now I have some experience in this feild and as a MLOps team memeber, I migrated a lot of projects into cloud. I saved data scientists' valuable time by automating and scheduling their ML projects. So now I need to share that experience and knowledge with you and this is my first step of that journey.
## Technical Aspects

This project highly relies on AWS cloud platform and in here we don’t train any model. We use previously developed projects from scratch and trying to deploy it in AWS.
1) Used s3 bucket to store the input/output data, models and model artifacts.
2) Used Sagemaker to implement and modify the existing scripts. And also automated the Python scripts.
3) Containerize all the scripts using Docker images and stored them in ECR repository
4) Used build your own container concept in AWS
5) Used AWS Sagemaker Studio to view the Sagemaker Pipelines, execution history, model performance matrices,etc.
6) Used Sagemaker Model Registry to save the model

## Installation

#### Requirements

1. An AWS account
2. Python 3.5+
3. Docker (optional)


Only thing you need to satisfy in this list is you must have an AWS account. If you don't have an account you can create it free, using below link:
https://aws.amazon.com/free/
    
## Run
1) Upload/push/clone previously implemented mobile price prediction project into AWS Sagemaker instance or JupyterLab environment.
2) Run build_docker.ipynb
3) Execute training_pipeline.ipynb
4) See the workflow using AWS Sagemaker stuido
* (i) Open Sagemaker Studio
* (ii) Choose Pipeline option then you can see the execution list
* (iii) Select the executing one, see the visualization
* (iv) If you need to see more details about each stage, click on the each bubble and right hand side you can see all the details of each stage
* (v) To see the model registry, click the Model Registry option in the left hand side

## Deployment on AWS Sagemaker

Will disscuss more details in the pipeline_train.ipynb

## Directory Tree

```
├── data 
|   └──data.csv
├── mobile_price_preprocessing
│   ├── Dockerfile
|   └── preprocessing.py
├── mobile_price_training
│   ├── model
|       └──train.py
|   ├── Dockerfile
├── build_docker_training.ipynb
├── aws_helper.py
├── CONTRIBUTING.md
├── LICENSE
├── setup.py
└── tox.ini
```

## To Do

Need to add,
1) Need to add evalution step as a seperate component
2) Need to add accuracy condition to the workflow

Don't worry, we will discss above topics and many more in the future sections.

## Bug / Feature Requests
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/Data-Fenix/aws-sagemaker-training-job-mobile-price-prediction/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/Data-Fenix/aws-sagemaker-training-job-mobile-price-prediction/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
[<img target="_blank" src="https://venturebeat.com/wp-content/uploads/2021/02/SageMaker.jpg?fit=1292%2C664&strip=all" width=200>](https://venturebeat.com/wp-content/uploads/2021/02/SageMaker.jpg?fit=1292%2C664&strip=all) [<img target="_blank" src="https://www.cloudsavvyit.com/p/uploads/2019/06/55634f08.png?width=1198&trim=1,1&bg-color=000&pad=1,1" width = 200>](https://www.cloudsavvyit.com/p/uploads/2019/06/55634f08.png?width=1198&trim=1,1&bg-color=000&pad=1,1) [<img target="_blank" src="https://jfrog.com/connect/images/6053d4dc2f6c53160a53d407_linux-container-updates-iot.png" width = 200>](https://jfrog.com/connect/images/6053d4dc2f6c53160a53d407_linux-container-updates-iot.png) [<img target="_blank" src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Logo-2015-2017.png" width = 200>](https://logos-world.net/wp-content/uploads/2021/02/Docker-Logo-2015-2017.png) [<img target="_blank" src="https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png" width = 200>](https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png) [<img target="_blank" src="https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png" width = 200>](https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png)

## Contributing

<p><b> ML Enginner </b> : Anuradha Dissanayake </p>
<p><b> Data Scientist </b>: Shashi Withanage </p>

## License

Copyright 2022 Anuradha Dissanayake and Shashi Withange

## Credits

1) https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb
2) https://docs.aws.amazon.com/sagemaker/



