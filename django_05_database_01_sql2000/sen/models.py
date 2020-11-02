from django.db import models

# Create your models here.
class Jfxx(models.Model):
    """
    机房信息
    """
    lsid = models.IntegerField(db_column='Lsid', verbose_name='流水ID')
    jfid = models.CharField(db_column='Jfid', primary_key=True, max_length=20, verbose_name='机房ID')
    jfmc = models.CharField(db_column='Jfmc', max_length=50, verbose_name='机房名称')
    dwdm = models.CharField(db_column='Dwdm', max_length=10, verbose_name='单位代码')
    # jfbz = models.CharField(db_column='Jfbz', max_length=50, blank=True, null=True, verbose_name='None')

    class Meta:
        managed = False
        db_table = 't_jf_jfxx'