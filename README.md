[![Build Status](https://travis-ci.org/nutshellfool/addit.svg?branch=master)](https://travis-ci.org/nutshellfool/addit)
# addit
## Add .gitignore content file via the command line

## Installation
```Bash
pip install addit
```

## Usage
```
usage: addit.py [-h] [-v] [PARAMETER [PARAMETER ...]]

Add .gitignore file via the command line

positional arguments:
  PARAMETER      the supported language in : Java ,Python ,Objective-C ,Swift
                 ,Go || the supported IDE in : JetBrains ,Xcode ,Vim ,Emacs
                 ,Eclipse || the supported OS in : macOS ,Windows ,Linux

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  display current version of addit
```
A common usage is:  
```Bash
cd your_project_path
addit Objective-C Xcode macOS
```

currently only support  

following language
* Java
* Python
* Objective-C
* Swift
* Go

following IDE
* JetBrains
* Xcode
* Vim
* Emacs
* Eclipse

following OS  
* macOS
* Windows
* Linux


*Be ware of the Capitalization and word case*  

sorry, addit is not so smart right now, this feature has added in the schedueled feature List

## Author
* Richard Li [@nutshellfool](https://twitter.com/nutshellfool)

## Notes
* Works with Python2 and Python3
* Maybe you have new idea and new feature for this, so please read the [github schedueled feature list](https://github.com/nutshellfool/addit/issues/1), and then make it.
