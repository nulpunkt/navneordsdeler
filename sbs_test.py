# -*- coding: utf-8 -*-

import unittest

from sbs import Splitter

class TestSplitter(unittest.TestCase):
    def setUp(self):
        self.t = Splitter()
        self.t.load([u"test", u"hest", u"parkering", "billet", "automat", u"universitet", u'forlag'])

    def test_we_can_split_to_known_words(self):
        self.assertEquals([u"test", u"hest"], self.t.split(u"testhest"))

    def test_we_ignore_the_obvious(self):
        self.assertEquals(None, self.t.split(u"testr"))
        self.assertEquals(None, self.t.split(u"tests"))

    def test_we_can_handle_some_conjugations(self):
        self.assertEquals([u"test", u"hester"], self.t.split(u"testhester"))
        self.assertEquals([u"test", u"hesten"], self.t.split(u"testhesten"))
        self.assertEquals([u"testen", u"hesten"], self.t.split(u"testenhesten"))
        self.assertEquals([u"parkerings", u"billet", "automat"], self.t.split(u"parkeringsbilletautomat"))

if __name__ == '__main__':
    unittest.main()
