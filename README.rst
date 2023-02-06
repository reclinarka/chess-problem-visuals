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

    pip install pip install git+https://github.com/reclinarka/chess-problem-visuals

Documentation <WIP>
-------------------



Features <WIP>
--------

* IPython/Jupyter Notebook integration.

    .. code:: python

        >>> paint_nxn_board(9)

    .. image:: https://i.imgur.com/5OWDVxJ.png
        :alt: A 9x9 board

* N-Queens Problem

    .. code:: python

        >>> paint_nxn_board(8,Qs=[])
