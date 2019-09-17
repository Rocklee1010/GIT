import pymysql
import tkinter

class User:
    def __init__(self, database):
        self.db = pymysql.connect(user='root', passwd='123456', database=database, charset='utf8')
        self.cur = self.db.cursor()

    def regist(self,name, pwd):
        sql = "select name from users where name = %s"
        self.cur.execute(sql, [name])
        if self.cur.fetchone():
            print("用户名已存在")
            return False
        else:
            try:
                sql = "insert into users (name, pwd) values (%s, %s)"
                self.cur.execute(sql, [name, pwd])
                self.db.commit()
                return True
            except:
                self.db.rollback()

    def login(self, name, pwd):
        sql = "select * from users where name = %s and pwd = %s"
        self.cur.execute(sql, [name, pwd])
        if self.cur.fetchone():
            return True

if __name__ == '__main__':



    print("请注册")
    user1 = User('user')
    while True:
        name = input("请输入姓名:")
        if not name:
            break
        pwd = input("请输入密码:")

        if user1.regist(name, pwd):
            print("注册成功")
            break

    print("请登录")
    while True:
        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        if user1.login(name, pwd):
            print("登录成功")
            break
        else:
            print("用户名或密码错误")








