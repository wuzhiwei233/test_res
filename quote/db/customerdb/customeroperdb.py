from quote.db.handlesql import Handlesql


class CustomerOperationDb:
    def __init__(self,host,user,password,database,port,charset):
        self.cus=Handlesql(host,user,password,database,port,charset)
    #查询数据
    def cus_search(self,sql):
        self.cus.db_search(sql)
    #更新数据
    def cus_update(self,sql):
        self.cus.db_update(sql)
    #删除数据
    def cus_delete(self,sql):
        self.cus.db_delete(sql)
    #插入数据
    def cus_insert(self,sql):
        self.cus.db_insert(sql)