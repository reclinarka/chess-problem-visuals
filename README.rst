chess-problem-visuals: A python visualization tool for chess based Problems
========================================
.. image:: https://github.com/niklasf/python-chess/workflows/Test/badge.svg
    :target: https://github.com/niklasf/python-chess
    :alt: Heavily inspried by

.. image:: https://badge.fury.io/py/chess.svg
    :target: https://pypi.python.org/pypi/chess
    :alt: PyPI package

Introduction
------------
This Module is meant as a tool for visualizing Chess based Problems like the n-Queens Problem or the Knight Problem


Installing
----------

Requires Python 3.7+. Download and install the latest release:

::

    pip install git+https://github.com/reclinarka/chess-problem-visuals

Documentation <WIP>
-------------------



Features <WIP>
--------

* IPython/Jupyter Notebook integration.

    .. code:: python

        >>> Board(15)
        >>> test.add_piece((2,2),"k")
        >>> test.add_piece((2,3),"P")

    .. image:: https://i.imgur.com/vJqYaMa.png
        :alt: A 9x9 board

* N-Queens Problem

    .. code:: python

        >>> problem_board(10,Qs=[1,None,2,3])

    .. image:: https://i.imgur.com/n8azSne.png
        :alt: A 9x9 board

* Knight Problem

    .. code:: python

        >>> problem_board(10,KnPs=[ (7,6), [ (2,2), (1,4), (5,9) ] ] )

    .. image:: https://i.imgur.com/MCjGRj9.png
        :alt: A 9x9 board