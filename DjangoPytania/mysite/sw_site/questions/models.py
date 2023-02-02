from django.db import models

# Create your models here.

class Question(models.Model):
    number_of_question = models.PositiveIntegerField(primary_key=True, unique=True)
    question_content = models.TextField(max_length=1000)
    answer_a = models.TextField(max_length=250)
    answer_b = models.TextField(max_length=250)
    answer_c = models.TextField(max_length=250)
    a_is_correct = models.BooleanField()
    b_is_correct = models.BooleanField()
    c_is_correct = models.BooleanField()
    question_notes = models.TextField(max_length=1000)


    def check_answers(self, user_answers):
        proper_answers = [self.a_is_correct, self.b_is_correct, self.c_is_correct]
        print(self.number_of_question)
        print(proper_answers)
        print(user_answers)
        return proper_answers == user_answers

    # def __str__(self):
    #     return f"Pytanie nr {self.number_of_question}"

    def create_question(self, question_listed):
        self.number_of_question = question_listed[0]
        self.question_content = question_listed[1]
        self.answer_a = question_listed[2]
        self.answer_b = question_listed[3]
        self.answer_c = question_listed[4]
        self.a_is_correct = "a" in question_listed[5]
        self.b_is_correct = "b" in question_listed[5]
        self.c_is_correct = "c" in question_listed[5]
        self.question_notes = question_listed[6]


class Answer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_question = models.PositiveIntegerField()
    answer_a = models.BooleanField(blank=True)
    answer_b = models.BooleanField(blank=True)
    answer_c = models.BooleanField(blank=True) 
    answer_is_proper = models.BooleanField()
