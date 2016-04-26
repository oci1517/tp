# -*- coding: utf-8 -*-

from main import *

def test_case_max_word_len(sentence, expected):
    (i, size) = max_word_len(sentence)

    if (i, size) != expected and show_only_failures or not show_only_failures:
        print 40*"="
        print "testcase max_word_len on ... ", sentence.encode('utf-8')
        print "got", (i, size), "expected", expected
        print "PASS : ", "OK" if (i, size) == expected else 10*"=" + "> FAILURE"
        print "longest word : ", sentence[i:i+size].encode('utf-8')

def test_max_word_len():
    test_case_max_word_len(u"Je suis dans la joie", (3, 4))
    test_case_max_word_len(u"Je suis dans la joie éternellement", (21, 13))
    test_case_max_word_len(u"", (0, 0))


def test():
    global show_only_failures
    show_only_failures = True
    test_max_word_len()

test()
