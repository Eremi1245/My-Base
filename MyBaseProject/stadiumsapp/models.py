from django.db import models


class Stadiums(models.Model):
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
    in_Reg_stad = models.FileField(verbose_name='Реестр Видов Спорта',upload_to='stadiums_documents', blank=True)
    conf_in_expluatation = models.FileField(verbose_name='Ввод в эксплуатац',upload_to='stadiums_documents', blank=True)
    instr_pub_order = models.FileField(verbose_name='Инструкция безопасности',upload_to='stadiums_documents', blank=True)
    instr_pub_order_date_until = models.DateField (verbose_name='Инструкция безопасности до',blank=True)
    act_categ = models.FileField(verbose_name='Акт категорирования',upload_to='stadiums_documents', blank=True)
    act_categ_date_until = models.DateField(verbose_name='Акт категорирования до', blank=True)
    statd_plan = models.FileField(verbose_name='План стадиона',upload_to='stadiums_documents', blank=True)
    category_RFS = models.FileField(verbose_name='Категория РФС',upload_to='stadiums_documents', blank=True)
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

    def __str__(self):
        return self.shrt_name

    class Meta:
        verbose_name = 'стадион'
        verbose_name_plural = 'стадионы'




