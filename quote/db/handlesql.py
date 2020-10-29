import pymysql


class Handlesql:
    def __init__(self,host,user,password,database,port,charset):
        # 创建连接
        self.conn = pymysql.Connection(host=host, user=user, password=password,
                                  database=database, port=port, charset=charset)
        # 创建游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    #查询数据
    def db_search(self,sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            res = self.cur.fetchall()
            print(res)
        except Exception as e:
            print(e,'search error')
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()

            # 关闭连接
            self.conn.close()
        return res
    #更新数据
    def db_update(self,sql):
        try:
            # 执行sql
            conut=self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e,'update error')
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()

            # 关闭连接
            self.conn.close()
        return conut
    #删除数据
    def db_delete(self,sql):
        try:
            # 执行sql
            count=self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e,'delete error')
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()

            # 关闭连接
            self.conn.close()
        return count
    #插入数据
    def db_insert(self,sql):
        try:
            # 执行sql
            count=self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e,'insert error')
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()

            # 关闭连接
            self.conn.close()
        return count
# if __name__ == '__main__':
#     db=Handlesql('172.17.4.216','root','123456','quote',3306,'utf8')
#     db.db_search('select * from tb_user')
#     # db.db_delete()
#     # db.db_insert()
#     # db.db_delete()