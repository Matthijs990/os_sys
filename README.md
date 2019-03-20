##OS_Sys

Newest features:
===========================
os_sys, wifi and fail have been updated




Index:
===========================

Installation
description
loading_bars

Installation:
===========================

Installation command (in your shell, ex. cmd, bash): python -m pip install --upgrade os_sys
                                                                                

description:
===========================
os_sys is a package for python 3.
    




loading_bars:
Easy progress visualization for Python
==================================

####Pypi



Bars
----

There are 7 progress bars to choose from:

- ``Bar``
- ``ChargingBar``
- ``FillingSquaresBar``
- ``FillingCirclesBar``
- ``IncrementalBar``
- ``PixelBar``
- ``ShadyBar``

To use them, just call ``next`` to advance and ``finish`` to finish:

<code>    from os_sys.progress import bar

    bar = Bar('Processing', max=20)
    #the bar reads the text "Processing" and has 20 parts, so after calling bar.next() 20 times, it will be full.
    for i in range(20):
        # Do some work
        bar.next()
    bar.finish()</code>
or use any bar of this class as a context manager:

<code>    from os_sys.progress import bar

    with Bar('Processing', max=100) as bar:
        for i in range(100):
            # Do some work
            bar.next()</code>

The result will be a bar like the following:

<code>    Processing |#############                   | 42/100</code>

To simplify the common case where the work is done in an iterator, you can
use the ``iter`` method:

<code>    for i in Bar('Processing').iter(it):
        # Do some work</code>
        
Progress bars are very customizable, you can change their width, their fill
character, their suffix and more:

<code>    bar = Bar('Loading', fill='@', suffix='%(percent)d%%')</code>

This will produce a bar like the following: ::

<code>    Loading |@@@@@@@@@@@@@                   | 42%</code>

You can use a number of template arguments in ``message`` and ``suffix``:

==========  ================================
Name        Value
==========  ================================
index       current value
max         maximum value
remaining   max - index
progress    index / max
percent     progress * 100
avg         simple moving average time per item (in seconds)
elapsed     elapsed time in seconds
elapsed_td  elapsed as a timedelta (useful for printing as a string)
eta         avg * remaining
eta_td      eta as a timedelta (useful for printing as a string)
==========  ================================

Instead of passing all configuration options on instatiation, you can create
your custom subclass:

<code>    class FancyBar(Bar):
        message = 'Loading'
        fill = '*'
        suffix = '%(percent).1f%% - %(eta)ds'</code>

You can also override any of the arguments or create your own:

<code>    class SlowBar(Bar):
        suffix = '%(remaining_hours)d hours remaining'
        @property
        def remaining_hours(self):
            return self.eta // 3600</code>


Spinners
========

For actions with an unknown number of steps you can use a spinner:


<code>    from os_sys.progress import spinner

    spinner = Spinner('Loading ')
    while state != 'FINISHED':
        # Do some work
        spinner.next()</code>

There are 5 predefined spinners:

- ``Spinner``
- ``PieSpinner``
- ``MoonSpinner``
- ``LineSpinner``
- ``PixelSpinner``

Next up: We're working on the big 2.0.0 update!

home:
===========================
    
    Please visit our websites:
    
    Matthijs990's one and only post-every-script-you-want site:
    https://python-libs-com.webnode.nl/
    
    CenTdemeern1's Project Crossroad:
    https://CenTdemeern1.github.io/
    
