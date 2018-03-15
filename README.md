## py-list-html-translator v1.0.0

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

To use py-list-html-translator, we will need Python 3.x and pip (https://www.python.org).  To test it, we will need pytest (https://pytest.org).


## Installing py-list-html-translator

1. Download this repository.
2. Extract its contents.
3. Run python3 setup.py build sdist.

```
python3 setup.py build sdist
```

4. Change to the dist directory.

```
cd ./dist
```

5. Run pip3 install py-list-html-translator-1.0.0.tar.gz.

```
pip3 install py-list-html-translator-1.0.0.tar.gz
```

If we encounter any errors during installation, then we will try again, this time prefacing our commands with "sudo."

```
sudo python3 setup.py build sdist
cd ./dist
sudo pip3 install py-list-html-translator-1.0.0.tar.gz
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

## Testing py-list-html-translator

1. Locate the directory in which the list_html_translator module is located.
2. Change to that directory.

```
cd /path/to/list_html_translator/
```

3. Run pytest list_html_translator_tests.py.

```
pytest list_html_translator_tests.py
```

These test cases are not exhaustive.  They are meant to provide a basic level of confidence in py-list-html-translator.

