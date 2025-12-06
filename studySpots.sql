-- Create Study Spots table
DROP table if exists study_spots;
CREATE TABLE study_spots (
    spotID INT PRIMARY KEY AUTO_INCREMENT,
    spotName VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL
    /* createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP */
);
-- Create Users table
DROP table if exists users;
CREATE TABLE users (
    userID INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    hashedPassword VARCHAR(255) NOT NULL,
    favoriteStudySpot INT,
    kudos INT DEFAULT 0,
    /* createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, */
    FOREIGN KEY (favoriteStudySpot) REFERENCES study_spots(spotID) ON DELETE SET NULL
);

-- Create Spot Reviews table
DROP table if exists spot_reviews;
CREATE TABLE spot_reviews (
    reviewID INT PRIMARY KEY AUTO_INCREMENT,
    spotID INT NOT NULL,
    userID INT NOT NULL,
    noiseLevel INT NOT NULL CHECK (noiseLevel BETWEEN 0 AND 10),
    crowdedness INT NOT NULL CHECK (crowdedness BETWEEN 0 AND 10),
    starRating INT NOT NULL CHECK (starRating BETWEEN 0 AND 5),
    reviewText VARCHAR(1000),
    /* createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, */
    FOREIGN KEY (spotID) REFERENCES study_spots(spotID) ON DELETE CASCADE,
    FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE,
    -- Ensure only one active review per user per spot
    UNIQUE KEY unique_user_spot_review (userID, spotID)
);