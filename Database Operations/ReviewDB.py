import mysql.connector
from Models.Review import Review
from Models.User import User
from Models.Spot import Spot
from ExecuteDB import execute_DBOperation

create_review = ("INSERT INTO spotReviews "
                "(spotID, userID, noiseLevel, crowdedness, content) "
                "VALUES (%s, %s, %s, %s, %s)")

#
edit_review_rating = "UPDATE spotReviews SET rating = %s WHERE reviewID = %s"
edit_review_content = "UPDATE spotReviews SET content = %s WHERE reviewID = %s"
edit_review_noiseLevel = "UPDATE spotReviews SET noiseLevel = %s WHERE reviewID = %s"
edit_review_crowdedness = "UPDATE spotReviews SET crowdedness = %s WHERE reviewID = %s"

delete_spot = "DELETE from spotReviews WHERE reviewID = %s"


class ReviewDB:
        

    def create_review(rating: float, noiseLevel: int, content: str, crowdedness: int, user: User, spot: Spot):
        value = (f"{spot.spotID}", f"{user.userID}", f"{noiseLevel}", f"{crowdedness}", f"{content}")
        execute_DBOperation(create_review, value)
        

    def edit_review_rating(review: Review, rating: float):
        value = (f"{rating}", f"{review.reviewID}")
        execute_DBOperation(edit_review_rating, value)


    def edit_review_content(review: Review, content: str):
        value = (f"{content}", f"{review.reviewID}")
        execute_DBOperation(edit_review_content, value)


    def edit_review_noiseLevel(review: Review, noiseLevel: int):
        value = (f"{noiseLevel}", f"{review.reviewID}")
        execute_DBOperation(edit_review_noiseLevel, value)

    
    def edit_review_crowdedness(review: Review, crowdedness: int):
        value = (f"{crowdedness}", f"{review.reviewID}")
        execute_DBOperation(edit_review_crowdedness, value)

    def delete_review(review: Review):
        value = (f"{review.reviewID}")
        execute_DBOperation(delete_spot, value)
    