import os


class ConfigurationManager(object):


    def get_redis_configuration(self):
        config_dic = {}
        config_dic["redis-host"] = os.environ["REDIS_HOST"]
        config_dic["redis-port"] = int(os.environ["REDIS_PORT"])
        config_dic["redis-password"] = os.environ["REDIS_PASSWORD"]
        return config_dic
