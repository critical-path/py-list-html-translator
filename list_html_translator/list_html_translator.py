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

  def __parse_list__(self):
    """Parse an input list.

       Do not call this method directly.
    """
    
    try:
  
      # Loop over each item in the list.
  
      for index in range(0, len(self.list)):
        item = self.list[index]

      # If the item is of type list, then pass it in to a 
      # new instance of Translator, recursively converting it 
      # to HTML.
    
        if isinstance(item, list):
          translator = Translator(item)
          branch_html = translator.translate()
          self.branch_html_elements.append(branch_html)

      # If the item is of type str, then begin to parse it.
    
        else:
          item = item.split(" ")
    
      # Split the str into a list, and loop over each item.
      
          for index in range(0, len(item)):
            component = item[index]
 
      # First, try to find the name of the HTML element.
          
            if component.startswith(self.html_element_name["delimiter"]):
              html_element_name = component.strip(self.html_element_name["delimiter"])
              self.html_element_name["value"] = html_element_name
    
      # Second, try to find its id.
    
            elif component.startswith(self.html_element_id["delimiter"]):
              html_element_id = component.strip(self.html_element_id["delimiter"])
              self.html_element_id["value"] = html_element_id

      # Third, try to find its class.
    
            elif component.startswith(self.html_element_class["delimiter"]):
              html_element_class = component.strip(self.html_element_class["delimiter"])
              self.html_element_class["value"] = html_element_class

      # Fourth, try to find any other of its attributes.

            elif component.startswith(self.html_element_attributes["delimiter"]):
              html_element_attribute = component.strip(self.html_element_attributes["delimiter"])
              self.html_element_attributes["pairs"].append(html_element_attribute)

      # Last, try to find its text content.

            elif component.startswith(self.html_element_text["delimiter"]):
              html_element_text = component.strip(self.html_element_text["delimiter"])
              self.html_element_text["value"] = html_element_text

    except:
      raise RuntimeError("Error parsing list.")

  def __get_html_element_start_tag__(self):
    """Get an HTML element's start tag.

       Do not call this method directly.
    """
  
    # First, open the HTML element's tag.
 
    html_element_start_tag = "<"
    
    # Second, try to add the name of the element.
    
    if self.html_element_name["value"]:
      html_element_name = self.html_element_name["value"]
      html_element_start_tag += html_element_name + " "
    
    # Third, try to add its id and enclose it in quotation marks.
    
    if self.html_element_id["value"]:
      html_element_id = self.html_element_id["key"] + "=" + "\"" + self.html_element_id["value"] + "\""
      html_element_start_tag += html_element_id + " "

    # Fourth, try to add its class and enclose it in quotation marks.
    
    if self.html_element_class["value"]:
      html_element_class = self.html_element_class["key"] + "=" + "\"" + self.html_element_class["value"] + "\""
      html_element_start_tag += html_element_class + " "
 
    # Fifth, try to add any other of its attributes, 
    # assuming that the user enclosed them in quotation marks.
    
    if self.html_element_attributes["pairs"]:
      html_element_attributes = ""
    
      for attribute in self.html_element_attributes["pairs"]:
        html_element_attributes += attribute + " "
    
      html_element_start_tag += html_element_attributes
    
    # Sixth, remove any trailing space characters.
    
    html_element_start_tag = html_element_start_tag.strip()
    
    # Last, close the tag.
    
    html_element_start_tag += ">"
    
    self.html_element_start_tag = html_element_start_tag

  def __get_html_element_end_tag__(self):
    """Get an HTML element's end tag.

       Do not call this method directly.
    """

    # First, determine whether the HTML element requires an end tag.
    # If not, then pass.  If yes, then proceed.
  
    if self.html_element_name["value"] in self.void_elements:
      pass
  
    else:
    
    # Second, open the tag.
    
      html_element_end_tag = "</"
    
    # Third, try to add the name of the element.
        
      if self.html_element_name["value"]:
        html_element_name = self.html_element_name["value"]
        html_element_end_tag += html_element_name
    
    # Fourth, close the tag.
    
      html_element_end_tag += ">"

      self.html_element_end_tag = html_element_end_tag

  def __get_html_element__(self):
    """Get a full HTML element, including start and end tags.

       Do not call this method directly.
    """

    html_element = ""
    
    # First, add the HTML element's start tag.
    
    html_element += self.html_element_start_tag
    
    # Second, try to add its text content.
    
    if self.html_element_text["value"]:
      html_element_text = self.html_element_text["value"]
      html_element += html_element_text
 
    # Third, try to add the HTML of any branches.
    
    if self.branch_html_elements:
      for index in range(0, len(self.branch_html_elements)):
        branch_html_element = self.branch_html_elements[index]
        html_element += branch_html_element
    
    # Last, close the tag.
    
    html_element += self.html_element_end_tag
    
    self.html_element = html_element

  def translate(self):
    """Convert an input list to HTML.

       Call this method directly.
    """
  
    self.__parse_list__()
    self.__get_html_element_start_tag__()
    self.__get_html_element_end_tag__()
    self.__get_html_element__()
    
    return self.html_element
