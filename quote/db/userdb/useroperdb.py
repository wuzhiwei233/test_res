from quote.db.handlesql import Handlesql


class userOperationDb:
    def __init__(self,host,user,password,database,port,charset):
        self.us=Handlesql(host,user,password,database,port,charset)
    #查询数据
    def user_search(self,sql):
        self.us.db_search(sql)
    #更新数据
    def user_update(self,sql):
        self.us.db_update(sql)
    #删除数据
    def user_delete(self,sql):
        self.us.db_delete(sql)
    #插入数据
    def user_insert(self,sql):
        self.us.db_insert(sql)