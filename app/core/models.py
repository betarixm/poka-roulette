from django.db import models


class User(models.Model):
    povis_id = models.CharField(verbose_name="POVIS ID", max_length=100)
    rounds = models.ManyToManyField('roulette.Round', verbose_name="참여한 라운드", blank=True)

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저들"
        ordering = ['povis_id']

    def __str__(self):
        return self.povis_id

    def __repr__(self):
        return self.povis_id

    def is_joined_round(self, target_round):
        if self.rounds.filter(id=target_round.id).count() == 0:
            return False
        else:
            return True

    def join_round(self, target_round):
        self.rounds.add(target_round)

    @classmethod
    def create(cls, povis_id):
        user = cls(povis_id=povis_id)
        return user
