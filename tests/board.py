from unittest import TestCase

from src.board import Board, BadTuningError, StringNotInBoardError, NoteNotFoundError
from tests.helpers import standard_board, abcdef_board

class BoardTest(TestCase):

    def setUp(self):
        self.board = Board()

    def test_standard_tuning(self):
        self.assertEquals(self.board.fretboard, standard_board)

    def test_other_tuning(self):
        board = Board('abcdef')
        self.assertEquals(board.fretboard, abcdef_board)

    def test_none_tuning(self):
        self.assertRaises(BadTuningError, Board, None)

    def test_empty_tuning(self):
        self.assertRaises(BadTuningError, Board, '')

    def test_int_tuning(self):
        self.assertRaises(BadTuningError, Board, 1)

    def test_get_note_from_string_6(self):
        expected = ('a', 2)
        self.assertEquals(expected, self.board.get_note(6, 5))

    def test_get_note_from_string_5(self):
        expected = ('c', 3)
        self.assertEquals(expected, self.board.get_note(5, 3))

    def test_get_note_from_string_4(self):
        expected = ('g#', 3)
        self.assertEquals(expected, self.board.get_note(4, 6))

    def test_get_note_from_string_3(self):
        expected = ('a', 3)
        self.assertEquals(expected, self.board.get_note(3, 2))

    def test_get_note_from_string_2(self):
        expected = ('c#', 4)
        self.assertEquals(expected, self.board.get_note(2, 2))

    def test_get_note_from_string_1(self):
        expected = ('b', 4)
        self.assertEquals(expected, self.board.get_note(1, 7))

    def test_get_note_none_string(self):
        self.assertRaises(StringNotInBoardError, self.board.get_note, None, 3)

    def test_get_note_none_fret(self):
        self.assertRaises(StringNotInBoardError, self.board.get_note, 1, None)

    def test_find_note(self):
        expected = [('5', 1), ('6', 6)] 
        self.assertEquals(expected, self.board.find_note('a#', 2))

    def test_find_unexistent_note(self):
        self.assertRaises(NoteNotFoundError, self.board.find_note, 'h', 3)

