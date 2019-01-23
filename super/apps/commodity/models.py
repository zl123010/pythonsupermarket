from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
# 商品分类表
from DB.base_model import BaseModel

is_on_sale_choices = (
    (False, "下架"),
    (True, "上架"),
)


class ComClassModel(BaseModel):
    class_name = models.CharField(
        max_length=50,
        verbose_name="分类名称",
        validators=[MinLengthValidator(2)],
    )
    class_intro = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="分类简介"
    )

    class Meta:
        db_table = 'ComClassModel'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name


class ComSpuModel(BaseModel):
    SPU_name = models.CharField(max_length=50,
                                validators=[MinLengthValidator(2)],
                                verbose_name='spu名称')
    SPU_details = models.CharField(max_length=255,
                                   validators=[MinLengthValidator(2)],
                                   verbose_name='spu详情')

    class Meta:
        db_table = 'ComSpuModel'
        verbose_name = '商品SPU表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.SPU_name


class UnitModel(BaseModel):
    unit = models.CharField(max_length=10,
                            verbose_name='单位')

    class Meta:
        db_table = 'UnitModel'
        verbose_name = '商品单位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.unit


class ComSkuModel(BaseModel):
    Sku_name = models.CharField(max_length=50,
                                validators=[MinLengthValidator(2)],
                                verbose_name='商品名')
    comintro = models.CharField(max_length=100,
                                validators=[MinLengthValidator(2)],
                                verbose_name='商品简介')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='价格')
    stock = models.PositiveIntegerField(verbose_name='库存')
    sales = models.PositiveIntegerField(verbose_name='销量')
    logo = models.ImageField(verbose_name='封面图片', upload_to='logo/%Y%m/%d')
    is_on_sale = models.BooleanField(verbose_name="是否上架",
                                     choices=is_on_sale_choices, default=False)
    Comclass = models.ForeignKey(to="ComClassModel",
                                 verbose_name="商品分类")
    Com_spu = models.ForeignKey(to="ComSkuModel", verbose_name="商品SPU")

    def __str__(self):
        return self.Sku_name

    class Meta:
        verbose_name = "商品SKU管理"
        verbose_name_plural = verbose_name


class GalleryModel(BaseModel):
    img_url = models.ImageField(verbose_name='图集图片地址', upload_to='gallery/%Y%m/%d')
    com_sku = models.ForeignKey(to='ComSkuModel', verbose_name='商品SKU')

    class Meta:
        verbose_name = '商品图集管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "商品图集:{}".format(self.img_url.name)


class BannerModel(BaseModel):
    name = models.CharField(verbose_name="轮播活动",
                            max_length=50, )
    img_url = models.ImageField(verbose_name="轮播图片地址",
                                upload_to='banner/%Y%m/%d')
    order = models.SmallIntegerField(verbose_name="排序", default=0)
    com_sku = models.ForeignKey(to="ComSkuModel", verbose_name="商品SKU")

    class Meta:
        verbose_name = "轮播管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ActivityModel(BaseModel):
    Activi_name = models.CharField(verbose_name='活动名称', max_length=50)
    Activi_image = models.ImageField(verbose_name='活动图片地址', upload_to='activity/%Y%m/%d')
    Activi_url = models.URLField(verbose_name='活动的url地址', max_length=255)

    def __str__(self):
        return self.Activi_name

    class Meta:
        verbose_name = '活动管理'
        verbose_name_plural = verbose_name


class ActivityZoneModel(BaseModel):
    AZ_name = models.CharField(verbose_name="活动专区名称", max_length=50)
    AZ_intro = models.CharField(verbose_name="活动专区简介", max_length=255, null=True, blank=True)
    AZ_order = models.SmallIntegerField(verbose_name="排序",default=0 )
    is_on_sale = models.BooleanField(verbose_name="是否上线",choices=is_on_sale_choices,default=0)
    com_sku = models.ManyToManyField(to="ComSkuModel",verbose_name="商品")
    def __str__(self):
        return self.AZ_name
    class Meta:
        verbose_name = "活动专区管理"
        verbose_name_plural  = verbose_name
