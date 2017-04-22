# -*- coding: utf-8 -*-
__created_date__ = "2017/4/18"

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QVBoxLayout, QHBoxLayout
from PyQt4.QtCore import QSize
from dialog_classes import *

qtCreatorFile = "psychtest.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class PsychTest(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.RutterKidsButton.clicked.connect(self.rutter_kids_test)
        self.EysenckYoungButton.clicked.connect(self.eysenck_young_test)
        self.EysenckAllButton.clicked.connect(self.eysenck_all_test)
        self.ChildBehaviorChecklistButton.clicked.connect(self.child_behavior_checklist_test)
        self.InterpersonalTrustScaleButton.clicked.connect(self.interpersonal_trust_scale_test)
        self.SelfEsteemScaleButton.clicked.connect(self.self_esteem_scale_test)

    def self_esteem_scale_test(self):
        '''自尊量表SES测试'''
        dialog = TestDialog()
        dialog.setWindowTitle(u"自尊量表SES")
        dialog.context.setText(u"测试说明文档")

        # Dialog布局器
        d_layout = QVBoxLayout()
        d_layout.addWidget(dialog.context)
        # d_layout.addWidget(test_case1)

        # 对TestCase进行组装
        test_case1 = TestCase()
        test_case1.setQuestion(u"1.测试问题")

        myQListWidgetItem = QListWidgetItem(dialog.qlist)
        myQListWidgetItem.setSizeHint(QSize(100, 100))
        dialog.qlist.addItem(myQListWidgetItem)
        dialog.qlist.setItemWidget(myQListWidgetItem, test_case1)


        dialog.setLayout(d_layout)
        dialog.exec_()

    def rutter_kids_test(self):
        '''Rutter儿童行为问卷测试'''
        pass

    def eysenck_young_test(self):
        '''艾森克人格测评（少年版）'''
        pass

    def eysenck_all_test(self):
        '''艾森克人格问卷（全套）'''
        pass

    def child_behavior_checklist_test(self):
        '''儿童行为量表测试'''
        pass

    def interpersonal_trust_scale_test(self):
        '''人际信任量表测试'''
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = PsychTest()
    window.show()
    sys.exit(app.exec_())