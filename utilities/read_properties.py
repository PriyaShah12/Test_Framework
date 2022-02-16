import configparser

config=configparser.RawConfigParser()
config.read(".//configFile//config.ini")

class configRead:
    @staticmethod
    def ReadUrl():
        url=config.get('common Info', 'base_url')
        return url