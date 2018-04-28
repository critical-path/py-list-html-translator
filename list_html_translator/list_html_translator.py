class Translator(object):
  def __init__(self, list):
    """ requires list as argument """
    
    self.list = list
    self.branch_html_elements = []
    self.void_elements = ["area", "base", "br", "col", "embed",
                          "hr", "img", "input", "keygen", "link", 
                          "meta", "param", "source", "track", "wbr"] 
    self.html_element_name = {"delimiter": "@", "key": None, "value": ""}
    self.html_element_id = {"delimiter": "#", "key": "id", "value": ""}
    self.html_element_class = {"delimiter": ".", "key": "class", "value": ""}
    self.html_element_attributes = {"delimiter": "&", "pairs": []}
    self.html_element_text = {"delimiter": "$", "key": None, "value": ""}
    self.html_element_start_tag = ""
    self.html_element_end_tag = ""
    self.html_element = ""

  def __parse_list__(self):
    """ parses list (do not call directly) """
    
    try:
  
      # loop over each item in the list.
  
      for index in range(0, len(self.list)):
        item = self.list[index]

      # if the item is of type list, 
      # pass it in to a new instance of Translator,
      # recursively coverting it to html.
    
        if isinstance(item, list):
          translator = Translator(item)
          branch_html = translator.translate()
          self.branch_html_elements.append(branch_html)

      # if the item is of type string, then is ready to be parsed.
    
        else:
          item = item.split(" ")
    
      # split the string into a list, and loop over each item.
      
          for index in range(0, len(item)):
            component = item[index]
 
      # first, try to find the name of the html element.
          
            if component.startswith(self.html_element_name["delimiter"]):
              html_element_name = component.strip(self.html_element_name["delimiter"])
              self.html_element_name["value"] = html_element_name
    
      # second, try to find its id.
    
            elif component.startswith(self.html_element_id["delimiter"]):
              html_element_id = component.strip(self.html_element_id["delimiter"])
              self.html_element_id["value"] = html_element_id

      # third, try to find its class.
    
            elif component.startswith(self.html_element_class["delimiter"]):
              html_element_class = component.strip(self.html_element_class["delimiter"])
              self.html_element_class["value"] = html_element_class

      # fourth, try to find any other of its attributes.

            elif component.startswith(self.html_element_attributes["delimiter"]):
              html_element_attribute = component.strip(self.html_element_attributes["delimiter"])
              self.html_element_attributes["pairs"].append(html_element_attribute)

      # last, try to find its text content.

            elif component.startswith(self.html_element_text["delimiter"]):
              html_element_text = component.strip(self.html_element_text["delimiter"])
              self.html_element_text["value"] = html_element_text

    except:
      raise RuntimeError("error parsing array!")

  def __get_html_element_start_tag__(self):
    """ gets start tag of html element (do not call directly) """
  
    try:
  
      # create the start tag of the html element.
        
      # first, open the tag.
 
      html_element_start_tag = "<"
    
      # second, try to add the name of the element.
    
      if self.html_element_name["value"]:
        html_element_name = self.html_element_name["value"]
        html_element_start_tag += html_element_name + " "
    
      # third, try to add its id and enclose it in quotation marks.
    
      if self.html_element_id["value"]:
        html_element_id = self.html_element_id["key"] + "=" + "\"" + self.html_element_id["value"] + "\""
        html_element_start_tag += html_element_id + " "

      # fourth, try to add its class and enclose it in quotation marks.
    
      if self.html_element_class["value"]:
        html_element_class = self.html_element_class["key"] + "=" + "\"" + self.html_element_class["value"] + "\""
        html_element_start_tag += html_element_class + " "
 
      # fifth, try to add any other of its attributes, assuming that the
      # user enclosed them in quotation marks.
    
      if self.html_element_attributes["pairs"]:
        html_element_attributes = ""
    
        for attribute in self.html_element_attributes["pairs"]:
          html_element_attributes += attribute + " "
    
        html_element_start_tag += html_element_attributes
    
      # sixth, remove any trailing space characters.
    
      html_element_start_tag = html_element_start_tag.strip()
    
      # last, close the tag.
    
      html_element_start_tag += ">"
    
      self.html_element_start_tag = html_element_start_tag

    except:
      raise RuntimeError("error getting html element's opening tag!")

  def __get_html_element_end_tag__(self):
    """ gets end tag of html element (do not call directly) """

    try:
      
      # create the end tag of html element.
    
      # first, determine whether it requires an end tag.
      # if not, then pass.  if yes, then proceed.
  
      if self.html_element_name["value"] in self.void_elements:
        pass
  
      else:
    
      # second, open the tag.
    
        html_element_end_tag = "</"
    
      # third, try to add the name of the element.
        
        if self.html_element_name["value"]:
          html_element_name = self.html_element_name["value"]
          html_element_end_tag += html_element_name
    
      # fourth, close the tag.
    
        html_element_end_tag += ">"

        self.html_element_end_tag = html_element_end_tag

    except:
      raise RuntimeError("error getting html element's closing tag!")

  def __get_html_element__(self):
    """ gets full html element (do not call directly) """

    try:
  
      # create the full html element.
  
      html_element = ""
    
      # first, add the start tag.
    
      html_element += self.html_element_start_tag
    
      # second, try to add its text content.
    
      if self.html_element_text["value"]:
        html_element_text = self.html_element_text["value"]
        html_element += html_element_text
 
      # third, try to add the html of any branches.
    
      if self.branch_html_elements:
        for index in range(0, len(self.branch_html_elements)):
          branch_html_element = self.branch_html_elements[index]
          html_element += branch_html_element
    
      # last, close the tag.
    
      html_element += self.html_element_end_tag
    
      self.html_element = html_element

    except:
      raise RuntimeError("error getting full html element!")

  def translate(self):
    """ translates list to html (call directly) """
  
    self.__parse_list__()
    self.__get_html_element_start_tag__()
    self.__get_html_element_end_tag__()
    self.__get_html_element__()
    
    html = self.html_element
    
    return html
