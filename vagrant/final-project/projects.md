# Final Project Submissions

### Overview

Below are all of the submissions made by CMSC389L students in Fall 2017. To read more about the final project, [look here](/vagrant/final-project/README.md).

### Projects

#### Uvent: Tal Davidi, Tim Chen

**Abstract**: Uvent is an automatically updating service which helps users find nearby events. Users can use Amazon Alexa to discover interesting events going around on campus (currently available for UMD). Each morning, Uvent scrapes datasets and calendars to load new event information. This information is available through the Alexa skill, our frontend website, and our public API. Users can also submit events to our database through our website or through POST requests.

**Services**: Lambda, DynamoDB, API Gateway, Elastic Beanstalk, Alexa Skills Kit, Cloudwatch

**GitHub**: https://github.com/timothychen01/uvent

{{ 'https://www.youtube.com/watch?v=uM8DYldtCOQ' | iframely }}

#### Split: Chris Nakamura

**Abstract**: Split is a Google Photos like service.  When you upload your photo to Split, they are automatically tagged using computer vision.  Then, the user can search for their images using these tags.

**Services**: S3, Lambda, Rekognition, RDS, ECS

**GitHub**: https://github.com/chnakamura/CMSC389L-Split

{{ 'https://www.youtube.com/watch?v=B0L8dqx8wY4' | iframely }}

#### Soundsave: Cameron Payton, Ishaan Parikh

**Abstract**: Our project allows DJs and regular people alike to save their favorite Soundcloud songs and remixes to their Dropbox simply by texting the Soundcloud to a number. They can then use the songs later by accessing their Dropbox at any time.

**Services**: DynamoDB, S3, Lambda, SNS

**GitHub**: https://github.com/pikachu/aws_soundcloud_to_dropbox

{{ 'https://youtu.be/NZWSUCejEzA' | iframely }}

#### GPSBook: Nisarg Patel

**Abstract**: An online address book that stores user places based on GPS location. GPS location is determined by HTML5 geolocation API, no addresses needed.

**Services**: Route53, Cloudfront, S3, API Gateway, DynamoDB, Lambda

**GitHub**: https://github.com/nisargnp/GPSBook

{{ 'https://youtu.be/MPv1wcXztvc' | iframely }}

#### Mooni: David Ng

**Abstract**: Mooni is a very lightweight web application for keeping track of your expenses. Users can add their expenses and track their past expenses, seeing their total amount spent.

**Services**: S3, Elastic Beanstalk, DynamoDB

**GitHub**: https://github.com/ng-david/expense-aws-public 

{{ 'https://youtu.be/iwmJYXIT5Mo ' | iframely }}

#### PhotoTagger: Will Gomolka

**Abstract**: PhotoTagger is an app that allows users to take pictures of their friends and automatically have it sent to those who appear in them without having to do anything on their own.

**Services**: S3, DynamoDB, Lambda, Rekognition

**GitHub**: https://github.com/will108/PhotoTagger

{{ 'https://youtu.be/bdQt3WloVYw' | iframely }}

#### Spammy: SaiArvind Ganganapalle

**Abstract**: Spammy helps you keep track of spam numbers. Just tell Alexa to ask Spammy to either add a number, delete a number, check if a number has called you before, or send you a spam report. So now you don't have to remember which spam numbers called you.

**Services**: Alexa Skills Kit, Lambda, DynamoDB, SNS, SES

**GitHub**: https://github.com/saiarvindg/spammy

{{ 'https://youtu.be/8EwzyTx-ky0' | iframely }}

#### SoundLab: Ryan Stumbaugh

**Abstract**: A collaborative music listening web app.

**Services**: DynamoDB, API Gateway, Lambda, Elastic Beanstalk

**GitHub**: https://github.com/rstumbaugh/soundlab 

{{ 'https://www.useloom.com/share/5fe07ae69fec488ca2c1d8ef2b566a1c ' | iframely }}

#### Lex Speech Assistant: Sahana Rao

**Abstract**: Lex Speech Assistant is a web app that provides a means for individuals with speech disorders and impairments to practice and improve their speech with an integrated Lex chatbot. 

**Services**: Lex, Lambda, DynamoDB

**GitHub**: https://github.com/srao2019/lex-speech-assist

{{ 'https://youtu.be/J5Ccq4rBJW8' | iframely }}

