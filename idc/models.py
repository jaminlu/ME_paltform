from django.db import models


# Create your models here.


class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name="机房名",unique=True,help_text="机房名")
    idc_flag = models.CharField(max_length=32,verbose_name="机房标识",unique=True)
    address = models.CharField(max_length=128, null=True,blank=True,verbose_name="机房地址",help_text="机房地址")
    tel_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="电信IP段",help_text="电线IP段")
    mob_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="移动IP段",help_text="移动IP段")
    uni_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="联通IP段",help_text="联通IP段")
    dns_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="DNS",help_text="DNS")
    email = models.EmailField(verbose_name="email地址")
    comment = models.TextField(blank=True,verbose_name="备注",help_text="备注")
    #首次添加时间
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间",help_text="添加时间")
    #修改时间
    mod_time = models.DateTimeField(auto_now=True,verbose_name="修改时间",help_text="修改时间")

    class Meta:
        verbose_name="IDC机房"
        verbose_name_plural=verbose_name

    def __str__(self):
        return 'id:%s name:%s' %(self.id, self.name)


