from project.parsers.querie_goods import get_product


if __name__ == "__main__":
    goods_list = get_product('Молодой вкусный картофель',10)
    for good in goods_list[0]:
        print(good)
    # print(goods_list)
