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
*Jupyter Notebook

*Pandas

*Python

*Javascript / HTML

# Circle Role/Database
Our second segment has been filled with a large amount of data exploration. I have been working with Connor and Matthew to help nail down our machine learning model to the best accuracy we could find. Our database was interesting in how robust it was. The database contains over 90 columns of pitching data that was very accessible and extremely detailed. The main question we have been going through in our data exploration phase was not as much how do we need to pre-process and treat the data, but what questions we can actually answer with this masse of data! My role this segment has been helping Matthew and Connor by preparing any data sets and csvs that would help them create machine learning models for our dataset. I worked closely with both of them to help supply any data cleaned and encoded for ideas they might have in exploring our dataset. We explored multiple different ideas, like predicting what section of the strike zone pitches fell into naturally, how different at bats and pitch structures affected the delta run expectancy and delta win percentage, but in the end, it looks like our most accurate model has been for predicting the outcome of individual pitches, being strike, ball, or hit. We have gone through a few iterations of datasets in exploring this outcome prediction as we determined which features would be the most interesting for users to interact with on a website and which would be the most predictive of our model. It was an interesting challenge working on which features would be both a combination of predictive, and interesting for users. In the end, we have narrowed down our dataset massively and settled on a smaller group of features that gave us around 71% accuracy rates for ball strike and hit outcomes.  This smaller dataset is one that Matthew, Connor, and I came up with and is reflected in my datacleaning python notebook. I have moved this database into SQL and AWS for easy access for Connor and Matthew to work with in connecting to our model. I have also created smaller data sets for strike rates and zone rates by pitcher that have been moved into SQL as well and will be used as some of the main background information for our infographics that will be paired with the interactive sections of our project. We decided it would be interesting for users to be able to see inforgraphics of general strike and zone rates to compare to the interactive and predicitve model they will be using on our website. This will help give them a more general idea of the typical pitch rates seen in the MLB, which will help contextualize the results they will be seeing from our predictive model. 