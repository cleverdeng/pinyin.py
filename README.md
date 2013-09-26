pinyin.py
=========

汉字转拼音,With Python

Example:

    from pinyin import PinYin

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
    string = u'Chrome浏览器版本29'
    run_test(string)

    #补充例子，复杂字符串
    string = u'植物大战僵尸2：奇妙时空之旅（Plants vs. Zombies 2: Its About Time）'
    run_test(string)


Out:

    test.hanzi2pinyin(string='钓鱼岛是中国的')
    ['diao', 'yu', 'dao', 'shi', 'zhong', 'guo', 'de']
    test.hanzi2pinyin_split(string='钓鱼岛是中国的', split="-")
    diao-yu-dao-shi-zhong-guo-de

-------

Update:

    2013-09-26  wklken
                1.[del] split合并到同一个方法中，作为split参数判断处理
                2.[add] all2pinyin方法，使得模块可以处理返回含有英文，数字，标点符号的字符串
                3.[add] acronym方法，返回拼音首字母字符串
                4.[fix] 修复原有方法传入含空格字符串异常的问题
