pyoembed
========

.. image:: https://ci.rgm.io/buildStatus/icon?job=pyoembed
   :target: https://ci.rgm.io/job/pyoembed/

A Python library for oEmbed that supports auto-discovered and manually
included providers.


Installation
------------

::

   $ pip install pyoembed


Usage
-----

The library provides a function that should be called to automatically embed
the url content, and it is called ``oEmbed``:

.. sourcecode:: python

   from pyoembed import oEmbed, PyOembedException

   try:
       # maxwidth and maxheight are optional.
       data = oEmbed('http://www.youtube.com/watch?v=_PEdPBEpQfY',
                     maxwidth=640, maxheight=480)
   except PyOembedException, e:
       print 'An error was ocurred: %s' % e

   # data is a dict with keys that will depends on the media type. You should
   # choose how to display the content based on the data['type'] value and
   # the oEmbed spec ( http://oembed.com/ ).
   if data['type'] == 'video':
       print data['html']

   # and it goes... Someday we will provide default renderes for each media
   # type.


Addition of new providers
-------------------------

pyoembed tries to cover the major oEmbed providers, and should works for any
provider that supports oEmbed auto-discover out-of-the box, however your
favorite provider may be unsupported yet! :(

To add it, create a file inside the ``pyoembed.providers`` package, based on
the following example:

.. sourcecode:: python

   from pyoembed.providers import BaseProvider


   class InstagramProvider(BaseProvider):

       # priority of the provider. Increase it if the provider isn't well known
       priority = 10

       # url schemas that are supported by the provider.
       # re.compile'd regex are allowed.
       oembed_schemas = ['http://instagram.com/p/*',
                         'http://instagr.am/p/*']

       # api endpoint that answers to oEmbed requests for the provider.
       oembed_endpoint = 'http://api.instagram.com/oembed'


You will also need to add some test urls of your provider to the
``integration_test.py`` file, and run it to see if everything is ok.

If everything works, feel free to send a pull request to add the provider:

https://github.com/rafaelmartins/pyoembed/pulls

That's it!

