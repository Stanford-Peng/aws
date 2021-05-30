# TagTag - Modern Image Detection & Storage in Cloud

TagTag is a modern image detection application stored entirely using [AWS Services](https://aws.amazon.com/)
- Lambda Functions
- Cognito User Pool 
- S3 Buckets
- DynamoDB
- API Gateway

## Architecture
![Architecture](https://github.com/Stanford-Peng/aws/blob/main/gitResources/Architecture.png)

## Features
### 1. Upload Image 
Using [YOLO - Real-Time Object Detection](https://pjreddie.com/darknet/yolo/), the uploaded images are assigned tags based on detected objects (E.g., Person, Tree, Cup, Chair)
![Upload](https://github.com/Stanford-Peng/aws/blob/main/gitResources/Upload.png)

### 2. Search Images by Tags
Users can query the API to find images with specified tags
![FindByTags](https://github.com/Stanford-Peng/aws/blob/main/gitResources/FindByTag.png)

### 3. Search Images by Image
Using [YOLO - Real-Time Object Detection](https://pjreddie.com/darknet/yolo/), the uploaded image can return similar images based on their tags
![FindByImage](https://github.com/Stanford-Peng/aws/blob/main/gitResources/FindByImage.png)

## Real World Applications
The global spread of Coronavirus has greatly increased the necessity for individuals to wear facemasks when engaging in public activity. Many governments across the world legally enforce this requirement, particularly when entering public locations.  

We believe that the image recognition service deployed could be integrated with a camera/webcam, as well as physical barriers, to monitor entry into specific areas. For example, in order to enter a shopping centre, visitors have to walk up to a barrier with a webcam. The webcam image is then processed using the image detection service and searches for the tag ‘Facemask’, and an accuracy level of above 60%. Should these criteria be met, the visitor will then be permitted to enter the premises. Optionally, the images for each visitor will then be stored into a database if visitors agree to it, and they can be revisited at a latter point in time.  
