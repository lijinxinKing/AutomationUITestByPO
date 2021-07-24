# 用来读取yaml数据

import yaml
#使用如下命令安装yaml
# pip install pyyaml
def loadyaml(fileName):
    file = open(fileName,'r',encoding='utf-8')
    # 读取Yaml 文件
    data = yaml.load(file,Loader=yaml.FullLoader)
    return data
