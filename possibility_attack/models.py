from django.db import models
from users.models import Users

class Heart(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    sex = models.IntegerField(null=False, blank=False)
    cp = models.IntegerField(null=False, blank=False)
    trtbps = models.IntegerField(null=False, blank=False)
    chol = models.IntegerField(null=False, blank=False)
    fbs = models.IntegerField(null=False, blank=False)
    restecg = models.IntegerField(null=False, blank=False)
    thalachh = models.IntegerField(null=False, blank=False)
    exng = models.IntegerField(null=False, blank=False)
    oldpeak = models.FloatField(null=False, blank=False)
    slp = models.IntegerField(null=False, blank=False)
    caa = models.IntegerField(null=False, blank=False)
    thall = models.IntegerField(null=False, blank=False)
    output = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'heart'

    def __int__(self):
        return self.user_id
