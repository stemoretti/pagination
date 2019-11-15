Pagination Filter Plugin for Pelican
====================================

This plugin adds a filter function ``pagination`` that returns a list
of numbers from 1 to n and abbreviated with 0 if too long.

Usage
-----

Enable the plugin in your pelicanconf.py:

.. code:: python

  PLUGINS = [ 'pagination' ]

Use the filter in a theme as follows:

.. code:: html

  <ul>
  {% for cpage articles_paginator.num_pages | pagination(articles_page.number) %}
    <li>
    {% if cpage != 0 %}
      <a href="{{ articles_paginator.page(cpage).url }}">{{ cpage }}</a>
    {% else %}
      <span>...</span>
    {% endif %}
    </li>
  {% endfor %}
  </ul>

Credits
-------

The filter function is a modified version of the original in
`this stackexchange answer <stackexchange_>`_.

.. _stackexchange:
  https://codereview.stackexchange.com/questions/15235/how-to-generate-numbers-for-pagination#answer-15239
