# AWS MachineHack

This is our submission for the MachineHack AWS Hackathon 

**Toll Booth Automation System using Vehicle and Number Plate Recognition System**

## Installation

```bash
pip install -r requirements.txt
```

##  Themes Highlighted 
- Deep Learning,Computer Vision & Image Processing
- AI for Transportation/Media & Entertainment/e-Commerce/FinTech
- Machine Learning for Automation

## Detailed Desciption/Outline 
- The project system uses Yolo’s Image Segmentation to recognize the type of vehicle and then assign a unique ID to the vehicle in the database using the Text decrypted by the Vehicle’s Number Plate.
- There is an option to use a pre-existing database or make a fresh one using sqlite/AWS/DynamoDB  integrated with python.
- Special treatment to Ambulance and other Emergency vehicles as they won’t be charged.
- Equipped with a fully functioning web-portal where users can login, see their account balances and pay their charges using online payment portals.

### Features

## Separate Modes Explained
- **Admin Mode** - Admin has the option to upload a video on the AWS Server / fetch a video from an I.P. Address and generate/update a database with the corresponding vehicles & charges.   

![admin](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/5.jpg)

![admin](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/6.jpg)

- **User Mode** - The user has a separate account linked to Aadhar Card to login and a dedicated AWS Database is used to store and return the information.

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/3.jpg)

## Database  
The entire functioning would be primarily based on the collective functioning of the user details and the fine details database that would be used on AWS Database. The attributes are shared below:

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/10.jpg)

## Payments Portal  
The website is supported with a payments portal that can be called upon by the user to pay the toll charges. The support with various third party payment portals and banks is also supported. The charges however are dynamic and can be tuned/adjusted for various vehicle classes.

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/4.jpg)

## Chatbot  
An assistive chatbot aimed to help the user to use and navigate through the chatbot.

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/8.jpg)

## Vehicle Recognition 
We have used Yolo’s supervised Object Detection to detect the various vehicles in an image/video source. A sample is attached below

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/1.jpg)


## License Plate Retrieval
This feature is achieved using a methodological approach consisting of License Plate Detection and License Plate Recognition which are being achieved by using Yolo and OCR. Instead of using a 3rd party OCR we have trained our OCR model on a combination of 3 usual Vehicle Number Plate datasets using Tensorflow on the AWS Sagemaker.

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/9.jpg)

##  Emergency Vehicle Classification  
The system is equipped with a Computer Vision model to separate emergency vehicles like Ambulance/Police Vehicles to create a hassle free execution system in real life too! The model is trained using the AWS EC2.

### Flow of Control
- **User**

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/user.png)

- **Admin**

![user](https://github.com/namantuli18/Amazon-Web-Services-Hackathon/blob/master/img/My%20First%20Document%20(1).png)

## AWS Technologies
![user](https://i.ibb.co/WVWcPXC/Screenshot-59.png)

## In a video
<a href="https://streamable.com/mmq1rw"> ![user](https://cdn-cf-east.streamable.com/image/mmq1rw.jpg) </a>
