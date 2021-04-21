from django.db import models

class Applicant(models.Model):
    """Соискатель"""
    full_name = models.CharField('ФИО', max_length=200)
    telephone_number = models.IntegerField('номер телефона', null=True)
    position = models.CharField('должность', max_length=200)
    date_of_interview = models.DateField('дата собеседования', null=True)
    duration = models.IntegerField('срок задания', null=True)
    interviewer_name = models.CharField('руководитель', max_length=200)
    interviewer_position = models.CharField('Должность руководителя', max_length=200)

    def __str__(self):
        return f"{self.interviewer_name}"

class Mark(models.Model):
    """Отметка о получении задания"""
    text = models.TextField('отметка')
    created = models.DateField('дата', db_index=True)
    interviewer_name = models.ForeignKey(Applicant, verbose_name='руководитель', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.applicant.full_name}"