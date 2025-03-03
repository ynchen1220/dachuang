from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import *
import random
import json
import sys
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
sys.path.append("..")
from py2neo import Graph, Node
graph = Graph("http://localhost:7474", auth=("neo4j", "jiayi031220"))
import json
import os
import uuid
import time

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
from .models import DoctorInfo

def patientregister(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        e = request.POST.get('email')
        try:
            x = models.User.objects.get(email=e)
            return HttpResponse("n")
        except:
            new_user = models.User.objects.create(username=u, email=e, password=p)
            return HttpResponse("y")


def patientlogin(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        try:
            x = models.User.objects.get(email=e)
            if x.password == p:
                return HttpResponse("y")
            else:
                return HttpResponse("n")
        except:
            return HttpResponse("n")



def doctorregister(request):
    if request.method == 'POST':
        try:
            # 检查是否是 multipart/form-data 请求
            if request.content_type.startswith('multipart/form-data'):
                # 获取表单数据
                email = request.POST.get('email')
                password = request.POST.get('password')
                username = request.POST.get('username')
                gender = request.POST.get('gender')
                birth_date = request.POST.get('birth_date')
                phone = request.POST.get('phone')
                education = request.POST.get('education')
                university = request.POST.get('university')
                major = request.POST.get('major')
                experience = request.POST.get('experience')
                license_number = request.POST.get('license_number')
                title = request.POST.get('title')
                departments = json.loads(request.POST.get('departments', '[]'))
                workplace = request.POST.get('workplace')

                # 获取上传的文件
                license_image = request.FILES.get('license_image')

                if license_image:
                    # 生成唯一的文件名
                    # 获取原始文件扩展名
                    file_extension = os.path.splitext(license_image.name)[1]
                    # 生成唯一文件名：时间戳_uuid.扩展名
                    unique_filename = f"{int(time.time())}_{str(uuid.uuid4())[:8]}{file_extension}"

                    # 创建保存路径
                    save_path = os.path.join(settings.MEDIA_ROOT, 'doctor_licenses')
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)

                    # 构建文件完整路径
                    file_path = os.path.join(save_path, unique_filename)

                    # 保存文件
                    with open(file_path, 'wb+') as destination:
                        for chunk in license_image.chunks():
                            destination.write(chunk)

                    license_image.name = unique_filename

                # 检查邮箱是否已存在
                if DoctorInfo.objects.filter(email=email).exists():
                    return JsonResponse({'data': 'email_exists'})

                # 创建医生信息记录
                doctor = DoctorInfo(
                    username=username,
                    email=email,
                    password=password,  # 实际应用中应该加密存储
                    gender=gender,
                    birth_date=birth_date,
                    phone=phone,
                    education=education,
                    university=university,
                    major=major,
                    experience=experience,
                    license_number=license_number,
                    title=title,
                    departments=departments,
                    workplace=workplace,
                    is_verified=False  # 默认未验证
                )

                # 如果上传了文件，保存文件
                if license_image:
                    doctor.license_image = license_image
                    print("Image field set in model:", doctor.license_image.name)
                # 保存到数据库
                doctor.save()
                return HttpResponse("y")
            else:
                return HttpResponse("n")

        except Exception as e:
            print(f"Registration error: {str(e)}")
            return HttpResponse("n")
    return HttpResponse("n")

def doctorlogin(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        try:
            x = models.DoctorInfo.objects.get(email=e)
            if x.password == p and x.is_verified == 1:
                return HttpResponse("y")
            else:
                return HttpResponse("n")
        except:
            return HttpResponse("n")

#展示模型列表
def showModel(self):
    response = {}
    models = Model.objects.filter()
    response['list'] = json.loads(serializers.serialize("json", models))
    return JsonResponse(response)


# 删除模型
def delModel(request):
    response = {}
    model = Model.objects.get(name=request.GET.get('name'))  # 已存在
    model.delete()
    response['msg'] = 'success'
    response['error_num'] = 0
    return JsonResponse(response)

# 新增模型
def addModel(request):
    response = {}
    try:
        model = Model.objects.get(name=request.GET.get('name'))  # 已存在
        response['msg'] = 'fail'
        response['error_num'] = 1
    except Exception as e:
        model = Model(name=request.GET.get('name'), active=request.GET.get('active'))
        model.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    return JsonResponse(response)

# 展示用户列表
def showUser(self):
    response = {}
    try:
        users = User.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



# 新增用户
def addUser(request):
    response = {}
    try:
        user = User.objects.get(username=request.GET.get('username'))  # 已存在
        response['msg'] = 'fail'
        response['error_num'] = 1
    except Exception as e:
        user = User(username=request.GET.get('username'), password=request.GET.get('password'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    return JsonResponse(response)


# 删除用户
def delUser(request):
    response = {}
    user = User.objects.get(username=request.GET.get('username'))  # 已存在
    print(user.password)
    user.delete()
    response['msg'] = 'success'
    response['error_num'] = 0
    return JsonResponse(response)


# 修改用户
def modUser(request):
    response = {}
    username = request.GET.get('username')
    print(username)
    user = User.objects.get(username=username)  # 已存在
    print(user.password)
    User.objects.filter(username=request.GET.get('username')).update(
        password=request.GET.get('password'),
    )

    response['msg'] = 'success'
    response['error_num'] = 0
    return JsonResponse(response)


# 知识推理
def entityReasoning(request):
    entity_name = request.GET.get("entity_name", '')
    model = request.GET.get("model", '')
    reasonings = Reasoning.objects.filter(yc=entity_name,model=model)
    r_len = len(reasonings)
    response = {}
    result_list = []
    entity_list = []
    relation_list = []
    i = 2
    for reason in reasonings:
        result = {
            'id': '',
            'rank': '',
            'score': '',
            'herbs': '',
            'efficacy': '',
            'type': ''
        }
        n2_type = 0
        if reason.type == '1':
            n2_type = 1
        entity1 = {
            'id': str(1),
            'name': reason.yc,
            'category': 0,
        }
        entity2 = {
            'id': str(i),
            'name': reason.gn,
            'category': n2_type,
        }
        relation = {
            'source': str(1),
            'target': str(i),
            'value': '功效',
        }
        i += 1
        result['rank'] = reason.rank
        result['score'] = reason.score
        result['herbs'] = reason.yc
        result['efficacy'] = reason.gn
        result['type'] = reason.type
        result['id'] = reason.id
        result_list.append(result)
        if entity1 not in entity_list:
            entity_list.append(entity1)
        if entity2 not in entity_list:
            entity_list.append(entity2)
        if relation not in relation_list:
            relation_list.append(relation)

    response['result'] = result_list
    response['entity'] = entity_list
    response['relation'] = relation_list
    return JsonResponse(response)

#推理结果修改
def resoningMod(request):
    herbs = request.GET.get("herbs", '')
    efficacy = request.GET.get("efficacy", '')
    id = request.GET.get("id", '')
    reasoning = Reasoning.objects.get(id = int(id))
    reasoning.yc = herbs
    reasoning.gn = efficacy
    reasoning.save()
    response = {}
    response['msg'] = 'success'
    return JsonResponse(response)

#删除推理的知识
def reasoningDel(request):
    id = request.GET.get("id", '')
    Reasoning.objects.get(id=int(id)).delete()
    response = {}
    response['msg'] = 'success'
    return JsonResponse(response)




# 新增实体
def entityAdd(request):
    entity_name = request.GET.get("entity_name", '')
    print(entity_name)
    response = {}

    # count=random.randint(0,100)


    if (len(graph.run("MATCH (n:" + entity_name + ")RETURN n").data()) == 0):
        # node1 = Node('Entity', name=entity_name, synonyms='', C='', D='', ID='disease-{}'.format(count))
        # count += 1
        # graph.create(node1)
        graph.run("create (n:"+ entity_name +" {name:'"+ entity_name +"'})")
        response['msg'] = 'success'
    else:
        response['msg'] = 'fail'
    return JsonResponse(response)


# 删除实体
def entityDel(request):

    entity_name = request.GET.get("entity_name", '')
    print(entity_name)

    response = {}

    if (len(graph.run("MATCH (n:" + entity_name + ")RETURN n").data()) == 0):
        response['msg'] = 'fail'
    else:
        try:
            graph.run("MATCH (n:" + entity_name + ")DELETE n")
            response['msg'] = 'success'
        except Exception as e:
            response['msg'] = str(e)

    return JsonResponse(response)


# 修改实体
def entityMod(request):
    entity_name = request.GET.get("entity_name", '')
    entity_name_new = request.GET.get("entity_name_new", '')
    entity_type = request.GET.get("entity_type", '')
    entity_type_new = request.GET.get("entity_type_new", '')
    # entity_synonyms = request.GET.get("entity_synonyms", '')
    # entity_description = request.GET.get("entity_description", '')
    # print(
    #     entity_name + "<->" + entity_name_new + "<->" + entity_type + "<->" + entity_synonyms + "<->" + entity_description)
    # count = random.randint(0, 100)
    # entity_type_new = ''
    # if entity_type == '药物':
    #     entity_type_new = 'drug-{}'.format(count)
    # if entity_type == '基因':
    #     entity_type_new = 'gene-{}'.format(count)
    # if entity_type == '显性分子':
    #     entity_type_new = 'phenotype-{}'.format(count)
    # if entity_type == '蛋白质':
    #     entity_type_new = 'protein-{}'.format(count)
    # if entity_type == '小分子':
    #     entity_type_new = 'small_molecule-{}'.format(count)


    response = {}

    if (len(graph.run("MATCH (n:" + entity_name + ")RETURN n").data()) == 0):
        response['msg'] = 'notfind'
    elif (len(graph.run("MATCH (n:" + entity_name_new + ")RETURN n").data()) != 0):
        graph.run("MATCH (n:"+ entity_name_new +") set n = {category: '"+ entity_type_new +"',name: '"+entity_name_new +"'} return n")
        # response['msg'] = 'exist'
        response['msg'] = 'success'
    else:
        graph.run(
            "MATCH (n:"+entity_name+") remove n:"+entity_name+" set n:"+entity_name_new+", n={name:'"+entity_name_new+"',category:'"+ entity_type_new+"'} ")
        response['msg'] = 'success'
    return JsonResponse(response)


# 查找实体
def entityFind(request):
    entity_name = request.GET.get("entity_name", '')


    response = {}

    if (len(graph.run("MATCH (n:" + entity_name + ")RETURN n").data()) == 0):
        response['msg'] = 'fail'
    else:
        response['msg'] = 'success'
    return JsonResponse(response)


# 新增关系
def relAdd(request):
    entity1_name = request.GET.get("entity1_name", '')
    entity2_name = request.GET.get("entity2_name", '')
    rel = request.GET.get("rel", '')

    print(entity1_name + "<->" + rel + "<->" + entity2_name)

    response = {}

    if (len(graph.run("MATCH (n:" + entity1_name + ")RETURN n").data()) == 0):
        response['msg'] = 'e1 not find'
    elif (len(graph.run("MATCH (n:" + entity2_name + ")RETURN n").data()) == 0):
        response['msg'] = 'e2 not find'
    elif (len(graph.run(
            "MATCH (a:"+entity1_name+")-[r:"+rel+"]->(b:"+ entity2_name +")  RETURN r").data()) != 0):
        response['msg'] = 'exist'
    else:
        cypher = "MATCH (a:"+entity1_name+"),(b:"+ entity2_name +")  CREATE (a)-[r:" + rel + "]->(b) RETURN a,b "
        graph.run(cypher)
        response['msg'] = 'success'
    return JsonResponse(response)


# 删除关系
def relDel(request):
    entity1 = request.GET.get("entity1", '')
    entity2 = request.GET.get("entity2", '')
    rel = request.GET.get("rel", '')

    response = {}

    cypher = "MATCH (a:"+entity1+")-[r:"+rel+"]-(b:"+entity2+")  delete r"

    graph.run(cypher)

    response['msg'] = 'success'
    return JsonResponse(response)


# 修改关系
def relMod(request):
    entity1 = request.GET.get("entity1", '')
    entity2 = request.GET.get("entity2", '')
    entity2_new = request.GET.get('entity2_new','')
    rel = request.GET.get("rel", '')
    rel_new = request.GET.get("rel_new", '')

    response = {}

    cypher = "MATCH (a)-[r]-(b) WHERE a.name = '" + entity1 + "' AND b.name = '" + entity2_new + "' AND type(r) = '" + rel_new + "' return r"
    graph.run(cypher)
    if (len(graph.run(cypher).data()) != 0):
        print("已存在！" + cypher)
        response['msg'] = 'exist'
    else:
        # cypher = "MATCH (a)-[r]-(b) WHERE a.name = '" + entity1 + "' AND b.name = '" + entity2 + "' AND type(r) = '" + rel + "' delete r"
        cypher = "MATCH (a{name:'"+ entity1+"'}) - [r:"+ rel +"] -> (b{name:'"+entity2+"'}) delete r"
        graph.run(cypher)
        print("先删除原rel:" + cypher)
        # cypher = "MATCH (a),(b) WHERE a.name = '" + entity1 + "' AND b.name = '" + entity2_new + "' CREATE (a)-[ r:"+rel_new+" ]->(b) RETURN a,b "
        cypher = "MATCH (a:"+entity1+") CREATE (a)-[ r:"+rel_new+ "]->(b:"+ entity2_new+"{name:'"+ entity2_new+"',label:'patent'}) RETURN a,b"
        graph.run(cypher)
        print("再创建new_rel:" + cypher)
        response['msg'] = 'success'

    return JsonResponse(response)


# 展示知识图谱
def showKG(request):
    example = ExampleShow()

    entity_list = []
    relation_list = []
    name = []

    for i in example:
        n11 = i['n1']
        n22 = i['n2']
        n1 = i['n1.name']
        n1_id = i['id(n1)']
        n2_id = i['id(n2)']
        rel = i['type(rel)']
        n2 = i['n2.name']

        kg = {'用药':1,'功能':2,'主治':3,'性味':4,'物种':5,'化学成分':6,'拼音':7,'英文':7
              ,'类别':8,'其他':9}
        i = 0
        n1_type = 0
        n2_type = 0
        if rel in kg.keys():
            n2_type = kg[rel]
        else:
            n2_type = 9
        if 'category' in n11.keys():
            n1_type = kg[n11['category']]
        if 'category' in n22.keys():
            n2_type = kg[n22['category']]
        # for tmp in list:
        #     if (tmp in n1_id):
        #         n1_type = i
        #     if (tmp in n2_id):
        #         n2_type = i
        #     i = i + 1

        # entity1 = {
        #     'id': str(n1_id),
        #     'name': n1,
        #     'category': n1_type,
        # }
        entity1 = {
            'id': str(n1_id),
            'name': n1,
            'category': n1_type,
        }
        entity2 = {
            'id': str(n2_id),
            'name': n2,
            'category': n2_type,
        }

        if entity1 not in entity_list:
            entity_list.append(entity1)
        if entity2 not in entity_list:
            entity_list.append(entity2)
        relation = {
            'source': str(n1_id),
            'target': str(n2_id),
            'value': rel,
        }
        relation_list.append(relation)

    result = {
        'entity': entity_list,
        'relation': relation_list,
    }
    result = json.dumps(result, ensure_ascii=False)
    return HttpResponse(result)


# Cypher查询
def test(request):

    cypher = request.GET.get("text", '')

    try:
        example = graph.run(cypher).data()


        entity_list = []
        relation_list = []
        name = []

        for i in example:
            n1 = i['n1.name']
            n1_id = i['id(n1)']
            n2_id = i['id(n2)']
            rel = i['type(rel)']
            n2 = i['n2.name']

            entity1 = {
                'id': str(n1_id),
                'name': n1,
            }
            entity2 = {
                'id': str(n2_id),
                'name': n2,
            }

            if entity1 not in entity_list:
                entity_list.append(entity1)
            if entity2 not in entity_list:
                entity_list.append(entity2)
            relation = {
                'source': str(n1_id),
                'target': str(n2_id),
                'value': rel,
            }
            relation_list.append(relation)

        result = {
            'entity': entity_list,
            'relation': relation_list,
        }
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result)
    except Exception as e:
        entity_list = []
        relation_list = []
        print("暂不支持该类型Cypher语句！")
        result = {
            'entity': entity_list,
            'relation': relation_list,
        }
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result)


# 实体查询
def entitySearch(request):

    entity_name = request.GET.get("entity_name", '')
    # cypher = "match(n1:"+ entity_name +")-[rel]->(n2)  return id(n1),id(n2),n1.name,type(rel),n2.name,n1,n2 LIMIT 30"
    cypher = "MATCH (n1)-[rel]->(n2) WHERE (n1.name = '" + entity_name + "' OR n2.name = '" + entity_name + "') RETURN id(n1), id(n2), n1.name, type(rel), n2.name, n1, n2 LIMIT 30"

    cypher2 = "match(n1:"+ entity_name +")  return id(n1),n1.name,n1 LIMIT 30"

    example = graph.run(cypher).data()

    if (len(example) != 0):
        entity_list = []
        relation_list = []
        name = []
        for i in example:
            n11 = i['n1']
            n22 = i['n2']
            n1 = i['n1.name']
            n1_id = i['id(n1)']
            n2_id = i['id(n2)']
            rel = i['type(rel)']
            n2 = i['n2.name']

            kg = {'疾病': 0,'用药': 1, '功能': 2, '主治': 3, '性味': 4, '物种': 5, '化学成分': 6, '拼音': 7, '英文': 7
                , '类别': 8, '其他': 9}
            i = 0
            n1_type = 0
            n2_type = 0
            if rel in kg.keys():
                n2_type = kg[rel]
            else:
                n2_type = 9

            if 'category' in n11.keys():
                n1_type = kg[n11['category']]
            if 'category' in n22.keys():
                n2_type = kg[n22['category']]

            entity1 = {
                'id': str(n1_id),
                'name': n1,
                'category': n1_type,
            }
            entity2 = {
                'id': str(n2_id),
                'name': n2,
                'category': n2_type,
            }

            if entity1 not in entity_list:
                entity_list.append(entity1)
            if entity2 not in entity_list:
                entity_list.append(entity2)
            relation = {
                'source': str(n1_id),
                'target': str(n2_id),
                'value': rel,
            }
            relation_list.append(relation)

        result = {
            'entity': entity_list,
            'relation': relation_list,
        }
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result)

    if (len(example) == 0):
        example = graph.run(cypher2).data()
        entity_list = []
        for i in example:
            n11 = i['n1']
            n1_id = i['id(n1)']
            n1_type = 0
            n1 = i['n1.name']
            kg = {'疾病':0,'用药': 1, '功能': 2, '主治': 3, '性味': 4, '物种': 5, '化学成分': 6, '拼音': 7, '英文': 7
                , '类别': 8, '其他': 9}
            i = 0
            if 'category' in n11.keys():
                n1_type = kg[n11['category']]
            entity1 = {
                'id': str(n1_id),
                'name': n1,
                'category': n1_type,
            }

            if entity1 not in entity_list:
                entity_list.append(entity1)

        result = {
            'entity': entity_list,
        }
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result)


