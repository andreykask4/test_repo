import os


def categ_to_num():
    """
    asdasdsa
    Args:
        q (int): колчиство q
    """
    pass


def window2():
    pass


def window3():
    pass


def window4():
    stages = ['train', 'test', 'val']
    for stage in stages: 
        creation_path = os.path.join('data', stage)
        print(creation_path)
        if not os.path.exists(creation_path):
            os.makedirs(creation_path)


def window5():
    pass


def EDA():
    categ_to_num()
    window2()
    window3()
    window4()
    window5()


if __name__ == "__main__":
    EDA()