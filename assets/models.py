from django.db import models


# Create your models here.

class Assets(models.Model):
    asset_type_choices = (
        ('server', u'物理机'),
        ('server', u'虚拟机'),
    )
    STATUS_CHOICES = (
        ("ok", "ok"),
        ("repair", "repair"),
        ("withdraw", "withdraw"),
    )
    asset_type = models.CharField(verbose_name='资产类型', max_length=64, choices=asset_type_choices, default='server')
    hostname = models.CharField(max_length=32, unique=True)
    idc = models.CharField(verbose_name='机房', max_length=32, unique=True)
    #电信IP
    tel_ip = models.CharField(max_length=64, null=True, blank=True, verbose_name='电信IP')
    #联通IP
    uni_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name='联通IP')
    #移动IP
    mob_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name='移动IP')

    # fqdn_ip4
    internal_ip = models.GenericIPAddressField(max_length=32, verbose_name='内网IP')
    # cpu_model
    cpu_model = models.CharField(max_length=64, null=True, blank=True, verbose_name='CPU 型号')
    # num_cpus
    cpu_count = models.CharField(max_length=32, null=True, verbose_name='CPU 逻辑个数')
    # memory total
    mem_total = models.CharField(max_length=64, null=True, blank=True, verbose_name='总内存MB')
    # os
    os = models.CharField(max_length=128, null=True, blank=True, verbose_name='操作系统')
    # osrelease
    os_version = models.CharField(max_length=16, null=True, blank=True, verbose_name='os版本')

    salt_state = models.TextField(blank=True, verbose_name='salt状态')
    asset_state = models.CharField(max_length=128, default="ok", choices=STATUS_CHOICES, verbose_name="主机状态")

    comment = models.TextField(blank=True, verbose_name="备注")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    mod_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = '主机信息'

    def __str__(self):
        return self.hostname


class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name="机房名",unique=True,help_text="机房名")
    idc_flag = models.CharField(max_length=32,verbose_name="机房标识",unique=True)
    address = models.CharField(max_length=128, null=True,blank=True,verbose_name="机房地址",help_text="机房地址")
    tel_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="电信IP段",help_text="电线IP段")
    mob_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="移动IP段",help_text="移动IP段")
    uni_ip = models.CharField(max_length=64,null=True,blank=True,verbose_name="联通IP段",help_text="联通IP段")
    dns = models.CharField(max_length=64,null=True,blank=True,verbose_name="DNS",help_text="DNS")
    email = models.EmailField(verbose_name="email地址")
    comment = models.TextField(blank=True,verbose_name="备注",help_text="备注")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间",help_text="添加时间")
    mod_time = models.DateTimeField(auto_now=True,verbose_name="修改时间",help_text="修改时间")

    class Meta:
        verbose_name="IDC机房"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


