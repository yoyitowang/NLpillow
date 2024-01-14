from utils import Utils
from goods import Goods
from line_notify import Line

if __name__ == '__main__':
    utils = Utils()
    utils.check_goods(Goods.NLpillow.url)
    print("Run finished")