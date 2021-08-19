# Team Country Music Final Project

## Topic
The topic for our final project is pitching data in MLB. We selected this data because we found it intruiging, extremely flexible, and because we thought that the explorations we create with this data could be very enjoyable for anyone who enjoys the game of baseball. Our data comes from MLB's statcast. Statcast is a database created by the MLB for the purpose of analysizing the statistical aspects of baseball. Cameras record input data from every pitch from every game of the MLB, the data is robust, clean, and fascinating. There is 93 columns of data in the starting data set, from the pitcher/batter present and the type of pitch, to the outcome of each individual pitch, at bat, and game. There are a few questions we are excited to explore with this data set:

1. Can you predict what will be pitched by each MLB team, and prepare for it?
2. Can you predict the outcome of an at bat or baseball game with customized inputs on pitching data?
3. What are the largest factors in decided what makes the best pitchers in the MLB great?

We expect that with such a large, organized dataset, we will come across many other questions that we are very excited to explore and see what answers the data might yield. 

## Roles
Square: Karen Mashburn

Triangle: Matthew Muldoon

Circle: Hayden McMordie and Dayton Marchlewski

X: Conor McGrew

## Communication Protcols
Slack.

Meetings Tue, Thur during class time.

Additional meetings Sunday mornings.

## Technologies Used


### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using PyPlot. 

### Database Storage
The "database" is simply a csv at the moment. But in order to integrate it with our webpage, we may later be using SQLite. SQLite also may be beneficial to more easily generate queries for the pertinant pitcher data. 

## Machine Learning Models

### Preliminary Data Preprocessing

When we initially obtained our datasets, they each had 95 columns of data - much more than we needed to produce our models. Additionally, due to the nature of the column names, and the fact that no one on our team was well-read on the different statistics collected by Statcast, we were initially overwhelmed and unsure of what the datasets actually contained. 

We overcame this initial hurdle by finding the [Statcast CSV Documentation](https://baseballsavant.mlb.com/csv-docs), which
helped us make sense of the datasets and allowed us to begin the process of designing our machine learning models.

While we at first began modeling using data for all pitchers from 2017-2020, we very quickly ran into computational barriers - our computers were unable to handle the 2+ million rows of data we were using. This, along with concerns of overwhelming users on our dashboard, led us to focus our data on the top 9 pitchers in the MLB.


### Preliminary Feature Selection and Decision-Making Process

For our models, we focused on two questions:
    - Can we predict whether a pitch will be a 'strike', 'ball', or 'in play'?
    - Can we predict what zone the pitch will be thrown to?
but as will be noted later, these had to be adjusted as the modeling process continued.

Once we came to understand the data we had, we were able to begin paring it down to only those columns that were relevant to our questions. This meant the removal of any columns that we believed were not immediately related to pitching.

This was further reduced as the project continued to only those features that we believed were directly involved in the pitch and that the pitcher might strategically think about during an event. This lead us to our final list of ten features we felt were relevant to our questions and provided fair accuracy in our models:

    - release_speed: the speed the ball is released at during the pitch
    - zone: the area above the plate the ball passes over (1-14, sans 10)
    - balls: the number of balls during the pitch event
    - strikes: the number of strikes during the pitch event
    - inning: the inning of the pitch event
    - release_spin_rate: the rate the ball spins when pitched
    - release_extension: the number of feet the pitcher extends forward from the pitcher's plate during the pitch event
    - pitch_number: how many pitches have been thrown during the batter's at-plate
    - stand: which side of the plate the batter stands on (L/R)
    - p_throws: handedness of the pitcher (L/R)
    - pitch_type: the type of pitch thrown (fastball, curveball, etc.)

During this process, we also used One Hot encoding on the categorical features, allowing us to create our models.


### Creation of Training and Testing Sets

To create our training and testing sets, we used the train_test_split function. This allowed us to easily form and standardize the training sets for both X and y. Since our questionsa and data pointed towards the creation of supervised machine learning models, these sets were directly formed from the datasets we can created. 


### Model Choice

Once our data was processed, our features were chosen, and training and testing sets were formed, we created multiple different models - a Gradient Boosted Classifer, a Logistic Classifier, and a Neural Network - to 'see what stuck'.

These differing models were selected for their for their abilities to classify data that is as diverse and extensive as ours. The neural network was selected since our initial dataset had upwards of 35 features. Unfortunately, our neural network model i  The Gradient Boosted Classifier was selected due to its ability to classify while remaining robust and resiliant against overfitting. At first, we attempted to modify the Logistic Regression to work with non-binary classifications, but were not very successful.

Ultimately, we decided on using the Gradient Boosted Classifier.


#### Limitations

With the Gradient Boosted Classifier, we created two models - one for determining the pitch outcome (strike, ball, in play) and one for determing the zone outcome - with great accuracies, ~73% and ~92% respectively. 


However, upon closer inspection of our models and their classification reports, we found that they were not behaving as expected. Our zone model (~92%) was relying on features that gave the position of the ball as it passed over the plate - almost definitionally what the zone is. When this was removed, our accuracy dropped ~40 points to ~51%. Further, when looking at its classification report, we found that the model was not making predictions as much as it was assigning every pitch to a specific zone, namely 14. That is, our model was 51% accurate because our datasets were 51% zone 14, and the model only ever guessed zone 14. 
Despite attempts to stratify the model and oversample our lacking rows, we were not able to drastically change the model's ability to predict many other zones.

With this discovery in the zone model, we decided to check our pitching model for similar tendencies. Unfortunately, it had similar tendencies - the model was predicting either 'strike' or 'ball' without predicting 'in play'. Due to this, we combined 'ball' and 'in play' into a single category, which allowed the model to maintain its accuracy while making predictions.

Unfortunately, due to the black box problem, it is hard to understand what exactly the model did to come to the predictions it outputs.

#### Benefits

The Gradient Boosted Classifier is able to create models with high accuracy while maintaining resilience against overfitting. This allows it to work with our massive dataset without too much variance or bias. Additionally, the way the Gradient Boosted Classifier works, by combining weak random forest predictors, is easily interpretable. 


### Dashboard
We will use both Flask and D3.json to create an interactive model. The model will be hosted on github. 

## Circle Role/Database
For our mock database, we have preprocessed the statcast CSV provided by the MLB. Dayton and I collaborated together to remove unecessary rows, encode categorical data, and clean the data for number inconsistencies and null values that could have caused issues in our preliminary data explorations. We have sent the prelim version of the csv to each member in the group to work as our prelim database. 

