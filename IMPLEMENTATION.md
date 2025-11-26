# Implementation




## Implemented :


### SQL Schema for information about users, study spots, and reviews


- users table  
**Contains information associated with each individual user**  
The users table consists of the fields userID (primary key), username, email, hashedPassword, favoriteStudySpot (as a foreign key), kudos, and createdAt. The favorite study spot connects the user to a spot entry in the study_spots table.


userID - int, auto increments on user creation, unique user identifier  
username - varchar, unique username for each user  
email - varchar, unique email address associated with each user  
hashedPassword - varchar, user password (hashing not yet implemented)  
favoriteStudySpot - int, spotID of user’s favorite study spot  
kudos - int, user’s kudos score  
createdAt - timestamp of when the user account was created  

---

- study_spots table  
**Contains information associated with each individual study spot**  
The study_spots table consists of the fields spotID (primary key), spotname, location, and createdAt.


spotID - int, auto increments on study spot creation, unique study spot identifier  
spotName - varchar, unique name for each study spot  
location - varchar, location for the study spot  
createdAt - timestamp of when the study spot was created  

---

- spot_reviews table  
**Contains information associated with each individual study spot review**  
The spot_reviews table consists of the fields reviewID (primary key), userID (as a foreign key), spotID (as a foreign key), noiselevel, crowdedness, starRating, reviewText, createdAt, and updatedAt. The userID and spotID ensure one active, unique review per user per spot, through the unique key constraint unique_user_spot_review. On the deletion of either the user or study spot associated with a review, the entire review is deleted.


reviewID - int, auto increments on study spot review creation, unique review identifier  
spotID - int, spotID of the study spot that is reviewed  
userID - int, userID of the user who is creating the review  
noiseLevel - int, the noise level from 0 to 10 of the study spot in the review  
Crowdedness - int, the crowdedness level from 0 to 10 of the study spot in the review  
starRating - int, the star rating from 0 to 5 of the study spot in the review  
reviewText - varchar, the text content of the review  
createdAt - timestamp of when the review was created  
updatedAt - timestamp of when the review was updated  

---

### Identifying Object Classes for User, Spot, and Review.


- Review.py  
**Represents the review information on a spot that is left by a user**  
Contains a unique ID for the review. Information fields about the spot, such as: Rating, Review text content, Noise Level, Crowdedness, and the associated User and Spot Ids.


- Spot.py  
**Represents a single Study spot**  
Contains a unique ID for the spot. Information fields: Name of the spot, Location of the spot, and unique Spot ID


- User.py  
**Represents the user**  
Contains a unique ID for the user. Information fields: Username, email, password, favorite spot, kudos level.


### Database Operation Files for User, Spot, and Review.


- ExecuteDB.py


**Overview**
This file handles the actual database operation to the SQL database by taking in the SQL command and value to execute.

 **Execute Operations**  
**Defines the functions**
1.  Execute Database Operation
---

- ReviewDB.py


**Overview**
This file creates SQL values and commands to send to the ExecuteDB file to do database operations for the spot_reviews table. This file has functions that combine values and commands to create new review entry, edit a specific review entry's rating using the entry Id, edit a specific reviews entry's content using the entry Id, edit a specific reviews entry's text using the entry Id, edit a specific reviews entry's noise level using the entry Id, edit a specific reviews entry's crowdedness level using the entry Id, and delete an entry using the entry Id.


**Review operations**  
**Defines the functions**
1. creating a review
2. editing a review's rating
3. editing review text
4. editing a review's noise level
5. editing a review’s crowdedness level
6. deleting a review
---

- SpotDB.py


**Overview**
This file creates SQL values and commands to send to the ExecuteDB file to do database operations for the study_spots table. This file has functions that combine values and commands to create a new spot entry, edit a specific spot entry's name using the entry ID, edit a specific spot entry's location using the entry ID, and delete an entry using the entry ID.


**Study spot operations**  
**Defines the functions**
1. creating a spot
2. editing a spot name
3. editing a spot location
4. deleting a spot
---

- UserDB.py


**Overview**
This file creates SQL values and commands to send to the ExecuteDB file to do database operations for the users table. This file has functions that combine values and commands to create a new user entry, edit a specific user entry's username using the entry ID, edit a specific spt entry's favorite study spot using the entry ID, and delete an entry using the entry ID.


**User operations**  
**Defines the functions**
1. creating a user
2. editing a username
3. editing a user's favorite study spot
4. deleting a user
---



## How we implemented it


This implementation was done with asynchronous and synchronous communication between team members. For the initial design of the models and database classes, there was active communication through a Discord call to decide on SQL parameters and their data type. From there, tasks were assigned and communication was asynchronous, so each member was assigned a specific task, and upon completion, they would notify other members.


## How it connects to the overall system Design
We have established the foundation of the Model-View-Controller architectural pattern we chose for our system design. For the models, we created User.py, Spot.py, and Review.py. The classes created inside these form the data structure with which we store all information about users, study spots, and reviews. UserDB.py, SpotDB.py, ReviewDB.py, and ExecuteDB.py handle the operations on these models, such as creation, editing, and deletion. With this element established, we are in a good position to implement views in the form of a user UI and controllers to connect between user actions on the UI and model operations. 


This implementation serves as a starting point for the backend of the study spot finder application. It handles the database operations for persistent storage across user sessions and for public information displayed in the application. We followed the behavioral design practice of distributing responsibility. In this case, each Python file handles the responsibility of one type of data entry in the database. So, user, review, and spot operations are handled separately. Responsibility is distributed across separate layers, such as the models, database operations, and main.py. Furthermore, it enables the development of frontend features such as the creation of user reviews and the addition of study spot creation on admin accounts. 

