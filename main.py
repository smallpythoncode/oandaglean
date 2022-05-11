"""
# TODO
"""

from os.path import isfile
from configparser import ConfigParser


def retrieve_config():
    """

    :return:
    """
    file = "config/config.ini"
    if isfile("config/sp_config.ini"):
        file = "config/sp_config.ini"

    config = ConfigParser()
    config.read(file)
    account_id = config["oanda"]["account_id"]
    access_token = config["oanda"]["access_token"]
    configuration = {"account_id": account_id, "access_token": access_token}

    return configuration


# TODO
def initialize_config():
    pass


def main():
    config = retrieve_config()

    print("ID:", config["account_id"])
    print("Token:", config["access_token"])


if __name__ == "__main__":
    main()
