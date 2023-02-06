#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of the chess-problem-visuals library.
# Copyright (C) 2012-2021 Philipp Polland <contact@philipp-polland.dev>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import chess_problem_visuals.board

QUEEN_SVG_STRING = """<g id="white-queen" class="white queen" fill="#fff" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 12a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM24.5 7.5a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM41 12a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM16 8.5a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM33 9a2 2 0 1 1-4 0 2 2 0 1 1 4 0z"/><path d="M9 26c8.5-1.5 21-1.5 27 0l2-12-7 11V11l-5.5 13.5-3-15-3 15-5.5-14V25L7 14l2 12zM9 26c0 2 1.5 2 2.5 4 1 1.5 1 1 .5 3.5-1.5 1-1.5 2.5-1.5 2.5-1.5 1.5.5 2.5.5 2.5 6.5 1 16.5 1 23 0 0 0 1.5-1 0-2.5 0 0 .5-1.5-1-2.5-.5-2.5-.5-2 .5-3.5 1-2 2.5-2 2.5-4-8.5-1.5-18.5-1.5-27 0z" stroke-linecap="butt"/><path d="M11.5 30c3.5-1 18.5-1 22 0M12 33.5c6-1 15-1 21 0" fill="none"/></g>"""  # noqa: E501


def paint_nxn_board(n: int = 8, SQUARE_SIZE: int = 16, size: int = None, ipy_off=False, Qs: list = None,
                    KnPs: list = None):
    board = chess_problem_visuals.board.Board(n, SQUARE_SIZE, size, ipy_off)

    if Qs:
        for file_index, rank_index in enumerate(Qs):
            board.add_piece((file_index, rank_index), "Q")
    if KnPs:
        for file_index, rank_index in enumerate(KnPs[0]):
            board.add_piece((file_index, rank_index), "K")
        for file_index, rank_index in enumerate(KnPs[1]):
            board.add_piece((file_index, rank_index), "p")

    return board
