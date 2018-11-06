import pymysql
db=pymysql.connect('localhost','root','123456','ljdjango72') #改自己的主机名，用户名，密码，数据库名
cursor=db.cursor()
import json
for i in range(1):
    i+=1
    if i == 1:
        i=''

    # path='untitled/static/json/floor'+str(i)+'-lunbo.json'
    # path='untitled/static/json/index-lunbo1.json'
    path='../static/json/detail.json'
    # path='untitled/static/json/list-detail.json'
    a=open(path,'r',encoding='utf8')
    b=a.read()
    b=json.loads(b)
    a=0
    for j in b:

        a += 1
        cursor.execute('insert into App_goods values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,s%,s%,s%,s%,s%,s%)',[a,j['id'],j['name'],j['price'],j['detail'],j['unit'],'/static'+j['headImg'][2:],'/static'+j['img1'][2:],'/static'+j['img2'][2:],'/static'+j['img3'][2:],'/static'+j['img4'][2:],'/static'+j['img5'][2:],'/static'+j['img6'][2:],'/static'+j['img7'][2:],'/static'+j['img13'][2:],'/static'+j['img19'][2:],'/static'+j['img20'][2:],j['total'],j['potol'],])

    # for j in b:
    #
    #     a+=1
    #
    #     cursor.execute('insert into mbbapp_goods values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    #                    [a, j['id'], j['name'], j['price'], j['mbbPrice'], j['unit'], j['headImg'],
    #                     j['pic1'], j['pic2'], j['pic3']])
    #

    #
    # for j in b:
    #     try:
    #         cursor.execute('insert into mbbapp_img (num,img,name) values (%s,%s,%s)',[j['id'],j['img'],j['name']])
    #     except:
    #         j['name']='0'
    #         cursor.execute('insert into mbbapp_img (num,img,name) values (%s,%s,%s)', [j['id'], j['img'],j['name']])
    db.commit()
cursor.close()
db.close()