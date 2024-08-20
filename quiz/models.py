from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model()

# Create your models here.
class categories(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    categories= models.ForeignKey(categories, verbose_name=("categories of quiz"), on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    text= models.TextField()
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quesions')
    difficulty= models.IntegerField(default=1, choices=((1, 'Easy'), (2, 'Medium'), (3, 'Hard')))

    def __str__(self):
        return self.text
    
class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    text= models.TextField()
    is_correct= models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizTaker(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score= models.IntegerField(default=0)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

class Response(models.Model):
    quiz_taker= models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer= models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        self.quiz_taker.user.first_name

    # def is_correct(self):
    #     if self.selected_answer:
    #         return self.selected_answer.is_correct
    #     return False
