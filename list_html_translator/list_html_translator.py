"""The Translator class converts a list to HTML."""


class Translator(object):
  """The Translator class converts a list to HTML.

     Parameters
     ----------
     input_list : list
       The list to translate.

     Returns
     -------
     self.html_element : str
       The HTML translation. 
  """
  
  def __init__(self, input_list):
    """Instantiate Translator."""
    
    self.list = input_list

    self.void_elements = [
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
    ] 

    self.html_element_name = {
      "delimiter": "@", 
      "key": None, 
      "value": ""
    }

    self.html_element_id = {
      "delimiter": "#", 
      "key": "id", 
      "value": ""
    }

    self.html_element_class = {
      "delimiter": ".", 
      "key": "class", 
      "value": ""
    }

    self.html_element_attributes = {
      "delimiter": "&", 
      "pairs": []
    }

    self.html_element_text = {
      "delimiter": "$", 
      "key": None, 
      "value": ""
    }

    self.branch_html_elements = []

    self.html_element_start_tag = ""

    self.html_element_end_tag = ""

    self.html_element = ""

  def _parse_list(self):
    """Parse an input list.

       Do not call this method directly.
    """
    
    try:
  
      for index in range(0, len(self.list)):
        item = self.list[index]

        if isinstance(item, list):
          translator = Translator(item)
          branch_html = translator.translate()
          self.branch_html_elements.append(branch_html)

        else:
          item = item.split(" ")
    
          for index in range(0, len(item)):
            component = item[index]
 
            if component.startswith(self.html_element_name["delimiter"]):
              html_element_name = component.strip(self.html_element_name["delimiter"])
              self.html_element_name["value"] = html_element_name
    
            if component.startswith(self.html_element_id["delimiter"]):
              html_element_id = component.strip(self.html_element_id["delimiter"])
              self.html_element_id["value"] = html_element_id

            if component.startswith(self.html_element_class["delimiter"]):
              html_element_class = component.strip(self.html_element_class["delimiter"])
              self.html_element_class["value"] = html_element_class

            if component.startswith(self.html_element_attributes["delimiter"]):
              html_element_attribute = component.strip(self.html_element_attributes["delimiter"])
              self.html_element_attributes["pairs"].append(html_element_attribute)

            if component.startswith(self.html_element_text["delimiter"]):
              html_element_text = component.strip(self.html_element_text["delimiter"])
              self.html_element_text["value"] = html_element_text

    except:
      raise RuntimeError("Error parsing list.")

  def _get_html_element_start_tag(self):
    """Get an HTML element's start tag.

       Do not call this method directly.
    """
  
    html_element_start_tag = "<"
    
    if self.html_element_name["value"]:
      html_element_name = self.html_element_name["value"]
      html_element_start_tag += html_element_name + " "
    
    if self.html_element_id["value"]:
      html_element_id = self.html_element_id["key"] + "=" + "\"" + self.html_element_id["value"] + "\""
      html_element_start_tag += html_element_id + " "

    if self.html_element_class["value"]:
      html_element_class = self.html_element_class["key"] + "=" + "\"" + self.html_element_class["value"] + "\""
      html_element_start_tag += html_element_class + " "
 
    if self.html_element_attributes["pairs"]:
      html_element_attributes = ""
    
      for attribute in self.html_element_attributes["pairs"]:
        html_element_attributes += attribute + " "
    
      html_element_start_tag += html_element_attributes
    
    html_element_start_tag = html_element_start_tag.strip()
    
    html_element_start_tag += ">"
    
    self.html_element_start_tag = html_element_start_tag

  def _get_html_element_end_tag(self):
    """Get an HTML element's end tag.

       Do not call this method directly.
    """

    if self.html_element_name["value"] not in self.void_elements:
      
      html_element_end_tag = "</"
    
      if self.html_element_name["value"]:
        html_element_name = self.html_element_name["value"]
        html_element_end_tag += html_element_name
    
      html_element_end_tag += ">"

      self.html_element_end_tag = html_element_end_tag

  def _get_html_element(self):
    """Get a full HTML element, including start and end tags.

       Do not call this method directly.
    """

    html_element = ""
    
    html_element += self.html_element_start_tag
    
    if self.html_element_text["value"]:
      html_element_text = self.html_element_text["value"]
      html_element += html_element_text
 
    if self.branch_html_elements:
      for index in range(0, len(self.branch_html_elements)):
        branch_html_element = self.branch_html_elements[index]
        html_element += branch_html_element
    
    html_element += self.html_element_end_tag
    
    self.html_element = html_element

  def translate(self):
    """Convert an input list to HTML.

       Call this method directly.
    """
  
    self._parse_list()
    self._get_html_element_start_tag()
    self._get_html_element_end_tag()
    self._get_html_element()
    
    return self.html_element
