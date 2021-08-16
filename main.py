# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import weibo_model

def print_hi(name):
    res = '\u4e48\u6d3b\u7740'
    print(res.encode('utf-8').decode('utf-8'))
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    w = weibo_model.weibo_model()
    w.wang()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
