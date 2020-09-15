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

## Separate Modes Explained
- **Admin Mode**:Admin has the option to upload a video on the AWS Server / fetch a video from an I.P. Address and generate/update a database with the corresponding vehicles & charges.
