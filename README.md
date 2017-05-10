[![Build Status](https://travis-ci.org/nutshellfool/addit.svg?branch=master)](https://travis-ci.org/nutshellfool/addit)
# addit
## instant .gitignore file add helper via the command line

## Installation
```Bash
pip install addit
```

## Usage
```
usage: addit [-h] [-v] [LANGUAGE [LANGUAGE ...]]

instant .gitignore file add helper via the command line

positional arguments:
  LANGUAGE       the language of supported in : Java ,Python ,Objective-C
                 ,Swift ,Go

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  display current version of addit
```
A common usage is:  
```Bash
cd your_project_path
addit Java
```

currently only support
* Java
* Python
* Objective-C
* Swift
* Go

*Be ware of the Capitalization and word case*  

sorry, addit is not so smart right now, this feature has added in the schedueled feature List

## Author
* Richard Li [@nutshellfool](https://twitter.com/nutshellfool)

## Notes
* Works with Python2 and Python3
* Maybe you have new idea and new feature for this, so please read the [github schedueled feature list](https://github.com/nutshellfool/addit/issues/1), and then make it.
