import mysql.connector
import datetime
import traceback
host='localhost'
user='root'
passwd='root'
database='VIATICOME'
auth_plugin=None
#自定义myexecute    
def myexecute(sql,val):
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database,auth_plugin=auth_plugin)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        cur.execute(sql,val)
        mydb.commit()
        return 'ok'
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + "; val: " ,val);
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
        return []
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#自定义myselect
def myselect(sql,val):
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        cur.execute(sql,val)
        res=cur.fetchall()
        if res:
            return res
        else:
            return []
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";");
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
        return []
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#登录
def login(username,passwordin):
    sql="select * from user where email=(%s) and password=(%s)"
    val=(username,passwordin)
    user_info={}
    for x in myselect(sql,val):
        user_info['user_id'],user_info['email'],user_info['phone'],user_info['name'],user_info['password'],user_info['gender'],user_info['user_type']=x
    return user_info

#注册
def sign(email,phone,name,passwordin,gender,user_type):
    sql="insert into user (email,phone,name,password,gender,user_type) values (%s,%s,%s,%s,%s,%s)"
    val=(email,phone,name,passwordin,gender,user_type)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#简易版注册
def easy_sign(email,passwordin):
    user_type=0
    sql="insert into user (email,password,user_type) values (%s,%s,%s)"
    val=(email,passwordin,user_type)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服或租客修改email（修改user表）
