from django.db import models



class Clubs(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128, unique=True)
    shrt_name = models.CharField(verbose_name='Сокращенное Название', max_length=128, unique=True)
    email = models.EmailField(verbose_name='почта', blank=True)
    o_p_f = models.CharField(verbose_name='Форма', max_length=128, blank=True)
    jur_addr = models.CharField(verbose_name='Офиц. Адрес', max_length=128, blank=True)
    fact_addr = models.CharField(verbose_name='Факт. Адрес', max_length=128, blank=True)
    site = models.URLField(verbose_name='Сайт', blank=True)
    inn  = models.DecimalField(verbose_name='ИНН',decimal_places=0, max_digits=10, default=0)
    ogrn = models.DecimalField(verbose_name='ОГРН',decimal_places=0, max_digits=13, default=0)
    bank_name = models.CharField(verbose_name='Имя Банка', max_length=128, blank=True)
    check_ac = models.CharField(verbose_name='Расчетный счет', max_length=20, blank=True)
    ustav = models.FileField(verbose_name='Устав',upload_to='clubs_documents', blank=True)
    reg_in_min_just = models.FileField(verbose_name='МинЮст',upload_to='clubs_documents', blank=True)
    reg_in_tax = models.FileField(verbose_name='Налоговая',upload_to='clubs_documents', blank=True)
    creat_club = models.FileField(verbose_name='Создание',upload_to='clubs_documents', blank=True)
    creat_rucovod = models.FileField(verbose_name='Руководитель',upload_to='clubs_documents', blank=True)
    ofice = models.FileField(verbose_name='Офис',upload_to='clubs_documents', blank=True)
    Attempt = 'Допущен'
    NotAttempt = 'Не Допущен'
    STATUS = [
        (Attempt, ('Допущен до соревнования')),
        (NotAttempt, ('Не допущен до соревнования')),
    ]
    status = models.CharField(verbose_name='Статус',max_length=32,choices=STATUS, default=NotAttempt)
    notes = models.TextField(verbose_name='Примечание', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.ustav.__dict__['field'].upload_to=f'clubs/{self.shrt_name}/clubs_documents'
        self.reg_in_min_just.__dict__['field'].upload_to = f'clubs/{self.shrt_name}/clubs_documents'
        self.reg_in_tax.__dict__['field'].upload_to = f'clubs/{self.shrt_name}/clubs_documents'
        self.creat_club.__dict__['field'].upload_to = f'clubs/{self.shrt_name}/clubs_documents'
        self.creat_rucovod.__dict__['field'].upload_to = f'clubs/{self.shrt_name}/clubs_documents'
        self.ofice.__dict__['field'].upload_to = f'clubs/{self.shrt_name}/clubs_documents'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.shrt_name

    class Meta:
        verbose_name = 'клуб'
        verbose_name_plural = 'клубы'




