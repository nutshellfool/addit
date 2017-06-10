addit
=====
.. image:: https://travis-ci.org/nutshellfool/addit.svg?branch=master
    :target: https://travis-ci.org/nutshellfool/addit

Add .gitignore content file via the command line
-------------------------------------------

Installation
------------

::

    pip install addit
    
or update

::

    pip install addit -U

Usage
-----

::

    usage: addit.py [-h] [-v] [PARAMETER [PARAMETER ...]]
    
    Add .gitignore file via the command line
    
    positional arguments:
      PARAMETER      the supported language in : Java, Python, Objective-C, Swift
                 Android, Go, Maven, Gradle, Node || the supported IDE in : JetBrains, Xcode, Vim, Emacs
                 , Eclipse || the supported OS in : macOS, Windows, Linux
                 
    optional arguments:
      -h, --help     show this help message and exit
      -v, --version  display current version of addit
      -a, --auto     auto detect the project type

a common usage

for iOS (Objective-C) project (using Xcode as IDE) on macOS

::

    cd your_project_path
    addit Objective-C Xcode macOS

for Android project (using Android Studio as IDE) on macOS

::

    cd your_project_path
    addit Android JetBrains macOS

or you can try auto detect mode (beta)

::

    cd your_project_path
    addit -a

currently only support

following language (all support auto detect)

- Java
- Python
- Objective-C
- Swift
- Android
- Go
- Maven
- Gradle
- Node

following IDE

- JetBrains (support auto detect)
- Xcode (support auto detect)
- Vim
- Emacs
- Eclipse

following OS

- macOS
- Windows
- Linux

Author
------

-  Richard Li (`@nutshellfool <https://twitter.com/nutshellfool>`_)

Notes
-----
- Works with Python2 and Python3
- Maybe you have new idea and new feature for this, so please read the (`github schedueled feature list <https://github.com/nutshellfool/addit/issues/1>`_), and then make it.
