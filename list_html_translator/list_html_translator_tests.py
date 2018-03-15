from list_html_translator import Translator

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

  def test_void_element(self):
    in_list = ["@meta &charset=\"utf-8\""]
    translator = Translator(in_list)
    actual_result = translator.translate()
    expected_result = "<meta charset=\"utf-8\">"

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
