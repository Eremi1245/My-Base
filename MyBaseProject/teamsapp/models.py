from django.db import models

from clubsapp.models import Clubs

from stadiumsapp.models import Stadiums


class Teams(models.Model):
    club=models.ForeignKey(Clubs,
                           on_delete=models.CASCADE,
                           verbose_name='Клуб',
    )
    name=models.CharField(verbose_name='отделение',max_length=32)
    place_of_match=models.ForeignKey(Stadiums,
                                     on_delete=models.CASCADE,
                                     verbose_name='Место проведения матчей',
                                     default=1)
    football_field=models.CharField(verbose_name='Номер поля',max_length=32,default='единственное поле')
    club_league = 'Клубная Лига'
    first_league = 'Первая Лига'
    second_league = 'Вторая Лига'
    third_league = 'Третья Лига'
    fouth_league = 'Четвертая Лига'
    fifth_league = 'Пятая Лига'
    div_a = 'Дивизион А'
    div_b = 'Дивизион Б'
    league = [
        (club_league, ('Клубная Лига')),
        (first_league, ('Первая Лига')),
        (second_league, ('Вторая Лига')),
        (third_league, ('Третья Лига')),
        (fouth_league, ('Четвертая Лига')),
        (fifth_league, ('Пятая Лига')),
        (div_a, ('Дивизион А')),
        (div_b, ('Дивизион Б')),
    ]
    leagues = models.CharField(verbose_name='Лига',
                                max_length=32,
                                choices=league,
                                default='Нет данных')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'отделения'




