#!/usr/bin/env python

import sys
from distutils.core import setup

if sys.version_info < (2, 2):
    raise AssertionError("Python 2.2 or later required")

setup(name="tlslite",
      version="0.3.8",
      author="Trevor Perrin",
      author_email="trevp@trevp.net",
      url="http://trevp.net/tlslite/",
      description="tlslite implements SSL and TLS with SRP, shared-keys, cryptoID, or X.509 authentication.",
      license="public domain",
      scripts=["scripts/tls.py", "scripts/tlsdb.py"],
      packages=["tlslite", "tlslite.utils", "tlslite.integration"])
