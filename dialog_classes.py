# -*- coding: utf-8 -*-

__created_date__ = "2017/4/19"

from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QRadioButton
from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtGui import QVBoxLayout, QHBoxLayout
from PyQt4.QtGui import QButtonGroup
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLayout

h_box = QHBoxLayout()
v_box = QVBoxLayout()


class TestDialog(QDialog):
    '''测试类用以实例化不同类型测试对话框'''
    def __init__(self):
        super(TestDialog, self).__init__()
        # 对话框的Icon图标
        self.setWindowIcon(QIcon("huijia_logo.jpg"))
        # 对话框tittle
        self.tittle = None
        # 测试说明文档
        self.context = QLabel()
        # 用以放置N道TestCase的QtLlistWidget
        # self.qlist = QListWidget()

    def caculate(self):
        '''将用户每道题目选择的答案对应的分数累加，得到测试总分数'''
        pass


class TestCase(object):
    '''代表每道测试题目'''
    def __init__(self):
        super(TestCase, self).__init__()
        # TestCase的question，应该是个QLabel实例
        self.question = QLabel()
        # 代表唯一答案的radioButton字典，key="radioButton对象实例"、value="每一项答案分数"
        self.b_group = QButtonGroup()
        # 记录用户选择的对该question的答案
        self.choice = None














