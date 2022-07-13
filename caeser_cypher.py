# A python program to demonstrate Ceasar Cipher Technique
def encrypt(text, s): # a function that takes a string and the shift value
    result = "" # result is currently blank when the variable is created

    # traverse text
    # for the i in the range in the length of the text...
    for i in range(len(text)):
        char = text[i] # the i in the text will be passed to the char variable

        # Encrypt uppercase characters
        if (char.isupper()): # if the character (char) is uppercase...
            # the character is converted to its unicode value, ord returns an integer representing the Unicode character...
            # the character is concatinated? to s subtracted from 65 then moduloed by 26 and added to 65 and passed...
            # to the result variable
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else: # otherwise if characters are lowercase
            # the character is converted to its unicode value, ord returns an integer representing the Unicode character...
            # the character is concatinated? to s subtracted from 97 then moduloed by 26 and added to 97 and passed...
            # to the result variable
            result += chr((ord(char) + s - 97) % 26 + 97)
    # return the result which is now filled in by the math logic of the caeser cypher
    return result

# pass a string to text variable which will be a parameter in the encrypt function
text = "ATTACKATDAWN"
# the caeser cypher shift is set to 4
s = 4
# print the text passed to the function
print ("Text    : " + text)
# print the shift as a string that s variable is set to
print ("Shift   : " + str(s))
# print the output of the cypher after passing text string and shift to the encrypt function
print ("Cipher: " + encrypt(text,s))

# ABCDEFGHIJKLMNOPQRSTUVWXYZ