# Problem Set 4B
# Name: Gyalpo Dongo
# Collaborators:
# Time Spent: 9:00
# Late Days Used: 1

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_digit_shift(input_shift, decrypt):
    '''
    calculate the digit shift based on if decrypting or not
    decrypt: boolean, if decrypting or not
    Returns: digit_shift, the digit shift based on if decrypting or not
    '''
    if decrypt:
        digit_shift = 10 - (26-input_shift)%10
    else:
        digit_shift = input_shift
    return digit_shift

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = input_text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def make_shift_dict(self, input_shift, decrypt=False):#THINK NEG NUMBERS
        '''
        Creates a dictionary that can be used to apply a cipher to a letter and number.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift, as well as
        every number to one shifted down by the same amount. If 'a' is
        shifted down by 2, the result is 'c' and '0' shifted down by 2 is '2'.

        The dictionary should contain 62 keys of all the uppercase letters,
        all the lowercase letters, and all numbers mapped to their shifted values.

        input_shift: the amount by which to shift every letter of the
        alphabet and every number (0 <= shift < 26)

        decrypt: if the shift dict will be used for decrypting. affects digit shift function

        Returns: a dictionary mapping letter/number (string) to
                 another letter/number (string).
        '''
        dig_shift = get_digit_shift(input_shift,decrypt)
        #gets the new value for the shift in the digits
        dict_shift = {}

        for i in range(len(string.ascii_lowercase)):
            if input_shift > 25:
                new_input_shift = input_shift - 26
            else:
                new_input_shift = input_shift
            if (i+new_input_shift) > 25:
                t = (i+new_input_shift) - 26
                dict_shift[string.ascii_lowercase[i]] = string.ascii_lowercase[t]
            else:
                dict_shift[string.ascii_lowercase[i]] = string.ascii_lowercase[i+new_input_shift]
        for i in range(len(string.ascii_uppercase)):
            if input_shift > 25:
                new_input_shift = input_shift - 26
            else:
                new_input_shift = input_shift
            if (i+new_input_shift) > 25:
                t = (i+new_input_shift) - 26
                dict_shift[string.ascii_uppercase[i]] = string.ascii_uppercase[t]
            else:
                dict_shift[string.ascii_uppercase[i]] = string.ascii_uppercase[i+new_input_shift]
        for i in range(len(string.digits)):
            if dig_shift > 19:
                new_dig_shift = dig_shift - 20
            elif dig_shift > 9:
                new_dig_shift = dig_shift - 10
            else:
                new_dig_shift = dig_shift
                
            if (i+new_dig_shift) > 9:
                t = (i+new_dig_shift) - 10
                dict_shift[string.digits[i]] = string.digits[t]
            else:
                dict_shift[string.digits[i]] = string.digits[i+new_dig_shift]
        return dict_shift
    
        
            

    def apply_shift(self, shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with the shift
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down by some number of characters, determined by the shift
        value that shift_dict was built with.

        shift_dict: a dictionary with 62 keys, mapping
            lowercase and uppercase letters and numbers to their new letters
            (as built by make_shift_dict)

        Returns: the message text (string) with every letter/number shifted using
            the input shift_dict

        '''
        new_str = ""
        for i in self.get_message_text():
            if str(i) in shift_dict:
                #if str(i) is any of the keys in the dictionnary, then 
                #it shifted value will be added to new_str
                new_str += shift_dict[str(i)]
            else:
                new_str += str(i)
                #this is for when it is either punctuations or other symbols
                #or spacesso that they are not modified as problem specified
        return new_str

class PlaintextMessage(Message):
    def __init__(self, input_text, input_shift):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shift: the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using the shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self,input_text)
        self.shift = input_shift
        self.encryption_dict = self.make_shift_dict(self.shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy of self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text

    def modify_shift(self, input_shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by the shift.

        input_shift: an integer, the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        self.__init__(self.message_text,input_shift)
        self.shift = input_shift


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,input_text)

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value and
        finding the "best" one.

        We will define "best" as the shift that creates the max number of
        valid English words when we use apply_shift(shift) on the message text.
        If a is the original shift value used to encrypt the message, then
        we would expect (26 - a) to be the  value found for decrypting it.

        Note: if shifts are equally good, such that they all create the
        max number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to originally encrypt
        the message (a) and the decrypted message text using that shift value
        '''
        input_scores = {}
        #this will be a dictionnary with the different shifts as the keys
        #and the values of these keys will be a tupple of the respective
        #amount (score) of valid words found after applying this shift and the text
        #with this applied shift
        list_scores = []
        list_tuples = []
        #use of  list for the tuples of best_shift and text as there can be
        #many of these
        for i in range(26):
            #use of range 26 as that is the max
            t = 0
            #use of t as a counter for the amount of valid words in the
            #decrypted text
            shift_dict = self.make_shift_dict(26 - i, True).copy()
            shift_text = self.apply_shift(shift_dict)
            valid_words_list = self.valid_words.copy()
            for b in valid_words_list:
                if b in shift_text.lower():
                    t += 1
            input_scores[i] = (t,shift_text)
            list_scores.append(t)
        for i in input_scores:
            if input_scores[i][0] == max(list_scores):
                list_tuples.append((i,input_scores[i][1]))
        import random
        if len(list_tuples) > 0:
            return random.choice(list_tuples)
        else:
            return list_tuples[0]
        #return the 0 index because it is the only value, and if
        # all of them have the same score, as problem stated, any can be
        #can be returneed so use of random module to choose
            


def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''


    #Testing for numbers
    plaintext1 = PlaintextMessage("231.45", 2)
    print('Expected Output: 453.67')
    print('Actual Output:', plaintext1.get_encrypted_message_text())
    
    
    #Testing for Capitals and numbers
    plaintext1 = PlaintextMessage("HeLLo 23.21", 3)
    print('Expected Output: KhOOr 56.54')
    print('Actual Output:', plaintext1.get_encrypted_message_text())

#    #### Example test case (PlaintextMessage) #####

#    #This test is checking encoding a lowercase string with punctuation in it.
#    plaintext = PlaintextMessage('hello!', 2)
#    print('Expected Output: jgnnq!')
#    print('Actual Output:', plaintext.get_encrypted_message_text())



def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (EncryptedMessage) #####

#   # This test is checking decoding a lowercase string with punctuation in it.
#    encrypted = EncryptedMessage('jgnnq!')
#    print('Expected Output:', (2, 'hello!'))
#    print('Actual Output:', encrypted.decrypt_message())
    
    #Testing for Capital Letters and lowercase
    encrypted1 = EncryptedMessage('EQORwVGT')
    print('Expected Output:', (2, 'COMPuTER'))
    print('Actual Output:', encrypted1.decrypt_message()) 
    
    #Testing for Capitals,letters,punctuation and numbers
    encrypted2 = EncryptedMessage('Jgnnq42!')
    print('Expected Output:', (2, 'Hello21!'))
    print('Actual Output:', encrypted2.decrypt_message()) 

def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    encrypted = EncryptedMessage(get_story_string())
    return encrypted.decrypt_message()

if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    test_plaintext_message()
    test_encrypted_message()

    # Uncomment these lines to try running decode_story_string()
    best_shift, story = decode_story()
    print("Best shift:", best_shift)
    print("Decoded story: ", story)
