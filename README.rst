===========
Local CNAME
===========

.. image:: https://img.shields.io/pypi/v/local-cname.svg
   :target: https://pypi.python.org/pypi/local-cname
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/local-cname.svg
   :target: https://pypi.python.org/pypi/local-cname
   :alt: Development Status

.. image:: https://img.shields.io/pypi/pyversions/local-cname.svg
   :target: https://pypi.python.org/pypi/local-cname
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/l/local-cname.svg
   :target: https://github.com/hjacobs/local-cname/blob/master/LICENSE
   :alt: License

Installation:

.. code-block::

    $ sudo pip install -U local-cname

Usage:

.. code-block::

    $ sudo local-cname FROM_DNS_NAME TO_DNS_NAME

Example:

.. code-block::

    $ sudo local-cname google.com duckduckgo.com
    $ ping google.com