# 关系查询
def relSearch(request):

    entity1_name = request.GET.get("entity1_name", '')
    entity2_name = request.GET.get("entity2_name", '')
    rel = request.GET.get("rel", '')
    if (entity1_name == "" and entity2_name == "" and rel == ""):  # 三个未知
        cypher = "match (n1)-[rel]->(n2) return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name != "" and entity2_name == "" and rel == ""):  # 已知实体1
        cypher = "match(n1)-[rel]->(n2) where n1.name='" + entity1_name + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name == "" and entity2_name != "" and rel == ""):  # 已知实体2
        cypher = "match(n2)<-[rel]-(n1) where n2.name='" + entity2_name + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name == "" and entity2_name == "" and rel != ""):  # 已知关系
        cypher = "match(n1)-[rel]->(n2) where type(rel)='" + rel + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name != "" and entity2_name != "" and rel == ""):  # 已知实体1和实体2
        cypher = "match(n1)-[rel]->(n2) where n1.name='" + entity1_name + "' and n2.name='" + entity2_name + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name != "" and entity2_name == "" and rel != ""):  # 已知实体1和关系
        cypher = "match(n1)-[rel]->(n2) where type(rel)='" + rel + "' and n1.name='" + entity1_name + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name == "" and entity2_name != "" and rel != ""):  # 已知实体2和关系
        cypher = "match(n1)-[rel]->(n2) where type(rel)='" + rel + "' and n2.name='" + entity2_name + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"
    if (entity1_name != "" and entity2_name != "" and rel != ""):  # 已知实体1和实体2和关系
        cypher = "match(n1)-[rel]->(n2) where type(rel)='" + rel + "' and n1.name='" + entity1_name + "' and n2.name='" + entity2_name + "' return id(n1),id(n2),n1.name,type(rel),n2.name,LABELS(n1),LABELS(n2),n1,n2  LIMIT 30"


    try:
        example = graph.run(cypher).data()


        entity_list = []
        relation_list = []
        name = []

        for i in example:

            n11 = i['n1']
            n22 = i['n2']
            n1 = i['n1.name']
            n1_id = i['id(n1)']
            n2_id = i['id(n2)']
            rel = i['type(rel)']
            n2 = i['n2.name']

            kg = {'疾病':0,'用药': 1, '功能': 2, '主治': 3, '性味': 4, '物种': 5, '化学成分': 6, '拼音': 7, '英文': 7
                , '类别': 8, '其他': 9}
            i = 0
            n1_type = 0
            n2_type = 0
            if rel in kg.keys():
                n2_type = kg[rel]
            else:
                n2_type = 9
            if 'category' in n11.keys():
                n1_type = kg[n11['category']]
            if 'category' in n22.keys():
                n2_type = kg[n22['category']]
            # for tmp in list:
            #     if (tmp in n1_id):
            #         n1_type = i
            #     if (tmp in n2_id):
            #         n2_type = i
            #     i = i + 1

            # entity1 = {
            #     'id': str(n1_id),
            #     'name': n1,
            #     'category': n1_type,
            # }
            entity1 = {
                'id': str(n1_id),
                'name': n1,
                'category': n1_type,
            }
            entity2 = {
                'id': str(n2_id),
                'name': n2,
                'category': n2_type,
            }

            if entity1 not in entity_list:
                entity_list.append(entity1)
            if entity2 not in entity_list:
                entity_list.append(entity2)
            relation = {
                'source': str(n1_id),
                'target': str(n2_id),
                'value': rel,
            }
            relation_list.append(relation)

        result = {
            'entity': entity_list,
            'relation': relation_list,
        }
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result)
    except Exception as e:
        entity_list = []
        relation_list = []
        print("暂不支持该类型Cypher语句!")
        result = {
            'entity': entity_list,
            'relation': relation_list,
        }
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result)


# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from django.views.decorators.csrf import csrf_exempt
# from langchain_openai import ChatOpenAI
# from langchain.agents import initialize_agent, load_tools, AgentType
# import os
# import json
#
# # Set environment variables for API keys
# os.environ["SERPAPI_API_KEY"] = '0fdf2243442ef59bb738c69fc6093c9901fdb3fb10b073653e254df558f9bc2a'
#
# # Initialize the ChatOpenAI model
# llm = ChatOpenAI(
#     api_key="sk-a9f778112e4c486e8acf2502c5280068",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     model="qwen2-1.5b-instruct"
# )
#
# # Load tools and initialize the agent
# tools = load_tools(["serpapi"])
# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
#
#
# def handle_chat_request(user_input, is_first_interaction=True):
#     if is_first_interaction:
#         intro = "你好！我是医疗助手AI，我在这里帮助你解答健康和医疗相关的问题。请随时向我提问。"
#         return {'response': intro}, 200
#
#     if not user_input:
#         return {'error': 'No message provided'}, 400
#
#     # 构建prompt，只回答医疗相关的问题
#     prompt = f"I am a medical assistant designed to answer questions related to health and medicine. Please only ask me questions related to these topics. Your question: {user_input}"
#
#     try:
#         # Try invoking the agent with the handle_parsing_errors parameter set to True
#         response = agent.invoke(prompt, handle_parsing_errors=True)
#
#         # Check if the response is in the expected format
#         if isinstance(response, dict) and 'output' in response:
#             response_text = response.get('output', 'No response text')
#         else:
#             response_text = str(response)  # In case response is just a string or unexpected format
#
#         return {'response': response_text}, 200
#     except Exception as e:
#         print("Error in handle_chat_request:", str(e))
#         return {'error': str(e)}, 500
#
#
# from django.contrib.sessions.models import Session
#
#
# @require_http_methods(["POST"])
# @csrf_exempt
# def chat(request):
#     try:
#         data = json.loads(request.body)
#         user_input = data.get('message')
#
#         # 检查是否是第一次交流
#         is_first_interaction = False
#         session_key = request.session.session_key
#         if session_key:
#             session = Session.objects.get(session_key=session_key)
#             if 'is_first_interaction' not in session.get_decoded():
#                 is_first_interaction = True
#                 session['is_first_interaction'] = False
#                 session.save()
#
#         response_data, status_code = handle_chat_request(user_input, is_first_interaction)
#         return JsonResponse(response_data, status=status_code)
#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, load_tools, AgentType
from django.contrib.sessions.models import Session
import os
import json
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.embeddings import DashScopeEmbeddings

