import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, help_text="Enter the question text.")
    pub_date = models.DateTimeField("date published", help_text="Enter the date when the question was published.")

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now - datetime.timedelta(days=1) and self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, help_text="Enter the choice text.")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
