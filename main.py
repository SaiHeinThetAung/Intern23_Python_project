import sec_tree
import own_db_tree
import third_tree

first_tree = own_db_tree.root
sec__tree = sec_tree.tree

third__tree = third_tree.tree
info = []


def connection_test(ftree, name):
    if ftree is not None:
        # connection_test(ftree.left, name)
        if ftree.data == name[0]:
            ftree.link = sec__tree
            sec_tree_con_test(ftree.link, len(name), name)
            info.append(name)
        elif ftree.data > name[0]:
            connection_test(ftree.left, name)
        else:
            connection_test(ftree.right, name)


def get_ftree(ftree, name):
    if ftree is not None:
        # connection_test(ftree.left, name)
        if ftree.data == name[0]:
            ftree.link = sec__tree
            return get_sec_tree(ftree.link, len(name), name)
            info.append(name)
        elif ftree.data > name[0]:
            return connection_test(ftree.left, name)
        else:
            return connection_test(ftree.right, name)
    return None


def sec_tree_con_test(sec__tre, length, name):
    if sec__tre is not None:
        # sec_tree_con_test(sec__tre.left, length, name)
        if sec__tre.data == length:
            sec__tre.sec_data = name
            #print("We found for third tree")

            for char in name:
                se_value = ord(char)
                third_tre = third_tree.ThirdNode()
                third_tre.data = char
                third_tre.se = se_value
                sec__tre.link = third_tree.ThirdNode()
            third_tree.third_insertion(sec__tre.link, name, se_value)

            # print(char, se_value)
            #print("input is stored at third tree.")
        elif sec__tre.data > length:
            sec_tree_con_test(sec__tre.left, length, name)
        else:
            sec_tree_con_test(sec__tre.right, length, name)


def get_sec_tree(sec__tre, length, name):
    #print(sec__tre.data)
    if sec__tre is not None:
        # sec_tree_con_test(sec__tre.left, length, name)
        if sec__tre.data == length:
            # sec__tre.sec_data = name
            #print("We found for third tree")

            for char in name:
                se_value = ord(char)
            return third_tree.get_third(sec__tre.link, name, se_value)

            # print(char, se_value)
            #print("input is stored at third tree.")
        elif sec__tre.data > length:
            return get_sec_tree(sec__tre.left, length, name)
        else:
            return get_sec_tree(sec__tre.right, length, name)
    return None


def search(name, ftree):
    if name[0] == ftree.data:
        search_sec(name, ftree.link)
    elif name[0] < ftree.data:
        search(name, ftree.left)
    else:
        search(name, ftree.right)


def search_sec(name, stree):
    if len(name) == stree.data:
        search_thir(name, stree.link)
    elif len(name) < stree.data:
        search_sec(name, stree.left)
    else:
        search_sec(name, stree.right)


def search_thir(name, ttree):
    print('Searched name is found', name)


def getdata():
    def getdata(name):
        print(name)


if __name__ == '__main__':
    while True:
        name = input("Enter user name:")
        info.append(name)
        connection_test(first_tree, name)
        val=eval(input("press 1 to retrieved"))
        if val==1:
                  print('Data retrieved ', get_ftree(first_tree, name))
        # printing(sec__tree)
        val2=eval(input("press 0 to display:"))
        if val2==0:
            getdata(name)
        #choseData = input("find the username:")
        #if choseData in info:
         #   search(choseData, first_tree)
        #else:
         #   print("User not found.")


