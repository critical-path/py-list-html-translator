[![Build Status](https://travis-ci.com/critical-path/py-list-html-translator.svg?branch=master)](https://travis-ci.com/critical-path/py-list-html-translator)

## py-list-html-translator v1.0.0

py-list-html-translator is a Python module that translates lists to HTML.

## Introduction

Writing HTML is tedious.  py-list-html-translator makes it fun!

With py-list-html-translator, we use strings to define HTML elements and nested lists to describe the hierarchical relationships between them.

## Defining HTML Elements

To define an HTML element, we use a string containing one or more special characters.

- "@" for name 
- "#" for id 
- "." for class
- "&" for other attributes in the form of key-value pairs
- "$" for text

```
["@h1"]
<h1></h1>

["@h1 #id"]
<h1 id="id"></h1>

["@h1 .class"]
<h1 class="class"></h1>

["@h1 &key=\"value\""]
<h1 key="value"></h1>

["@h1 $text"]
<h1>text</h1>
```

py-list-html-translator supports void elements, which have no closing tags.

```
[“@col”]
<col>

["@meta &charset=\"utf-8\""]
<meta charset="utf-8">

["@link &rel=\"stylesheet\" &href=\"./css/app.css\""] 
<link rel="stylesheet" href="./css/app.css">
```

Notes:

It is good practice to enclose attribute values in quotation marks and to escape the quotation marks.

__Good__:

```
[“@h1 &arbitrary-key=\"arbitrary-value\””] 
<h1 arbitrary-key="arbitrary-value"></h1>
```

__Bad__:

```
[“@h1 &arbitrary-key=arbitrary-value"]
<h1 arbitrary-key=arbitrary-value></h1>
```

Please remember to separate text values with non-space characters.  (Sorry!  This is a shortcoming in the code.) 

__Good__:

```
["@h1 $this-is-text"]
<h1>this-is-text</h1>
```

__Bad__:

```
["@h1 $this is text"]
<h1>this</h1>
```

## Describing the Hierarchical Relationships between HTML Elements

To describe the hierarchical relationships between HTML elements, we use nested lists.

```
["@html &lang=\"en\""]
<html lang="en"></html>

["@html &lang=\"en\"", ["@head"]]
<html lang="en"><head></head></html>

["@html &lang=\"en\"", ["@head", ["@meta charset=\"utf-8\""]]]
<html lang="en"><head><meta charset="utf-8"></head></html>

["@html &lang=\"en\"", ["@head", ["@meta charset=\"utf-8\""], ["@title $app"]]]
<html lang="en"><head><meta charset="utf-8"><title>app</title></head></html>

["@html &lang=\"en\"", ["@head", ["@meta charset=\"utf-8\""], ["@title $app"]], ["@body"]]
<html lang="en"><head><meta charset="utf-8"><title>app</title></head><body></body></html>
```

## Dependencies:

To use py-list-html-translator, we will need Python and pip.  To test it, we will need pytest pytest-cov.

## Installing py-list-html-translator with testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip with the install command and the --editable option.

```
sudo pip install --editable .[test] .
```

## Installing py-list-html-translator without testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip with the install command.

```
sudo pip install .
```

## Using py-list-html-translator

1. Import the Translator class from the list_html_translator module.
2. Create a list.
3. Instantiate Translator, passing in the list.
4. Call the translate method.
5. Do something fun with the HTML!

```
from list_html_translator import Translator
in_list = ["@html"]
translator = Translator(in_list)
out_html = translator.translate()
print(out_html)
```

## Testing py-list-html-translator after installation

1. Change to the tests directory.

```
cd ./tests
```

2. Run pytest with the -vv, --cov, and --cov-report options.

```
pytest -vv --cov=list_html_translator --cov-report=term-missing
```
