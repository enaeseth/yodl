yodl
====

[![Build Status](https://travis-ci.org/enaeseth/yodl.svg?branch=master)](https://travis-ci.org/enaeseth/yodl)
[![PyPI](https://img.shields.io/pypi/v/yodl.svg)](https://pypi.python.org/pypi/yodl)

Use [PyYAML](http://pyyaml.org/) to load a document into a Python OrderedDict.

```py
import yaml
import yodl

data = yaml.load(input, yodl.OrderedDictYAMLLoader)
```

### Installing

yodl is available on [PyPI](https://pypi.python.org/pypi/yodl).
