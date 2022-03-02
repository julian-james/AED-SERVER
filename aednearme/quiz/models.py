from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):

    quiz_subject = models.CharField(max_length=50)
    
    question_1 = models.TextField()
    question_2 = models.TextField()
    question_3 = models.TextField()
    question_4 = models.TextField()
    question_5 = models.TextField()
    question_6 = models.TextField()

    correct_answer_1 = models.TextField()
    correct_answer_2 = models.TextField()
    correct_answer_3 = models.TextField()
    correct_answer_4 = models.TextField()
    correct_answer_5 = models.TextField()
    correct_answer_6 = models.TextField()

    incorrect_answers_1 = models.TextField()
    incorrect_answers_2 = models.TextField()
    incorrect_answers_3 = models.TextField()
    incorrect_answers_4 = models.TextField()
    incorrect_answers_5 = models.TextField()
    incorrect_answers_6 = models.TextField()

    def __str__(self):
        return f'Quiz_ID: {self.id}, Quiz_Subject: {self.quiz_subject}, question_1: {self.question_1}, Correct_Answer_1: {self.correct_answer_1}, incorrect_answers_1: {self.incorrect_answers_1}'  

class User_Quiz(models.Model):

    completed = models.BooleanField(default=False)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'User_Quiz_ID: {self.id}, Quiz_ID: {self.quiz_id}, User_ID: {self.user_id}, Completed: {self.completed}'  

    


