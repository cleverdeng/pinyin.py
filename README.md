pinyin.py
=========

汉字转拼音,With Python


Example:

    from pinyin import PinYin

    test = PinYin()

Out:

    test.hanzi2pinyin(string='钓鱼岛是中国的')
    ['diao', 'yu', 'dao', 'shi', 'zhong', 'guo', 'de']
    test.hanzi2pinyin_split(string='钓鱼岛是中国的', split="-")
    diao-yu-dao-shi-zhong-guo-de

    test.hanzi2pinyin(string='hello world 123')
    out: [u'helloworld123']
    test.hanzi2pinyin_split(string='hello world 123', split="_")
    out: helloworld123

    test.hanzi2pinyin(string='hello 中国 123')
    out: [u'hello', 'zhong', 'guo', u'123']
    test.hanzi2pinyin_split(string='hello 中国 123', split="_")
    out: hello_zhong_guo_123
