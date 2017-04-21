# -*- coding: utf-8 -*-

import pytest
import FuzzyRoutines


class TestBaseMethods():

    @pytest.fixture(scope='class', autouse=True)
    def init(self):
        pass

    def test_DiapasonParser(self, capsys):
        # positive tests
        assert FuzzyRoutines.DiapasonParser("1") == [1]
        assert FuzzyRoutines.DiapasonParser("1,5") == [1, 5]
        assert FuzzyRoutines.DiapasonParser("1-5") == [1, 2, 3, 4, 5]
        assert FuzzyRoutines.DiapasonParser("8-10, 1-5, 6") == [1, 2, 3, 4, 5, 6, 8, 9, 10]
        assert FuzzyRoutines.DiapasonParser("11, 11, 12, 12, 1-5, 3-7") == [1, 2, 3, 4, 5, 6, 7, 11, 12]

        # negative tests
        assert FuzzyRoutines.DiapasonParser(12345) == []
        assert FuzzyRoutines.DiapasonParser("") == []
        assert FuzzyRoutines.DiapasonParser("-") == []
        assert FuzzyRoutines.DiapasonParser("1-") == []
        assert FuzzyRoutines.DiapasonParser(",") == []
        assert FuzzyRoutines.DiapasonParser("1,") == []
