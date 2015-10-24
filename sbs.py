# -*- coding: utf-8 -*-

import re
from bitmap import BitMap

class Splitter(object):
    def __init__(self):
        self._words = None

    def load(self, words):
        self._words = frozenset(filter(lambda w: len(w) > 1, words))

    def split(self, w):
        r = self._split(w)
        if r and len(r) == 1:
            return None
        return r

    def _split(self, w):
        candidate_words = self._munch(w)

        for ending in ['', 's', 'er', 'en']:
            candidates_with_ending = filter(lambda c: self._is_valid_ending(c, w), self._append_ending(candidate_words, ending))
            r = self._explorer_subspace(candidates_with_ending, w)
            if r:
                return r
        return None

    def _append_ending(self, xs, ending):
        return map(lambda s: s+ending, xs)

    def _is_valid_ending(self, x, w):
        return w[:len(x)] == x

    def _explorer_subspace(self, xs, w):
        for x in xs:
            w_tail = w[len(x):]

            if len(w_tail) == 0:
                return [x]

            ys = self._split(w_tail)
            if ys:
                return [x] + ys

        return None

    def _munch(self, w):
        words = []
        for j in range(len(w)+1, 1, -1):
            if w[:j] in self._words:
                words.append(w[:j])
        return words
