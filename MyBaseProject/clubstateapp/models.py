from datetime import date

from django.db import models

from clubsapp.models import Clubs


class ClubsState(models.Model):
    club=models.ForeignKey(
        Clubs,
        verbose_name='клуб',
        on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name='Имя', max_length=128)
    secondname = models.CharField(verbose_name='Фамилия', max_length=128)
    patrom  = models.CharField(verbose_name='Отчество', max_length=128)
    phone = models.CharField(verbose_name='Телефон', max_length=128)
    email = models.EmailField(verbose_name='почта', blank=True)
    post = models.CharField(verbose_name='должность',max_length=128)
    doc_of_study = models.FileField(verbose_name='Лицензия/Документ об образовании',upload_to='clubs state documents', blank=True)
    licence_under = models.DateField(verbose_name='Лицензия до', default=date(1,1,1))
    notes = models.TextField(verbose_name='Примечание', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.doc_of_study.__dict__['field'].upload_to=f'clubs/{self.club.shrt_name}/states_documents/{self.secondname} {self.post}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.secondname} {self.name} {self.post}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
