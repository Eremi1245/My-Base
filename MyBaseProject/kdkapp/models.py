from django.db import models

from clubsapp.models import Clubs


class Kdk(models.Model):
    date_meeting  = models.DateField(verbose_name='Дата Заседания', unique=True)
    notes = models.TextField(verbose_name='Примечание', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заседание {self.date_meeting}'

    class Meta:
        verbose_name = 'Заседание'
        verbose_name_plural = 'Заседания'

class Cases(models.Model):
    Kdk_id = models.ForeignKey(Kdk,
                              verbose_name='Дата Заседания',
                              on_delete=models.CASCADE
                              )
    case_number = models.CharField(verbose_name='номер дела',unique=True)
    time_meeting = models.TimeField(verbose_name='Время')
    potential_art = models.CharField(verbose_name='Статьи нарушений')

    notes = models.TextField(verbose_name='Примечание', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заседание {self.date_meeting}: {self.case_number}'

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'


# class Clubs_Case(models.Model):
#     case = models.ForeignKey(Cases,
#                              on_delete=models.CASCADE,
#                              verbose_name='Дело'
#                              )
#
#     club= models.ForeignKey(Clubs,
#                               verbose_name='Клуб 1',
#                               on_delete=models.CASCADE
#                               )
#     def __str__(self):
#         return f'Заседание {self.case}: {self.club.shrt_name}'
#
#     class Meta:
#         verbose_name = 'Клубы-Дела'
#         verbose_name_plural = 'Дела'