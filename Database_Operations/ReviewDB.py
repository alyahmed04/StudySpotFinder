from Models.Review import Review
from Models.User import User
from Models.Spot import Spot
from Database_Operations.ExecuteDB import execute_DBOperation


#Learned from the following sources about sql and mysqlconnector
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
#https://www.w3schools.com/python/python_mysql_update.asp
#https://www.red-gate.com/simple-talk/databases/mysql/modifying-mysql-data-from-within-python/

create_review = ("INSERT INTO spot_reviews "
                "(spotID, userID, noiseLevel, crowdedness, starRating, reviewText) "
                "VALUES (%s, %s, %s, %s, %s, %s)")

edit_review_rating = "UPDATE spot_reviews SET starRating = %s WHERE reviewID = %s"
edit_review_text = "UPDATE spot_reviews SET reviewText = %s WHERE reviewID = %s"
edit_review_noiseLevel = "UPDATE spot_reviews SET noiseLevel = %s WHERE reviewID = %s"
edit_review_crowdedness = "UPDATE spot_reviews SET crowdedness = %s WHERE reviewID = %s"

delete_review = "DELETE FROM spot_reviews WHERE reviewID = %s"


class ReviewDB:
        
    def create_review(starRating: int, noiseLevel: int, content: str, crowdedness: int, user: User, spot: Spot):
        value = (spot.spotID, user.userID, noiseLevel, crowdedness, starRating, content)
        execute_DBOperation(create_review, value)
        

    def edit_review_rating(review: Review, starRating: float):
        value = (starRating, review.reviewID)
        execute_DBOperation(edit_review_rating, value)


    def edit_review_text(review: Review, content: str):
        value = (content, review.reviewID)
        execute_DBOperation(edit_review_text, value)


    def edit_review_noiseLevel(review: Review, noiseLevel: int):
        value = (noiseLevel, review.reviewID)
        execute_DBOperation(edit_review_noiseLevel, value)

    
    def edit_review_crowdedness(review: Review, crowdedness: int):
        value = (crowdedness, review.reviewID)
        execute_DBOperation(edit_review_crowdedness, value)

    def delete_review(review: Review):
        value = (review.reviewID)
        execute_DBOperation(delete_review, value)
    