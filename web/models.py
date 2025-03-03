from django.db import models
from django.db import models
from py2neo import Graph
class DoctorInfo(models.Model):
    # 基本信息
    username = models.CharField(max_length=64, verbose_name='姓名')
    email = models.EmailField(max_length=64, unique=True, primary_key=True, verbose_name='邮箱')
    password = models.CharField(max_length=128, verbose_name='密码')
    gender = models.CharField(max_length=10, choices=[
        ('male', '男'),
        ('female', '女')
    ], verbose_name='性别')
    birth_date = models.DateField(verbose_name='出生日期')
    phone = models.CharField(max_length=11, verbose_name='联系电话')

    # 学历与专业背景
    education = models.CharField(max_length=20, choices=[
        ('bachelor', '学士'),
        ('master', '硕士'),
        ('doctor', '博士')
    ], verbose_name='最高学历')

    university = models.CharField(max_length=100, verbose_name='毕业院校')
    major = models.CharField(max_length=100, verbose_name='专业')
    experience = models.CharField(max_length=20, choices=[
        ('1-3', '1-3年'),
        ('3-5', '3-5年'),
        ('5-10', '5-10年'),
        ('10+', '10年以上')
    ], verbose_name='从业经验')

    # 执业信息
    license_number = models.CharField(max_length=50, unique=True, verbose_name='执业医师资格证号码')
    license_image = models.ImageField(upload_to='doctor_licenses/', verbose_name='资格证扫描件',null=True,blank=True)
    title = models.CharField(max_length=20, choices=[
        ('resident', '住院医师'),
        ('attending', '主治医师'),
        ('associate', '副主任医师'),
        ('chief', '主任医师')
    ], verbose_name='专业职称')

    # 科室（多选）可以使用 ManyToManyField 或者用 JSONField 存储列表
    departments = models.JSONField(verbose_name='执业科室')  # 存储科室列表
    workplace = models.CharField(max_length=200, verbose_name='执业地点')

    # 其他信息
    is_verified = models.BooleanField(default=False, verbose_name='是否已验证')
class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64,unique=True, primary_key=True)
    password = models.CharField(max_length=64)

class Reasoning(models.Model):
    id = models.IntegerField(primary_key = True)
    yc = models.CharField(max_length=64)
    gn = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    rank = models.CharField(max_length=64)
    score = models.CharField(max_length=64)

class Model(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    active = models.CharField(max_length=64)


class MedKG:
    def __init__(self):
        self.graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    def example(self):
        # cypher = "match (n1:Entity)-[rel]->(n2) return n1.ID,n2.ID,n1.name,rel.type,n2.name LIMIT 30"
        # cypher = "match (n1)-[rel]->(n2) return id(n1),id(n2),n1.name,type(rel),n2.name LIMIT 30 "
        cypher = "match (n1:人参)-[rel]-(n2) return id(n1),id(n2),n1.name,type(rel),n2.name,n1,n2 LIMIT 30"
        print(cypher)
        r = self.graph.run(cypher).data()
        return r

def ExampleShow():
    return MedKG().example()

