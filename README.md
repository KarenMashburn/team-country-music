# Team Country Music Final Project

## [Link to Google Slides](https://docs.google.com/presentation/d/1oTCmH0jA_3dtR0kVGq1bWAZvFO9u1cl-YB06-JuqyF8/embed?start=false#slide=id.p)


## Topic
For this project, we focused on pitching data from the MLB. This was chosen due to its intriguing nature and extreme flexibility, and because we believe that our explorations into the data could be very enjoyable for anyone who appreciates the game of baseball. Our data comes from the [MLB's Statcast](https://www.mlb.com/glossary/statcast) - a database created by teh MLB for the purspore fo analysing the statistical aspects of baseball. Cameras record data for every pith from every game of the MLB, each year producing datasets, hundreds of thousands of entries long, which are robust, clean, and downright fascinating. In our starting dataset alone, there were 93 columns of potential features - from the pitcher/batter present during the pitch event and the type of pitch thrown, to the outcome of each individual pitch, at bat, and game, to the x-z coordinates of the ball as it left the pitcher's hand or crossed over the plate. 

With so much data at our fingertips, we were excited to explore the datasets, coming up with many questions including (but not limited to):

- Can we predict what will be pitched by each MLB team, and prepare for it?
- Can we predict teh outcome of an at bat or baseball game with customized inputs on pitching data?
- What are the largest factors in deciding what makes the best pitchers in the MLB great?


With such a large, organized dataset, we came across these and many other questions that we were very excited to explore and see what answers the data might yield. Although we were unable to delve into every question we wanted to, we _were_ eventually able to focus our efforts towards one question the datasets lent themselves to:

- Can we predict whether or not a pitch will be a 'strike'?

## Roles
During the project time, each member stayed assigned to their roles, as listed below:

- Square: Karen Mashburn

- Triangle: Matthew Muldoon

- Circle: Hayden McMordie and Dayton Marchlewski

- X: Conor McGrew

However, as the project progressed, the stark borders between roles became more looseweave, with members stepping outside of their defined responsibilites to help others when needed and to ensure the project continued smoothly.

## Communication Protcols
Our main form of communication during the project was through our team chat in Slack.

Otherwise, we had meetings every Tuesday and Thursday during class time, with additional meetings planned for Sunday mornings. 

Other Zoom meetings were held outside of this schedule as needed. 

## Technologies Used


### Data Cleaning and Analysis
Pandas and Jupyter Notebook were used to clean the data and perform exploratory analyses. 

### Database Storage
Our database was stored using a combination of SQLite, Postgres, and AWS.

### Dashboard
For our dashboard, we used HTML/CSS along with Flask to create an interactive model for users. It will be deployed on Heroku.

## Machine Learning Models

### Preliminary Data Preprocessing

When we initially obtained our datasets, they each had 93 columns of data - much more than we needed to produce our models. Additionally, due to the nature of the column names, and the fact that no one on our team was well-read on the different statistics collected by Statcast, we were initially overwhelmed and unsure of what the datasets actually contained. 

We overcame this initial hurdle by finding the [Statcast CSV Documentation](https://baseballsavant.mlb.com/csv-docs), which
helped us make sense of the datasets and allowed us to begin the process of designing our machine learning models.

While we at first began modeling using data for all pitchers from 2017-2020, we very quickly ran into computational barriers - our computers were unable to handle the 2.3+ million rows of data we were using. This, along with concerns of overwhelming users on our dashboard, led us to focus our data on the top 9 pitchers in the MLB from 2019-2020.


### Preliminary Feature Selection and Decision-Making Process

For our models, we focused on two questions:

- Can we predict whether a pitch will be a 'strike', 'ball', or 'in play'?
- Can we predict what zone the pitch will be thrown to?
    
but as will be noted later, these had to be adjusted as the modeling process continued, leading us to our final question:

- Can we predict whether or not a ptich will be a 'strike'?

Once we came to understand the data we had, we were able to begin paring it down to only those columns that were relevant to our questions. This meant the removal of any columns that we believed were not immediately related to pitching.

This was further reduced as the project continued to only those features that we believed were directly involved in the pitch and that the pitcher might strategically think about during an event. This lead us to our final list of eleven features we felt were relevant to our questions and provided fair accuracy in our models:

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

During this process, we also used One Hot encoding on the categorical features.


### Creation of Training and Testing Sets

To create our training and testing sets, we used the train_test_split function. This allowed us to easily form and standardize the training sets for both X and y. Since our questions and data pointed towards the creation of a supervised machine learning model, these sets were directly formed from our data, directly predicting a known quantity (whether or not a pitch was a strike. 


### Model Choice

Once our data was processed, our features were chosen, and training and testing sets were formed, we created multiple different models - a Gradient Boosted Classifer, a Logistic Classifier, and a Neural Network - to 'see what stuck'.

These differing models were selected for their for their abilities to classify data that is as diverse and extensive as ours. The neural network was selected since our initial dataset had upwards of 35 features. Unfortunately, our neural network model did not perform well - with some iterations having an accuracy as low as 2%! The Gradient Boosted Classifier was selected due to its ability to classify data with high accuracy while remaining robust and resiliant against overfitting. The Logistic Regression was chosen as it is 'the classic' function for use when classifying. However, the Logisitic Regression traditionally workis with binary classifications, and while we attempted to modify it to work with non-binary data, we were not very successful.

Ultimately, we decided on using the Gradient Boosted Classifier.


#### Limitations

With the Gradient Boosted Classifier, we created two models - one for determining the pitch outcome (strike, ball, in play) and one for determining the zone outcome - with great accuracies, ~73% and ~92% respectively. 


However, upon closer inspection of our models and their classification reports, we found that they were not behaving as expected. Our zone model (~92%) was relying on features that gave the position of the ball as it passed over the plate - almost definitionally what the zone is. When this was removed, our accuracy dropped ~40 points to ~51%. Further, when looking at its classification report, we found that the model was not making predictions as much as it was assigning every pitch to a specific zone, namely 14. That is, our model was 51% accurate because our datasets were 51% zone 14, and the model only ever guessed zone 14. 
Despite attempts to stratify the model and oversample our lacking rows, we were not able to drastically change the model's ability to predict many other zones.

With this discovery in the zone model, we decided to check our pitching model for similar tendencies. Unfortunately, our suspicions were well-founded - the model was predominantly predicting 'strike' or 'ball' at the expense of 'in play'. To combat this issue, we combined 'ball' and 'in play' into a single category - 'not-strike'. This allowed the model to maintain its accuracy while making predictions on the pitch event.

Finally, due to the black box problem, it is unfortunately hard to understand what exactly the model did to come to the predictions it outputs, making deeper analysis of our model difficult.

#### Benefits

Due to the Gradient Boosted Classifier's use of 'weak learners', it is able to create models with high accuracy while maintaining resilience against overfitting. This allows it to work with our massive dataset without too much variance or bias, despite its sensitivity to outliers. Additionally, the tunability of its parameters (loss function, depth, number of trees, number of features, etc.) provides the Gradient Boosted Classifier a flexibility with our data.


## Circle Role/Database
For our mock database, we have preprocessed the statcast CSV provided by the MLB. Dayton and I collaborated together to remove unecessary rows, encode categorical data, and clean the data for number inconsistencies and null values that could have caused issues in our preliminary data explorations. We have sent the prelim version of the csv to each member in the group to work as our prelim database. 

