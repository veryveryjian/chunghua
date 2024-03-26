from django.db import models
from django.db import models
from django.views.generic import ListView



class Msavg(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    avg_2022 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msavg'



class Item(models.Model):
    name = models.CharField(max_length=255)  # 'Unnamed: 0' 컬럼에 대응
    on_hand = models.FloatField()            # 'On Hand' 컬럼에 대응
    color_code = models.CharField(max_length=255, blank=True, null=True)  # 새로운 필드
    model_code = models.CharField(max_length=255, blank=True, null=True)  # 새로운 필드

    def __str__(self):
        return self.name




# class Item(models.Model):
#     name = models.CharField(max_length=255)  # Unnamed: 0 컬럼에 대응
#     on_hand = models.FloatField()            # On Hand 컬럼에 대응
#
#     def __str__(self):
#         return self.name

class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Cbm(models.Model):
    model_code = models.CharField(max_length=50, primary_key=True)
    cbm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbm'






# class Cbm(models.Model):
#     model_code = models.CharField(max_length=50, blank=True, null=True)
#     cbm = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cbm'




class MsRoom(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    model_code = models.CharField(max_length=50, blank=True, null=True)
    ny = models.IntegerField(blank=True, null=True)
    nj = models.IntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pa = models.IntegerField(blank=True, null=True)
    number_275 = models.IntegerField(db_column='275', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_room'



class Newtable4(models.Model):
    item = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    jin_348_ms = models.IntegerField(db_column='JIN#348-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_349_ms = models.IntegerField(db_column='JIN#349-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_352_ms = models.IntegerField(db_column='JIN#352-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_353_ms = models.IntegerField(db_column='JIN#353-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_354_ms = models.IntegerField(db_column='JIN#354-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_355_ms = models.IntegerField(db_column='JIN#355-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_356_ms = models.IntegerField(db_column='JIN#356-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_357_ms = models.IntegerField(db_column='JIN#357-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_358_ms = models.IntegerField(db_column='JIN#358-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_359_ms = models.IntegerField(db_column='JIN#359-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_360_ms = models.IntegerField(db_column='JIN#360-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_361_ms = models.IntegerField(db_column='JIN#361-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_362_ms = models.IntegerField(db_column='JIN#362-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_363_ms = models.IntegerField(db_column='JIN#363-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_364_ms = models.IntegerField(db_column='JIN#364-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_365_ms = models.IntegerField(db_column='JIN#365-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_366_ms = models.IntegerField(db_column='JIN#366-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_373_ms = models.IntegerField(db_column='JIN#373-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_374_ms = models.IntegerField(db_column='JIN#374-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_375_ms = models.IntegerField(db_column='JIN#375-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jin_376_ms = models.IntegerField(db_column='JIN#376-MS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    available = models.IntegerField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    available = models.IntegerField(blank=True, null=True)
    order = models.CharField(db_column='Order', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_po = models.IntegerField(db_column='On PO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorder_qty = models.IntegerField(db_column='Reorder Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_deliv = models.CharField(db_column='Next Deliv', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_week = models.IntegerField(db_column='Sales/Week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ny_inv'