def modify_email(email,user_id):
    sql="update user set email=(%s) where user_id=(%s)"
    val=(email,str(user_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服或租客修改phone
def modify_phone(phone,user_id):
    sql="update user set phone=(%s) where user_id=(%s)"
    val=(phone,str(user_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服或租客修改name
def modify_name(name,user_id):
    sql="update user set name=(%s) where user_id=(%s)"
    val=(name,str(user_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服或租客修改password
def modify_password(password,user_id):
    sql="update user set password=(%s) where user_id=(%s)"
    val=(password,str(user_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服或租客修改gender
def modify_gender(gender,user_id):
    sql="update user set gender=(%s) where user_id=(%s)"
    val=(str(gender),str(user_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改用户全部资料
def modify_info(email,phone,name,passwd,gender,user_id):
    sql="update user set email=(%s),phone=(%s),name=(%s),password=(%s),gender=(%s) where user_id=(%s)"
    val=(str(email),str(phone),str(name),str(passwd),str(gender),str(user_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服或租客查询租客资料（查询user表）
def view_info(email):
    sql="select * from user where email=(%s)"
    val=(str(email),)
    user_info={}
    for x in myselect(sql,val):
        user_info['user_id'],user_info['email'],user_info['phone'],user_info['name'],user_info['password'],user_info['gender'],user_info['user_type']=x
    return user_info

#删除指定用户
def delete_user(email):
    sql="delete from user where email=(%s)"
    val=(str(email),)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#查询所有用户
def view_all_user():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from user"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['user_id'],info['email'],info['phone'],info['name'],info['password'],info['gender'],info['user_type']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#客服添置新房源（修改house表）
def add_house(size,house_type,bed_num,price,if_rented,intro,address):
    sql="insert into house (size,house_type,bed_num,price,if_rented,intro,address) values (%s,%s,%s,%s,%s,%s,%s)"
    val=(str(size),str(house_type),str(bed_num),str(price),str(if_rented),intro,address)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服删除房源（修改house表）
def delete_house(house_id):
    sql="delete from house where house_id=(%s)"
    val=(str(house_id),)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#获取单个房子信息（house表）
def view_one_house(house_id):
    sql="select * from house where house_id=(%s)"
    val=(str(house_id),)
    house_info={}
    for x in myselect(sql,val):
        house_info['house_id'],house_info['size'],house_info['house_type'],house_info['bed_num'],house_info['price'],house_info['if_rented'],house_info['intro'],house_info['address']=x
    return house_info

#获取所有房子信息
def view_all_house():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from house"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['house_id'],info['size'],info['house_type'],info['bed_num'],info['price'],info['if_rented'],info['intro'],info['address']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#获取未出租的房子信息（house表）
def view_available_house():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from house where if_rented=0"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['house_id'],info['size'],info['house_type'],info['bed_num'],info['price'],info['if_rented'],info['intro'],info['address']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#修改房子size（house表）
def modify_size(size,house_id):
    sql="update house set size=(%s) where house_id=(%s)"
    val=(str(size),str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改房子type（house表）
def modify_type(house_type,house_id):
    sql="update house set house_type=(%s) where house_id=(%s)"
    val=(str(house_type),str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改房子bed_num（house表）
def modify_bed(bed_num,house_id):
    sql="update house set bed_num=(%s) where house_id=(%s)"
    val=(str(bed_num),str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改房子price（house表）
def modify_bed(price,house_id):
    sql="update house set price=(%s) where house_id=(%s)"
    val=(str(price),str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改房子if_rented（house表）
def modify_if_rented(if_rented,house_id):
    sql="update house set if_rented=(%s) where house_id=(%s)"
    val=(str(if_rented),str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改房子intro（house表）
def modify_bed(intro,house_id):
    sql="update house set intro=(%s) where house_id=(%s)"
    val=(intro,str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改房子address（house表）
def modify_bed(address,house_id):
    sql="update house set address=(%s) where house_id=(%s)"
    val=(address,str(house_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#建立新的投诉或保修（修改feedback表）
def add_feedback(user_id,house_id,feedback_type,pic,comment):
    sql="insert into feedback (user_id,house_id,feedback_type,pic,comment,state) values (%s,%s,%s,%s,%s,%s)"
    val=(str(user_id),str(house_id),str(feedback_type),pic,comment,str(0))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#顾客或客服查看具体某一条投诉（查看feedback表）
def view_one_feedback(feedback_id):
    sql="select * from feedback where feedback_id=(%s)"
    val=(str(feedback_id),)
    feedback_info={}
    for x in myselect(sql,val):
        feedback_info['feedback_id'],feedback_info['user_id'],feedback_info['house_id'],feedback_info['feedback_type'],feedback_info['pic'],feedback_info['comment'],feedback_info['reply'],feedback_info['state']=x
    return feedback_info

#顾客总览所有自己发出的投诉（feedback表）
def view_customer_feedback(user_id):
    sql="select * from feedback where user_id=(%s)"
    val=(str(user_id),)
    infos=[]
    for x in myselect(sql,val):
        info={}
        info['feedback_id'],info['user_id'],info['house_id'],info['feedback_type'],info['pic'],info['comment'],info['reply'],feedback_info['state']=x
        infos.append(info)
    return infos

#客服总览所有所有的投诉（feedback表）
def view_all_feedback():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from feedback"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['feedback_id'],info['user_id'],info['house_id'],info['feedback_type'],info['pic'],info['comment'],info['reply'],feedback_info['state']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#客服回复投诉（修改feedback表）
def reply_feedback(reply,feedback_id):
    sql="update feedback set reply=(%s) where feedback_id=(%s)"
    val=(reply,str(feedback_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#筛选未完成投诉/报修
def find_unfinish_feedback():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from feedback where state=0"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['feedback_id'],info['user_id'],info['house_id'],info['feedback_type'],info['pic'],info['comment'],info['reply'],feedback_info['state']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#确定投诉/报修已完成
def confirm_feedback(feedback_id):
    sql="update feedback set state=1 where feedback_id=(%s)"
    val=(str(feedback_id),)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False


#客服查看所有工单（查看repair表）
def view_all_repair():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from repair"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['repair_id'],info['feedback_id'],info['user_id'],info['staff_id'],info['reply'],info['house_id']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#客服查看某一个师傅所有的工单（repair表）
def view_staff_repair(staff_id):
    sql="select * from repair where staff_id=(%s)"
    val=(str(staff_id),)
    infos=[]
    for x in myselect(sql,val):
        info={}
        info['repair_id'],info['feedback_id'],info['user_id'],info['staff_id'],info['reply'],info['house_id']=x
        infos.append(info)
    return infos

#客服或顾客查看某一个工单（repair表）
def view_one_repair(repair_id):
    sql="select * from repair where repair_id=(%s)"
    val=(str(repair_id),)   
    repair_info={}
    for x in myselect(sql,val):
        repair_info['repair_id'],repair_info['feedback_id'],repair_info['user_id'],repair_info['staff_id'],repair_info['reply'],repair_info['house_id']=x
    return repair_info

#顾客查看自己所有的工单（repair表）
def view_customer_repair(user_id):
    sql="select * from repair where user_id=(%s)"
    val=(str(user_id),)
    infos=[]
    for x in myselect(sql,val):
        info={}
        info['repair_id'],info['feedback_id'],info['user_id'],info['staff_id'],info['reply'],info['house_id']=x
        infos.append(info)
    return infos

#师傅回复（修改repair表信息）
def staff_reply(reply,repair_id):
    sql="update repair set reply=(%s) where repair_id=(%s)"
    val=(reply,str(repair_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#顾客评价师傅（修改repair表信息）
def staff_comment(user_id,staff_id,comment):
    sql="insert into comment (user_id,staff_id,staff_comment) values (%s,%s,%s)"
    val=(str(user_id),str(staff_id),comment)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#查看某个师傅的所有评价(comment表)
def view_staff_comment(staff_id):
    sql="select user_id,staff_comment from comment where staff_id=(%s)"
    val=(str(staff_id),)
    comments=[]
    for x in myselect(sql,val):
        comm={}
        comm['user_id'],comm['staff_comment']=x
        comments.append(comm)
    return comments

#客服建立工单并指定师傅（修改repair表）
def choose_staff(feedback_id,staff_id):
    user_id=view_one_feedback(feedback_id)['user_id']
    house_id=view_one_feedback(feedback_id)['house_id']
    sql="insert into repair (feedback_id,user_id,staff_id,house_id) values (%s,%s,%s,%s)"
    val=(str(feedback_id),str(user_id),str(staff_id),str(house_id))
    myexecute(sql,val)

#客服或租客查询具体一个合同（查询rent表）
def view_contract(rent_id):
    sql="select * from rent where rent_id=(%s)"
    val=(str(rent_id),)
    contract_info={}
    for x in myselect(sql,val):
        contract_info['rent_id'],contract_info['user_id'],contract_info['house_id'],contract_info['rentdate'],contract_info['rent_type'],contract_info['verify_type'],contract_info['long_if_sign'],contract_info['keep'],contract_info['if_paid']=x
    return contract_info

#客服或租客查询某租客全部合同（查询rent表）
def view_user_all_contract(user_id):
    sql="select * from rent where user_id=(%s)"
    val=(str(user_id),)
    infos=[]
    for x in myselect(sql,val):
        info={}
        info['rent_id'],info['user_id'],info['house_id'],info['rentdate'],info['rent_type'],info['verify_type'],info['long_if_sign'],info['keep'],info['if_paid']=x
        infos.append(info)
    return infos

#查询所有未审核合同
def view_unverify(verify_type):
    sql="select * from rent where verify_type=(%s)"
    val=(str(verify_type),)
    infos=[]
    for x in myselect(sql,val):
        info={}
        info['rent_id'],info['user_id'],info['house_id'],info['rentdate'],info['rent_type'],info['verify_type'],info['long_if_sign'],info['keep'],info['if_paid']=x
        infos.append(info)
    return infos

#查询所有合同
def view_all_contract():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from rent"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['rent_id'],info['user_id'],info['house_id'],info['rentdate'],info['rent_type'],info['verify_type'],info['long_if_sign'],info['keep'],info['if_paid']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#通过user_id查询user_name
def find_username(user_id):
    sql="select name from user where user_id=(%s)"
    val=(str(user_id),)
    res={}
    for x in myselect(sql,val):
        res['name']=x
    return res

#建立新合同
def add_contract(user_id,house_id,rentdate,rent_type,verify_type,long_if_sign,keep,if_paid):
    sql="insert into rent (user_id,house_id,rentdate,rent_type,verify_type,long_if_sign,keep,if_paid) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(user_id),str(house_id),str(rentdate),str(rent_type),str(verify_type),str(long_if_sign),str(keep),str(if_paid))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服和租客删除合同订单（修改rent表）
def delete_contract(rent_id):
    sql="delete from rent where rent_id=(%s)"
    val=(str(rent_id),)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#线下是否签订长期合同（修改rent表的long_if_sign）
def offline_sign(long_if_sign,rent_id):
    sql="update rent set long_if_sign=(%s) where rent_id=(%s)"
    val=(str(long_if_sign),str(rent_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#修改支付状态（修改rent表的if_paid）
def pay(if_paid,rent_id):
    sql="update rent set if_paid=(%s) where rent_id=(%s)"
    val=(str(if_paid),str(rent_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服增加维修人员（修改staff表）
def add_staff(phone,name):
    sql="insert into staff (phone,name) values (%s,%s)"
    val=(phone,name)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#客服删除维修人员（修改staff表）
def delete_staff(staff_id):
    sql="delete from staff where staff_id=(%s)"
    val=(str(staff_id),)
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#查看所有的维修人员
def view_all_staff():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from staff"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['staff_id'],info['phone'],info['name']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#客服审核合同（修改verify_type）
def verify_contract(verify_type,rent_id):
    sql="update rent set verify_type=(%s) where rent_id=(%s)"
    val=(str(verify_type),str(rent_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#顾客续约（修改rent合同）
def renew(time,rent_id):
    sql="update rent set keep=(%s) where rent_id=(%s)"
    keep=view_contract(rent_id)['keep']
    val=(str(time+keep),str(rent_id))
    res=myexecute(sql,val)
    if res:
        return True
    else:
        return False

#推荐9个房源
def recommend():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from house where if_rented=0 limit 0,9"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['house_id'],info['size'],info['house_type'],info['bed_num'],info['price'],info['if_rented'],info['intro'],info['address']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#最贵的房子
def expesive():
    try:
        connFlag=False
        curFlag=False
        mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
        connFlag=True
        cur = mydb.cursor()
        curFlag=True
        sql="select * from house where price >= all (select price from house) limit 0,1"
        cur.execute(sql)
        res=cur.fetchall()
        infos=[]
        for x in res:
            info={}
            info['house_id'],info['size'],info['house_type'],info['bed_num'],info['price'],info['if_rented'],info['intro'],info['address']=x
            infos.append(info)
        return infos
    except:
        traceback.print_exc()
        print("["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+"Mysql connection error executing: " + sql + ";")
        if (connFlag==False):
            print("Fail to connect to database")
        if (curFlag==False):
            print("Fail to create a cursor")
    finally:
        if curFlag==True:
            cur.close()
        if connFlag==True:
            mydb.close()

#判断是否为历史订单
def if_history():
    #先把所有时间字符串取出来格式化成时间格式，然后用python加上keep天数，判断后取出符合要求的rent_id,再返回这些rent的所有信息
    infos_history=[]
    for x in view_all_contract():
        n=x['keep']
        rent_id=x['rent_id']
        last_day=x['rentdate']+datetime.timedelta(days=n)
        print (last_day)
        if last_day<datetime.datetime.now():
            infos_history.append(x)
    if infos_history:
        return infos_history
    else:
        return []

#条件搜索短租
def search_short(checkin_time,rent_days,house_type,lowest_price,highest_price):
    sql="select house_id from house where house_type=(%s) and price>=(%s) and price <=(%s)"
    val=(str(house_type),str(lowest_price),str(highest_price))
    res=[]
    for x in myselect(sql,val):
        res.append(x[0])
    h=0
    for x in res:
        for rent in view_all_contract():
            n=rent['keep']
            id=rent['house_id']
            a=datetime.datetime.strptime(checkin_time, "%Y-%m-%d")
            b=(a+datetime.timedelta(days=rent_days)).strftime("%Y-%m-%d")
            first_day=rent['rentdate']
            last_day=rent['rentdate']+datetime.timedelta(days=n)
            if (x==id and a>=first_day) or (x==id and a<last_day):
                del res[h]
                h=h-1
                break
            if (x==id and b>first_day) or (x==id and b<=last_day):
                del res[h]
                h=h-1
                break
        h=h+1
    ans=[]
    for x in res:
        sql="select * from house where house_id=(%s)"
        val=(str(x),)
        for x in myselect(sql,val):
            info={}
            info['house_id'],info['size'],info['house_type'],info['bed_num'],info['price'],info['if_rented'],info['intro'],info['address']=x
            ans.append(info)
    
    if datetime.datetime.strptime(checkin_time, "%Y-%m-%d")<datetime.datetime.now():
        empty=[]
        print(1)
        return empty
    else:
        return ans

#条件搜索长租
def search_long(checkin_time,rent_months,house_type,lowest_price,highest_price):
    sql="select house_id from house where house_type=(%s) and price>=(%s) and price <=(%s)"
    val=(str(house_type),str(lowest_price),str(highest_price))
    res=[]
    for x in myselect(sql,val):
        res.append(x[0])
    h=0
    for x in res:
        for rent in view_all_contract():
            n=rent['keep']
            id=rent['house_id']
            a=datetime.datetime.strptime(checkin_time, "%Y-%m-%d")
            b=(a+datetime.timedelta(months=rent_months)).strftime("%Y-%m-%d")
            first_day=rent['rentdate']
            last_day=rent['rentdate']+datetime.timedelta(days=n)
            if (x==id and a>=first_day) or (x==id and a<last_day):
                del res[h]
                h=h-1
                break
            if (x==id and b>first_day) or (x==id and b<=last_day):
                del res[h]
                h=h-1
                break
        h=h+1
    ans=[]
    for x in res:
        sql="select * from house where house_id=(%s)"
        val=(str(x),)
        for x in myselect(sql,val):
            info={}
            info['house_id'],info['size'],info['house_type'],info['bed_num'],info['price'],info['if_rented'],info['intro'],info['address']=x
            ans.append(info)
    
    if datetime.datetime.strptime(checkin_time, "%Y-%m-%d")<datetime.datetime.now():
        empty=[]
        print(1)
        return empty
    else:
        return ans

#判断房子所租的日期是否会和已有订单发生冲突
def judge_period(checkin_time,rent_days,house_id):
    sql="select * from rent where house_id=(%s)"
    val=(str(house_id),)
    flag=1
    for x in myselect(sql,val):
        n=x['keep']
        first_day=x['rentdate']
        last_day=x['rentdate']+datetime.timedelta(days=n)
        a=datetime.datetime.strptime(checkin_time, "%Y-%m-%d")
        b=(a+datetime.timedelta(days=rent_days)).strftime("%Y-%m-%d")
        if (a>=first_day) or (a<last_day):
            flag=0
        if (b>first_day) or (b<=last_day):
            flag=0
        if a<datetime.datetime.now():
            flag=0
    #如果不会发生冲突,返回1
    if flag==1:
        return 1
    #如果发生冲突，返回0
    else:
        return 0