import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get("common info", "url")
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def get_mail():
        mail = config.get("common info", "mail")
        return mail
