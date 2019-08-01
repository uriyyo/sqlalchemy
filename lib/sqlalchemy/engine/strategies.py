# engine/strategies.py
# Copyright (C) 2005-2019 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""Deprecated mock engine strategy used by Alembic.


"""

from .mock import MockConnection  # noqa


class MockEngineStrategy(object):
    MockConnection = MockConnection
