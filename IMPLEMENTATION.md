# Implementation


## Implemented : 

### Identifying Object Classes for User, Spot, and Review.

- Review.py
**Represents the text review comment on a spot that is left by a user**
Contains a unique ID for the review. Information fields about the spot, such as: Star Rating, ContentNoise Level, Crowdedness; and the associated User and Spot.

- Spot.py
**Represents the Study spot**
Contains a unique ID for the spot. Information fields: Name of the spot, Location of the spot

- User.py 
**Represents the user**
Contains a unique ID for the user. Information fields: Username, email, password, favorite spot, kudos level

### Database Operation Files for User, Spot, and Review. 

- ReviewDB.py
**Review operations**
Defines the functions
---
1. creating a review
2. editing a review's rating
3. editing review text
4. editing a review's noise level
5. edit a review crowdedness level
6. deleting a review

- SpotDB.py
**Study spot operations**
Defines the functions
---
1. creating a spot
2. editing a spot name
3. editing a spot location
4. deleting a spot

- UserDB.py 
**User operations**
Defines the functions 
---
1. creating a user
2. editing a username
3. editing a user's favorite study spot
4. deleting a user


## How we implemented it

