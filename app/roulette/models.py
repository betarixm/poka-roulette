from django.db import models
from datetime import datetime


class Round(models.Model):
    name = models.CharField(verbose_name="라운드", max_length=20)
    start_time = models.DateTimeField(verbose_name="시작 시각")
    end_time = models.DateTimeField(verbose_name="끝 시각")

    def is_valid_time(self, t: datetime):
        if self.start_time <= t <= self.end_time:
            return True
        return False

    class Meta:
        verbose_name = "라운드"
        verbose_name_plural = "라운드들"
        ordering = ['start_time']

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(verbose_name="아이템 이름", max_length=100)
    probability = models.DecimalField(verbose_name="확률 (0~1)", max_digits=10, decimal_places=9)
    num = models.IntegerField(verbose_name="재고")
    users = models.ManyToManyField('core.User', verbose_name="당첨자", blank=True)
    img = models.CharField(verbose_name="이미지 이름", max_length=100)

    def is_remained(self):
        if self.num <= 0:
            return False
        else:
            return True

    def win(self, user):
        self.users.add(user)
        self.num -= 1
        self.save()

    def percent(self):
        return self.probability * 100

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = "상품들"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
