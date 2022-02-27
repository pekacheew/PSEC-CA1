def encrypt(string: str):

  alphabets = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
  splitStringLs = list(string)
  encryptedPswd = []

  for char in splitStringLs:
    if char.lower() in alphabets:
      index = splitStringLs.index(char)
      alphabetIndex = alphabets.index(char.lower())
      if char.islower():                                                # if character in userPassword is lower vvv
        encryptedPswd.append(alphabets[alphabetIndex - 4].lower())      # Move the lower alphabet letters with a key of 4 letters, right
        splitStringLs[index] = None
      if char.isupper():                                                # if character in userPassword is upper vvv
        encryptedPswd.append(alphabets[alphabetIndex - 4].upper())      # Move the upper alphabet letters with a key of 4 letters, right
        splitStringLs[index] = None
    else:                                                               # if character is numeral or special character, skip
      encryptedPswd.append(char)
  encryptedPswd = "".join(encryptedPswd)
  return encryptedPswd
