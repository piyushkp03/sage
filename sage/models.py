from django.db import models

# Create your models here.

class noti(models.Model):
    email=models.CharField(max_length=500,default="")
    date=models.CharField(max_length=500,default="")
    time=models.CharField(max_length=500,default="")
    hname=models.CharField(max_length=500,default="")
    vname=models.CharField(max_length=500,default="")
    def __str__(self):
        return self.hname

class vmain(models.Model):
    hname=models.CharField(max_length=500)
    himage=models.ImageField(upload_to="byimgs",default="")
    haddr=models.CharField(max_length=500, default="")
    hphone = models.CharField(max_length=100, default="")
    hmap= hlink=models.CharField(max_length=500, default="")
    hlink=models.CharField(max_length=500, default="")
    hcordinate=models.CharField(max_length=50,default="")
    hdis = models.FloatField(null=True, blank=True)
    htiming=models.CharField(max_length=100, default="")
    hclosed=models.CharField(max_length=50, default="")
    city=models.CharField(max_length=40)
    # hname=models.CharField(max_length=40)
    vname=models.CharField(max_length=69)
    nov = models.FloatField(null=True, blank=True, default = "")
    vprice = models.FloatField(null=True, blank=True, default = "")
    def __str__(self):
        return self.hname

class vaccinename(models.Model):
    srno = models.FloatField(null=True, blank=True, default = "")
    vyear1=models.CharField(max_length=40)
    vname=models.CharField(max_length=69)
    def __str__(self):
        return self.vname

class bhyhospital(models.Model):
    hname=models.CharField(max_length=40)
    himage=models.ImageField(upload_to="byimgs",default="")
    haddr=models.CharField(max_length=100, default="")
    hphone = models.CharField(max_length=100, default="")
    hmap= hlink=models.CharField(max_length=50, default="")
    hlink=models.CharField(max_length=50, default="")
    hcordinate=models.CharField(max_length=50,default="")
    hdis = models.FloatField(null=True, blank=True)
    htiming=models.CharField(max_length=100, default="")
    hclosed=models.CharField(max_length=50, default="")

    def __str__(self):
        return self.hname




class vasaihospital(models.Model):
    hname = models.CharField(max_length=40)
    himage = models.ImageField(upload_to="byimgs", default="")
    haddr = models.CharField(max_length=100, default="")
    hphone = models.CharField(max_length=100, default="")
    hmap = hlink = models.CharField(max_length=50, default="")
    hcordinate = models.CharField(max_length=50, default="")
    hdis=models.FloatField(null=True, blank=True)
    hlink = models.CharField(max_length=50, default="")
    htiming = models.CharField(max_length=100, default="")
    hclosed = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.hname

