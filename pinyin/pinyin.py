#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
    Modified by anakin.yan@gmail.com
"""

__all__ = ["PinYin"]

import pkgutil


class PinYin(object):
    def __init__(self):
        __package__ = 'pinyin'
        self.word_dict = {}
        self.data = pkgutil.get_data(__package__, 'data/word.data')

    def load_word(self):
        for line in self.data.split('\n'):
            self.word_dict[line[:5].strip()] = line[8:]

    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result

    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)


if __name__ == "__main__":
    test = PinYin()
    test.load_word()
    string = "钓鱼岛是中国的"
    print "in: %s" % string
    print "out: %s" % str(test.hanzi2pinyin(string=string))
    print "out: %s" % test.hanzi2pinyin_split(string=string, split="-")
