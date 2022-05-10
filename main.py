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

    return account_id, access_token




def main():
    account_id, access_token = retrieve_config()

    print("ID:", account_id)
    print("Token:", access_token)


if __name__ == "__main__":
    main()
