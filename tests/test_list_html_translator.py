from list_html_translator import Translator

from pytest import (
  mark,
  raises
)


class TestSuite(object):
  def test_element_name(self):
    in_list = ["@h1"]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1></h1>"
    
    assert actual_result == expected_result

  def test_element_id(self):
    in_list = ["@h1 #id"]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1 id=\"id\"></h1>"

    assert actual_result == expected_result

  def test_element_class(self):
    in_list = ["@h1 .class"]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1 class=\"class\"></h1>"

    assert actual_result == expected_result

  def test_element_attribute(self):
    in_list = ["@h1 &key=\"value\""]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1 key=\"value\"></h1>"

    assert actual_result == expected_result

  def test_element_attributes(self):
    in_list = ["@h1 &key0=\"value0\" &key1=\"value1\""]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1 key0=\"value0\" key1=\"value1\"></h1>"

    assert actual_result == expected_result

  def test_element_text(self):
    in_list = ["@h1 $text"]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1>text</h1>"
    
    assert actual_result == expected_result

  def test_all_element_components(self):
    in_list = ["@h1 #id .class &key0=\"value0\" &key1=\"value1\" $text"]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<h1 id=\"id\" class=\"class\" key0=\"value0\" key1=\"value1\">text</h1>"

    assert actual_result == expected_result

  @mark.parametrize("element", [
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "keygen",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr"
  ])
  def test_void_element(self, element):
    in_list = ["@{} &charset=\"utf-8\"".format(element)]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<{} charset=\"utf-8\">".format(element)

    assert actual_result == expected_result

  def test_two_nested_elements(self):
    in_list = ["@div", ["@h1 $text"]]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<div><h1>text</h1></div>"

    assert actual_result == expected_result

  def test_three_nested_elements(self):
    in_list = ["@body", ["@div", ["@h1 $text"]]]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<body><div><h1>text</h1></div></body>"

    assert actual_result == expected_result

  def test_four_nested_elements(self):
    in_list = ["@html", ["@body", ["@div", ["@h1 $text"]]]]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<html><body><div><h1>text</h1></div></body></html>"

    assert actual_result == expected_result

  @mark.parametrize("invalid_input", [
    None,
    [None]
  ])
  def test_error(self, invalid_input):
    with raises(RuntimeError) as exception:
      in_list = invalid_input
      translator = Translator(in_list)
      actual_result = translator.translate()

    assert "Error parsing list." in str(exception.value)