#### Virtual Space Tour: Raghav Gupta, Raghav Bhasin

**Abstract**: Alexa virtual space tour, talks about celestial bodies and displays it in Unity.

**Services**: Alexa Skills Kit, Lambda, SQS, DynamoDB, Cognito

**GitHub**: https://github.com/RaghavKGupta/Virtual-Space-Tour

{{ 'https://www.youtube.com/watch?v=ZBR7Mc02U_k' | iframely }}

#### Food Tracker: Charlie Ching

**Abstract**: Food Tracker is a web application that will allow users to track their food that has been eaten throughout the day and will then record the food’s nutritional attributes along with a food recommendation.

**Services**: S3, DynamoDB, Cloudtrail, API

**GitHub**: https://github.com/charlieching/FoodTracker

{{ 'https://www.youtube.com/watch?v=RvLywpsd0ag' | iframely }}

#### AlexaTwitchModerator: Dennis Reyes, Jihoon Ok

**Abstract**: The AlexaTwitchModerator is a tool which streamers can use their voice to invoke chat commands, rather than the streamer having to alt tab to input the commands they wish to invoke on their chat. 

**Services**: S3, Alexa Skill Kit, Lambda, SQS

**GitHub**: https://github.com/jihoonok/AlexaTwitchModerator

{{ 'https://youtu.be/Qc-SxqBI9AQ' | iframely }}

#### Hanna Kim, Nazifa Chowdhury

**Abstract**: A Node.js web app that lets you chat with another person and draw together on a shared canvas.

**Services**: Elastic Beanstalk, EC2, S3

**GitHub**: https://github.com/nazifanchowdhury/CatchMySketch

{{ 'https://www.youtube.com/watch?v=q-7R1hjUNH8' | iframely }}

#### Securebox: Arman Irman

**Abstract**: A lightweight web app to store and share files in the cloud with managed identities using Cognito. 

**Services**: Lambda, DynamoDB, S3, Cognito

**GitHub**: https://github.com/ArmanIman/389LFinal

{{ 'https://youtu.be/bOwrLYgc5qw' | iframely }}

#### Photo-Link: Tony Cheng

**Abstract**: Photo-link, a service for turning mobile photos into shareable photo links

**Services**: Lambda, API Gateway, DynamoDB, S3, Rekognition

**GitHub**: https://github.com/tocheng1/photo-link

{{ 'https://www.useloom.com/share/e2bd74d6cc424e1986c626ee4c83e771' | iframely }}

#### Personal Weather Assistant: Brandon Daniel

**Abstract**: A personal weather assistant that uses ML to predict how many layers of clothing you should wear.

**Services**: Lambda, DynamoDB, S3, ML, Cognito

**GitHub**: https://github.com/BDanielCS/PersonalizedWeatherAssistant

{{ 'TODO' | iframely }}

#### Alexander Zhang

**Abstract**: Allows you to set groups, colors, and actions for hue lights using a chat bot.

**Services**: Lambda, IOT, DynamoDB, Lex

**GitHub**: https://github.com/AlexanderYZhang/HueServer

{{ 'https://www.useloom.com/share/4a409e5c1c23427aa3e16b28159f0278' | iframely }}

#### Bryan Soriano

**Abstract**: This is an interactive story game which uses Amazon Alexa. Users can interact with the story by telling Alexa what direction/choices they want to take in the story. Users progress is saved and they can leave or come back at any point. Plays sounds from S3 to increase immersion.

**Services**: S3, Alexa Skill Kit, Lambda, DynamoDB

**GitHub**: https://github.com/Bryzzle/AlexasAdventure

{{ 'https://www.youtube.com/watch?v=JI9Q9LvhG7Q&feature=youtu.be' | iframely }}

#### Minecraft: Isaac Lockwood

**Abstract**: Minecraft hosted on AWS!

**Services**: EC2, S3, EBS, EIP, SNS, IAM

**GitHub**: https://github.com/iaLockwood/CMSC389L

{{ 'https://www.useloom.com/share/1a80855a063b493690215ea836aa9151' | iframely }}

{{ 'https://www.useloom.com/share/aeba86ee93c64b35b23630e32bf10e46' | iframely }}

{{ 'https://www.useloom.com/share/ac3bf8205dad438298c6da96ee4a2564' | iframely }}
