import time
from utils import Utils
from goods import Goods
from line_notify import Line

if __name__ == '__main__':
    utils = Utils()
    while True:
        try:
            utils.check_goods(Goods.NLpillow.url)
            print("Run finished")
            time.sleep(60*6)
        except Exception as e:
            print(f"Error occurred: {e}")
            raise e