#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    def __init__(self):
        self.word_dict = {}
        dirname, filename = os.path.split(__file__)        
        dict_file = os.path.join(dirname, 'word.data')
        self.load_word(dict_file)
        
    def load_word(self, dict_file):        
        if not os.path.exists(dict_file):
            raise IOError("NotFoundFile")
        if len(self.word_dict.keys()) > 0:
            print 'Dictionary already loaded'
            return
        with file(dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]
        f_obj.close()

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
    string = "钓鱼岛是中国的"
    print "in: %s" % string
    print "out: %s" % str(test.hanzi2pinyin(string=string))
    print "out: %s" % test.hanzi2pinyin_split(string=string, split="-")
