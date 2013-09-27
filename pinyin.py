#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '1.0'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string="", split=None):
        """
        只处理中文字符，数字，标点等返回空
        """
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)

            #result.append(self.word_dict.get(key, char).split()[0][:-1].lower())
            pychar = self.word_dict.get(key, char)
            if pychar.strip():
                pychar = pychar.split()[0][:-1].lower()

            result.append(pychar)

        if split:
            return split.join(result)
        return result


    def hanzi2pyacronym(self, string):
        """
        拼音首字母缩写
        """
        result = self.hanzi2pinyin(string=string)
        return ''.join([c[0] for c in result if c])


    def all2pinyin(self, string="", split=None):
        """
        中文字符返回拼音，数字，标点等返回原始字符
        """
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)

            pychar = self.word_dict.get(key, char)
            if pychar != char:
                pychar = pychar.split()[0][:-1].lower()
                pychar = pychar if pychar else char

            result.append(pychar)

        if split:
            return split.join(result)
        return result


    def all2pyacronym(self, string):
        """
        拼音首字母缩写,包含原有字符串英文，标点和数字
        """
        result = self.all2pinyin(string=string)
        return ''.join([c[0] for c in result if c])

if __name__ == "__main__":
    test = PinYin()
    test.load_word()

    def run_test(string):
        print
        print "in: %s" % string
        print 'convert just Hanzi:'
        print "out: %s" % ''.join(test.hanzi2pinyin(string=string))
        print "out: %s" % ''.join(test.hanzi2pinyin(string=string, split="-"))
        print "out: %s" % test.hanzi2pyacronym(string=string)

        print 'convert all:'
        print "out: %s" % ''.join(test.all2pinyin(string=string))
        print "out: %s" % ''.join(test.all2pinyin(string=string, split="-"))
        print "out: %s" % test.all2pyacronym(string=string)
        print '-' * 20


    #简单字符串
    string = 'Chrome浏览器版本29'
    #string = u'猎'
    run_test(string)

    #补充例子，复杂字符串
    string = u'植物大战僵尸2：奇妙时空之旅（Plants vs. Zombies 2: Its About Time）'
    run_test(string)
