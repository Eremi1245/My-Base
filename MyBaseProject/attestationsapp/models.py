from datetime import date

from django.db import models

from clubsapp.models import Clubs
from stadiumsapp.models import Stadiums


class Attestations(models.Model):

    club = models.ForeignKey(Clubs,
                             verbose_name='Клуб',
                             on_delete=models.CASCADE
                             )

    stadium = models.ForeignKey(Stadiums,
                                verbose_name='Стадион',
                                on_delete=models.CASCADE
                             )
    _year=models.CharField(verbose_name='Год Аттестации',max_length=4)

    application_1  = models.FileField(verbose_name='Заявление о процедуре аттестации',
                                      upload_to='attestations_documents',
                                      blank=True)
    application_2  = models.FileField(verbose_name='Проведение политики недопущения дискриминации',
                                      upload_to='attestations_documents',
                                      blank=True)
    application_3  = models.FileField(verbose_name='Согласие на соблюдение регламентов',
                                      upload_to='attestations_documents',
                                      blank=True)
    application_4  = models.FileField(verbose_name='Список сотрудников',
                                      upload_to='attestations_documents',
                                      blank=True)
    application_5  = models.FileField(verbose_name='Гарантийное письмо',
                                      upload_to='attestations_documents',
                                      blank=True)
    rent,right_use,certif_of_ownership='аренда','Право оперативного пользования','Свидетельство о собственности'
    foundation_document= [
        (rent, ('Аренда')),
        (right_use, ('Право оперативного пользования')),
        (certif_of_ownership, ('Свидетельство о собственности'))
    ]
    document= models.CharField(verbose_name='Право пользования стадионом',
                               max_length=32,
                               choices=foundation_document,
                               default='Нет')
    document_upload = models.FileField(verbose_name='загрузить документ',
                     upload_to='attestations_documents',
                                       )
    document_under = models.DateField(verbose_name='Срок действия документа',default=date(1,1,1))

    notes = models.TextField(verbose_name='Примечание', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.application_1.__dict__['field'].upload_to=f'attestations' \
                                                       f'/{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}' \
                                                       f'/documents'
        self.application_2.__dict__['field'].upload_to = f'attestations' \
                                                       f'/{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}' \
                                                       f'/documents'
        self.application_3.__dict__['field'].upload_to = f'attestations' \
                                                       f'/{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}' \
                                                       f'/documents'
        self.application_4.__dict__['field'].upload_to = f'attestations' \
                                                       f'/{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}' \
                                                       f'/documents'
        self.application_5.__dict__['field'].upload_to = f'attestations' \
                                                       f'/{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}' \
                                                       f'/documents'
        self.document_upload.__dict__['field'].upload_to = f'attestations' \
                                                       f'/{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}' \
                                                       f'/documents'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.club.shrt_name}-{self.stadium.shrt_name} {self._year}'

    class Meta:
        verbose_name = 'Аттестация'
        verbose_name_plural = 'Аттестации'

