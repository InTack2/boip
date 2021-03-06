# boip
[![PyPI Versions](https://img.shields.io/pypi/v/boip.svg)](https://pypi.org/project/boip)
[![Downloads](https://pepy.tech/badge/boip)](https://pepy.tech/project/boip)
[![license](https://img.shields.io/pypi/l/boip)](https://pypi.org/project/boip)
[![Supported Versions](https://img.shields.io/pypi/pyversions/boip.svg)](https://pypi.org/project/boip)
[![pytest](https://codecov.io/gh/InTack2/boip/branch/master/graph/badge.svg)](https://codecov.io/gh/InTack2/boip)
[![code style](https://img.shields.io/badge/code%20style-flake8-000000.svg)](https://pypi.org/project/flake8/)  

[Japanese](https://github.com/InTack2/boip/blob/master/README_JP.md)

boip is an abbreviation for Boiler Plate.  

A library that generates code from code templates based on the answers to some questions.  
I am a technical artist.  
Therefore, the template to be added has a lot of code generation such as Maya related.  


## 1. How to use.
### 1.1. pip install
```bash
python -m pip install boip
```

### 1.2. Run boip with CLI.
```bash
python -m boip
```

### 1.3. CD to the folder where you want to place the template.
```bash
cd "Folder path where you want to place the template."
```

### 1.4. Choose a template and answer your questions.

[![Image from Gyazo](https://i.gyazo.com/b3127fecbe5af7ea40fdce9a09e86c25.gif)](https://gyazo.com/b3127fecbe5af7ea40fdce9a09e86c25)

### 1.5. Check the generated folder.
It is copied under cd with the last selected folder name.  
Since I chose "Maya Qt-MVC" this time, a template of Maya + Qt + MVC pattern is generated.  

[![Image from Gyazo](https://i.gyazo.com/fc49047b094d2d9dfe305da46ad30f0a.gif)](https://gyazo.com/fc49047b094d2d9dfe305da46ad30f0a)



## 2. Add your own template.
Prepare a code template (BoipSet) in advance.
Then specify the folder path where BoipSet is located with the -s flag.
```
python -m boip -s "Target folder path."
```

### 2.1. What is BoipSet?
The following two are set as a Boip Set.  
- After asking a question, a folder named "template" to use for replacement.  
- Configuration file named boip.yaml.  
  
[reference](https://github.com/InTack2/boip/tree/master/src/boip/preset)  

#### 2.1.1. How to write boip.yaml.
``` yaml
title: MayaQt-MVC # template name
convertExtensions: # distExtension srcExtension(The same extension is okay.)
  py: py
  ui: ui
question: # question list
  - name: tool_name # Name to use for replacement. Use with {Name} for stationery.
    message: "Tool name?" # Question.
    default: sampleWindow # Default Value.

  - name: maya_version
    message: "What version of Maya are you using?"
    default: 2020
```

#### 2.1.2. How to make a template.
The folders under template will be copied. After that, the inside of {name} is converted by the answer to the question.  
It is expected that automatic generation will be included in the future, but currently it is manual.  

Example)In the case of "MayaQt-MVC" above.  
I have two questions, {tool_name} and {maya_version}.

- template
```python:sample.py
import sys

print("{tool_name}")
print("{maya_version}")
```

- answer the questions.
```bash
Tool name? > sampleWindow
What version of Maya are you using? > 2020
```

- After generation.
The answer to the question will be converted to the following.  

```python:sample.py
import sys

print("sampleWindow")
print("2020")
```

If you have a nice template, Please make a merge request!