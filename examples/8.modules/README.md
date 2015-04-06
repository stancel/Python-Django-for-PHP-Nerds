# Modules

The real power of Python is in the module library.  Many modules come bundled
with Python, and there are literally thousands of useful modules available to
you simply by typing:

    pip install module_name

## Some built-ins to get you started


### os

* `os.environ` is a dictionary of the shell environment variables
* `os.path.*` is a bunch of utilities to operate on path names
* `os.chdir` is a means of changing to a direction from within your program

https://docs.python.org/3/library/os.html


### sys

* `sys.argv` is a list of arguments passed to the script at run time
* `sys.exit()` exits your program with whatever code is passed to it
* `sys.stderr` and `sys.stdin` are your STDERR and STDIN
* `sys.path` is where Python looks for modules when you issue `import`

https://docs.python.org/3/library/sys.html


### random

* `random.randint()` returns a random integer
* `random.choice()` selects a random value from a list

https://docs.python.org/3/library/random.html


### hashlib

* `hashlib.md5` is a function to generate MD5 hashes
* `hashlib.sha1` ditto for SHA1
* `hashlib.sha256` ...you get the idea

https://docs.python.org/3/library/hashlib.html


### re

Your regular expression library.

* `re.match` tests whether something matches your expression
* `re.compile` lets you pre-compile your expression
* `re.sub` allows you to substitute stuff in your strings

https://docs.python.org/3/library/re.html


## Some publicly-available packages

As I said, there are literally *thousands* of excellent Python packages
available to you, but here's a sample.


### dateutil, arrow, delorean

Date math can be complicated, so there are a number of libraries out there to
help.  `dateutil` does some really great work with intervals and deltas, while
`arrow` and `delorean` take some of the pain out of dealing with things like
time zones, conversions, and math.

* https://pypi.python.org/pypi/python-dateutil
* https://pypi.python.org/pypi/arrow
* https://pypi.python.org/pypi/Delorean

### pyephem

Given a latitude, longitude, and planetary body, `pyephem` will be able to tell
you whether the sun is up and if Jupiter is visible.

https://pypi.python.org/pypi/pyephem


### Markdown

Parse markdown content (like this file) into various formats, all within your
program.

https://pypi.python.org/pypi/Markdown

### Celery

Asynchronous code execution by way of communicating with a queue server.  In
Python, it's as easy as issuing a few function calls.

https://pypi.python.org/pypi/celery

### Django

Yes, Django is a module, just like everything else.  You install it with `pip`,
and use it just by:

    import django

Of course, as modules go, Django is very complicated and pretty big.

https://pypi.python.org/pypi/Django
