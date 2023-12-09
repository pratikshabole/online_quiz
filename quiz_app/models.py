from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuizCategory(models.Model):
    title = models.CharField(max_length=25)
    details = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField(max_length=250)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question

class SubmitAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Submit Answers'