# _*_ coding:utf-8 _*_
from pyzabbix import ZabbixAPI
import logging, logging.config, sys
from logging.handlers import TimedRotatingFileHandler
# zabbix debug
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)

log = logging.getLogger('pyzabbix')
log.addHandler(stream)

log.setLevel(logging.INFO)



class ZBXHelper:
    def __init__(self):
        self.zapi = ZabbixAPI("http://10.31.23.147/zabbix/")
        try:
            self.zapi.login("lihuiyao", "12345678")
        except Exception as e:
            log.error("用户密码错误")
            exit(1)

    def findHost(self, hostname):
        """
        返回 host id,如没有返回None
        :param hostname:
        :return:
        """
        filter = {"host": [hostname]}
        host = self.zapi.host.get(filter=filter)
        if (len(host) == 1):
            return (host[0]["hostid"])
        else:
            return None

    def getAllHosts(self):
        """
        返回所有主机,排除模板
        :return:
        """
        # filter={"host":[host]}
        hosts = self.zapi.host.get(output="extend")
        return hosts

    def getItemsByHost(self,host):
        filter = {"host":host }
        items = self.zapi.item.get(filter=filter)
        return(items)

if __name__=="__main__":
    zbx = ZBXHelper()
    # zbx.addGROUP("asdf")
    items=zbx.getItemsByHost("10.31.23.147")
    for item in items:
        # log.info(item)
        log.info("key:%s-----value:%s-------timestamp:%s"%(item["key_"],item["lastvalue"],item["lastclock"]))
