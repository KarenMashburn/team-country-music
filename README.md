# team-country-music

# Topic
The topic for our final project is pitching data in MLB. We selected this data because we found it intruiging, extremely flexible, and because we thought that the explorations we create with this data could be very enjoyable for anyone who enjoys the game of baseball. Our data comes from MLB's statcast. Statcast is a database created by the MLB for the purpose of analysizing the statistical aspects of baseball. Cameras record input data from every pitch from every game of the MLB, the data is robust, clean, and fascinating. There is 93 columns of data in the starting data set, from the pitcher/batter present and the type of pitch, to the outcome of each individual pitch, at bat, and game. There are a few questions we are excited to explore with this data set:

1. Can you predict what will be pitched by each MLB team, and prepare for it?
2. Can you predict the outcome of an at bat or baseball game with customized inputs on pitching data?
3. What are the largest factors in decided what makes the best pitchers in the MLB great?

We expect that with such a large, organized dataset, we will come across many other questions that we are very excited to explore and see what answers the data might yield. 

# Roles
Square Karen Mashburn

Trianlge Matthew Muldoon

Circle Hayden McMordie and Dayton Marchlewski

X Conor McGrew

# Communication Protcols
Slack.

Meetings Tue, Thur during class time.

Additional meetings Sunday mornings.

# Technologies Used

### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using PyPlot. 

### Database Storage
The "database" is simply a csv at the moment. But in order to integrate it with our webpage, we may later be using SQLite. SQLite also may be beneficial to more easily generate queries for the pertinant pitcher data. 

### Machine Learning
Matthew has mocked up a gradient boosted classifer, a logistic model, and a neural network. 

### Dashboard
We will use both Flask and D3.json to create an interactive model. The model will be hosted on github. 

## Updates
Neural Net model "works" but with 0% accuracy. Need to update the zones to be catergorical rather than integers (should be easier for activation functions to predict). Also need to incorportate more datasets. 
Started a skeleton of an html script and an app.js file based on the UFO sightings page. We will be making the fillable fields into drop down menus later. 