# 设置环境变量
os.environ["DASHSCOPE_API_KEY"] = "sk-45419d65418944dc88190bf13f19fb96"
os.environ["SERPAPI_API_KEY"] = "0fdf2243442ef59bb738c69fc6093c9901fdb3fb10b073653e254df558f9bc2a"

# 初始化 OpenAI 和工具
llm = ChatOpenAI(api_key="sk-45419d65418944dc88190bf13f19fb96", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", model="qwen2-math-72b-instruct")
# llm = ChatOpenAI(
#         api_key="08c1756702a6cc0e506dd38bde781c7b:NGYwZTI5ZDhjNjQ1YmE1ZjhiNDZiZjc1",
#         base_url="https://spark-api-open.xf-yun.com/v1",
#         model="general"
#     )
tools = load_tools(["serpapi"])
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 初始化嵌入模型
embedding = DashScopeEmbeddings(dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"), model="text-embedding-v2")

def load_excel(file_path):
    df = pd.read_excel(file_path)
    data = []
    print("Excel File Content:")  # Debugging line
    for index, row in df.iterrows():
        disease = row.iloc[0]  # 第一列为病症
        medication = row.iloc[2]  # 第三列为用药
        data.append(f"病症：{disease}，用药：{medication}")
        # print(f"病症：{disease}，用药：{medication}")  # Debugging line
    return data

from langchain.vectorstores import Chroma

from langchain.schema import Document


def process_xlsx(file_path, db_path):
    data = load_excel(file_path)
    # print("Loaded Excel data:", data)  # Debugging line

    # 将每个字符串数据包装成 Document 对象
    documents = [Document(page_content=doc) for doc in data]

    # print("Documents wrapped:", documents)  # Debugging line

    # 使用 RecursiveCharacterTextSplitter 分割文本
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    # print("Text splitter initialized.")  # Debugging line
    splits = text_splitter.split_documents(documents)
    # print("Text split into chunks:", splits)  # Debugging line

    # 创建 Chroma 向量数据库并指定持久化目录
    vectordb = Chroma.from_documents(documents=splits, embedding=embedding, persist_directory=db_path)
    print("Chroma vector store created and data persisted.")  # Debugging line

    # Debugging: Print out the content of the saved vector database
    print("Database Saved: ", vectordb)  # Debugging line
    print("Number of Documents in DB: ", len(vectordb))  # Debugging line

    return vectordb


def query_medication(disease_name, vectordb):
    print(f"Loaded vector database from D:/vector_databases/all_vectordb")  # Debugging line
    print(f"Querying vector database with: 病症：{disease_name}")  # Debugging line

    query = f"病症：{disease_name}"
    docs = vectordb.similarity_search(query, k=7)  # 获取最相关的前 5 个块
    print(docs)

    if docs:
        # 如果 docs 是字符串类型
        if isinstance(docs[0], str):  # 如果 docs 是字符串（而非 Document 对象）
            context = "\n".join(docs)  # 直接将字符串连接起来
        else:
            context = "\n".join([doc.page_content for doc in docs])  # 如果是 Document 对象，使用 page_content

        print("Found Documents: ", context)  # Debugging line
        prompt = f"以下是与病症相关的内容：\n{context}\n\n病症：{disease_name}\n请你根据文档内容回答病症的用药信息，注意要有病症以及治疗病症的药品，并且对该药品进行阐述，如果还有别的问题，请你也继续回答："
        response = llm.invoke(prompt)
        # 调试：打印返回的 response
        print(f"Response from llm.invoke(): {response.content}")
        print(f"Type of response: {type(response)}")
        return response.content

    return "未能在数据库中找到相关信息"


def external_search(query):
    try:
        # 使用外部搜索工具
        print(f"Running external search with query: {query}")  # Debug: Log the search query
        prompt = f"我是一个设计用来回答有关健康和医学问题的医疗助手。请只向我询问与这些主题相关的问题。您的问题：{query}"

        # Try invoking the agent with the handle_parsing_errors parameter set to True
        response = agent.invoke(prompt, handle_parsing_errors=True)

        # Check if the response is in the expected format
        if isinstance(response, dict) and 'output' in response:
            response_text = response.get('output', 'No response text')
            print(111)
        else:
            response_text = str(response)  # In case response is just a string or unexpected format
            print(222)

        return response_text
    except Exception as e:
        print("Error in handle_chat_request:", str(e))
        return {'error': str(e)}, 500
    #     # 执行 SERPAPI 查询
    #     search_results = tools[0].run(query)
    #     print(f"Search Results: {search_results}")  # Debug: Log the full search results
    #
    #     # 如果 search_results 直接是字符串列表，直接返回第一个结果
    #     if search_results:
    #         return f"{search_results}"
    #
    #     # 如果没有找到有效的结果，返回默认提示
    #     return "未能找到相关的外部搜索结果。"
    #
    # except KeyError as e:
    #     print(f"KeyError in external_search: {str(e)}")  # 捕获 KeyError 错误
    #     return "外部搜索结果格式错误。"
    #
    # except Exception as e:
    #     print(f"Error in external_search: {str(e)}")  # 捕获其他异常
    #     return f"执行外部搜索时出错: {str(e)}"

import re

def is_valid_query(user_input):
    # 使用正则表达式检查用户输入中是否包含“病症”和“用药”相关信息
    # 比如：检查是否包含“病症”相关的词和“用药”
    disease_keywords = r'病症|胃炎|萎缩性胃炎|慢性胃炎|慢性浅表性胃炎|慢性萎缩性胃炎|浅表性胃炎|糜烂性胃炎|高血压病慢性胃炎心律失常|慢性萎缩性胃炎肠上皮化生'  # 病症相关关键词，根据需要扩展
    medication_keywords = r'用药|治疗|药物|药品|用什么药'  # 用药相关关键词，根据需要扩展

    # 判断是否同时包含病症和用药
    if re.search(disease_keywords, user_input) and re.search(medication_keywords, user_input):
        return True
    return False

def handle_chat_request(user_input, is_first_interaction=True):
    try:
        # 第一次交互，返回欢迎信息
        if is_first_interaction:
            intro = "你好！我是医疗助手AI，我在这里帮助你解答健康和医疗相关的问题。请随时向我提问。"
            return {'response': intro}, 200

        # 如果没有用户输入，返回错误
        if not user_input:
            return {'error': 'No message provided'}, 400

        # 假设用户输入是病症名称，构造查询
        disease_name = user_input.strip()
        print(f"Querying for disease: {disease_name}")  # Debug: Log the disease name

        # 检查输入是否包含病症和用药信息
        if is_valid_query(user_input):
            # 1. 查询数据库（Chroma 向量数据库）来获取病症的用药信息
            db_path = "vector_databases/all_vectordb"  # 加载向量数据库

            # 使用 Chroma 加载向量数据库
            vectordb = Chroma(persist_directory=db_path, embedding_function=embedding)

            # Debug: Log the loading of vectordb
            print(f"Loaded vector database from {db_path}")

            response_text = query_medication(disease_name, vectordb)

            print(f"Response from query_medication: {response_text}")  # Debug: Log the response from database query

            # 如果没有找到相关信息，进行外部搜索
            if "未能生成答案" in response_text or "未能在数据库中找到相关信息" in response_text:
                response_text = external_search(disease_name)
                print(f"Response from external search: {response_text}")  # Debug: Log the response from external search

        else:
            # 如果没有包含“病症”和“用药”字眼，进行外部搜索
            response_text = external_search(disease_name)
            print(f"Response from external search: {response_text}")  # Debug: Log the response from external search

        # 返回最终的回答
        return {'response': response_text}, 200

    except Exception as e:
        print(f"Error in handle_chat_request: {str(e)}")  # Debug: Log any exceptions
        return {'error': str(e)}, 500


@require_http_methods(["POST"])
@csrf_exempt
def chat(request):
    try:
        # 获取用户输入的消息
        data = json.loads(request.body)
        user_input = data.get('message')

        if not user_input:
            return JsonResponse({'error': 'No message provided'}, status=400)

        # 检查是否是第一次交流
        is_first_interaction = False
        session_key = request.session.session_key
        if session_key:
            session = Session.objects.get(session_key=session_key)
            if 'is_first_interaction' not in session.get_decoded():
                is_first_interaction = True
                session['is_first_interaction'] = False
                session.save()

        print(f"User input: {user_input}, is_first_interaction: {is_first_interaction}")  # Debug: Log user input

        # 调用 handle_chat_request 来处理用户请求
        response_data, status_code = handle_chat_request(user_input, is_first_interaction)

        print(f"Response Data: {response_data}, Status Code: {status_code}")  # Debug: Log response data

        return JsonResponse(response_data, status=status_code)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        print(f"Error in chat view: {str(e)}")  # Debug: Log the exception
        return JsonResponse({'error': str(e)}, status=500)


