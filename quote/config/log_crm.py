import logging
import time


class AutoLog:
    def __init__(self):
        self.logger=logging.getLogger('log')


    def set_mes(self,mess,level_p):
     try:
        # 时间
        now_data = time.strftime('%Y-%m-%d', time.localtime())
        # 创建文件handle
        fh = logging.FileHandler('../../log_info/auto_' + now_data + '.log')
        # 创建控制台handle
        ch = logging.StreamHandler()
        # 格式化
        fm = logging.Formatter('%(asctime)s %(message)s %(levelname)s')
        # 对文件格式
        fh.setFormatter(fm)
        # 对控制台格式
        ch.setFormatter(fm)
        # 文件句柄加入logger
        self.logger.addHandler(fh)
        # 控制台句柄加入logger
        self.logger.addHandler(ch)
        # 设置打印级别
        self.logger.setLevel(logging.DEBUG)
        # 输出info
        if level_p == 'debug':
            self.logger.debug(mess)
        elif level_p=='info':
            self.logger.info(mess)
        elif level_p == 'error':
            self.logger.error(mess)
        # 移除文件对象
        self.logger.removeHandler(fh)
        # 移除控制台对象
        self.logger.removeHandler(ch)
     except:
        print('file exception')
     finally:
        fh.close()
# if __name__=='__main__':
#     auto=AutoLog()
#     auto.set_mes('message','info')