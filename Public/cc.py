#coding: utf-8
import configparser

def readConfig(sections,option):
    try:
        config=configparser.ConfigParser()
        config.read("config.ini",encoding='UTF-8')
        return config.get(sections,option)
    except Exception as e:
        print(e)

if __name__ =="__main__":
    IP = readConfig("DEVICES","method")