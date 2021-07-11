from django.db import models

from clubsapp.models import Clubs

from clubstateapp.models import ClubsState


class Cases(models.Model):
    date_meeting = models.DateField(verbose_name='Дата Заседания')
    time_meeting = models.TimeField(verbose_name='Время')
    case_number = models.CharField(verbose_name='номер дела', max_length=128, unique=True)
    potential_art = models.CharField(verbose_name='Статьи нарушений', max_length=128)
    club_1 = models.ForeignKey(Clubs,
                               on_delete=models.CASCADE,
                               verbose_name='Клуб')
    participant = models.ForeignKey(ClubsState,
                                    on_delete=models.CASCADE,
                                    verbose_name='Участник')

    notes = models.TextField(verbose_name='Примечание', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заседание {self.date_meeting}: {self.case_number}'

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'
