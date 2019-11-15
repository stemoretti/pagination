"""
Pagination Filter for Pelican
=============================

Add a filter to generate a list of numbers that can be used for pagination
"""

from pelican import signals

# https://codereview.stackexchange.com/questions/15235/how-to-generate-numbers-for-pagination#answer-15239
def pagination(n, page):
    """
    Return a list of numbers from 1 to `n`
    and abbreviated with 0 if too long.

    >>> pagination(5, 3)
    [1, 2, 3, 4, 5]
    >>> pagination(10, 10)
    [1, 2, 0, 8, 9, 10]
    >>> pagination(20, 1)
    [1, 2, 3, 0, 19, 20]
    >>> pagination(80, 30)
    [1, 2, 0, 28, 29, 30, 31, 32, 0, 79, 80]
    """
    assert(0 < n)
    assert(0 < page <= n)

    if n <= 6:
        return list(range(1, n + 1))

    pages = (set(range(1, 3))
             | set(range(max(1, page - 2), min(page + 3, n + 1)))
             | set(range(n - 1, n + 1)))

    def display():
        last_page = 0
        for p in sorted(pages):
            if p - last_page == 2:
                yield p - 1
            elif p - last_page > 2:
                yield 0
            yield p
            last_page = p

    return list(display())

def add_filter(pelican):
    pelican.env.filters.update({'pagination': pagination})

def register():
    signals.generator_init.connect(add_filter)
