import os
def styleStr(str_, style=None, rgb=None, rgbSgr=38):
  """returns a string with ANSI Select Graphic Rendition

  Args:
    str_ (string): string to be converted
    sgr (integer): 
      ANSI SGR Values (Select Graphic Rendition):
        0: Reset
        1: Bold
        3: Italic
        4: Underline
      
      Default Colors in Order:
        (black, red, green, yellow, blue, magenta, cyan, white)  
      30-37: Text Color
      40-47: Background Color
      90-97: Text Color Bright
      100-107: Background Color Bright

    rgb (string, optional): rgb value with format '[(r,g,b), sgr]'. Available sgr are 38, 48, 98 and 108.
                            Defaults to None.

  Returns:
    string: ansi formatted string
  
  """
  if os.name == 'nt': # To enable ANSI in windows
    os.system('')

  sequenceESC = ''
  rstSequence = '\033[0m'

  sgr = None
  if style == 'reset':
    sgr = 0
  elif style == 'bold':
    sgr = 1
  elif style == 'italic':
    sgr = 3
  elif style == 'under':
    sgr = 4
  if sgr:
    if isinstance(sgr, list):
      for element in sgr:
        sequenceESC += '\033[' + str(element) + 'm'

    else:
      sequenceESC = '\033[' + str(sgr) + 'm'
  if rgb:
    sequenceESC += '\033[' + str(rgbSgr) + ';2;'
    sequenceESC += f'{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m'
  return f'{sequenceESC}{str_}{rstSequence}'
