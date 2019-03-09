import os
import configparser

proDir = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(configpath)
        print(proDir)
        print(configpath)

    def get_host(self,item):
        return self.config.get("host",item)



if __name__ == "__main__":
    readconfig = ReadConfig()
    print(readconfig.get_host("username"))