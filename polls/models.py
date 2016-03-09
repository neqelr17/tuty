"""polls app modles"""

from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """question model"""

    def __str__(self):
        """string method"""
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def was_published_recently(self):
        """practice function"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """choice model"""

    def __str__(self):
        """string method"""
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
