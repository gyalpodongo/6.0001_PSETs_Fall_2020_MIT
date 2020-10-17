# 6.0001 Spring 2020
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Gyalpo Dongo
# Collaborators: Paterne Byiringiro
# Time Spent: 4:00
# Late Days Used: (only if you are using any)

import string

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other


### Problem 1: Prep Data ###
# Make a *small* change to separate the data by whitespace rather than just tabs
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        list of strings holding the file contents where
            each string was separated by an empty space in the file
    """
    inFile = open(filename, 'r')
    line = inFile.read()
    inFile.close()
    line = line.strip().lower()
    for char in string.punctuation:
        line = line.replace(char, "")
        #Change from "/t" to ""  
    return line.split()

### Problem 2: Find Ngrams ###
def find_ngrams(single_words, n):
    """
    Args:
        single_words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters
        n:            length of 'n-gram' window
    Returns:
        list of n-grams from input text list, or an empty list if n is not a valid value
    """
    ngrams = []
    if n <= 0 or n > len(single_words):
        return ngrams
        #returns empty list
    elif n == 1:
        return single_words
        #returns original input
    else:
        for i in range(len(single_words)):
            if n + i > len(single_words):
                break
                #done so that the very last word of the n-gram is the
                #very last word of the list single_words
            else:
                mini_list = single_words[i:n+i]
                #creates a list with the words in the ngram
                #the list contains the words between index i and n+i so that 
                #the maximum possible value of n+i is the length of single_words
                ngrams_word = ' '.join([str(item) for item in mini_list])
                #the list is transformed into a string with spaces in between
                #and no spaces at the beginning or end
                ngrams.append(ngrams_word)
                #the n-gram string is added to the list
        return ngrams
        
        

### Problem 3: Word Frequency ###
def compute_frequencies(words):
    """
    Args:
        words: list of words (or n-grams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word (or n-gram) in words and the corresponding int
        is the frequency of the word (or n-gram) in words
    """
    frequency_dict = {}
    for i in words:
        if i in frequency_dict:
            frequency_dict[i] +=1
            #if the word/n-gram is already in the dictionnary, its frequency
            #keeps on increasing by one every time it appears in the list
            #of words/n-grams
        else:
            frequency_dict[i] = 1
            #if the word isn't in the dictionnary, its frequency is then set 
            #to one and if it appears again then it will go through the
            #previous conditional
    return frequency_dict

### Problem 4: Similarity ###
def get_similarity_score(dict1, dict2, dissimilarity = False):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of words or n-grams for one text
        dict2: frequency dictionary of words or n-grams for another text
        dissimilarity: Boolean, optional parameter. Default to False.
          If this is True, return the dissimilarity score, 100*(DIFF/ALL), instead.
    Returns:
        int, a percentage between 0 and 100, inclusive
        representing how similar the texts are to each other

        The difference in text frequencies = DIFF sums words
        from these three scenarios:
        * If a word or n-gram occurs in dict1 and dict2 then
          get the difference in frequencies
        * If a word or n-gram occurs only in dict1 then take the
          frequency from dict1
        * If a word or n-gram occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 100*(1-(DIFF/ALL)) rounded to the nearest whole number if dissimilarity
          is False, otherwise returns 100*(DIFF/ALL)
    """
    DIFF = 0
    for i in dict1:
        x = False
        #Boolean used to not add repeated frequencies as it will be seen later
        for j in dict2:
            if i == j:
                #use of == instead of i in j as for example word "meme" could
                #be in "memes" and would therefore cause a problem
                DIFF += abs(dict1[i] - dict2[j])
                #if the word/n-gram appears in both dictionnaires then
                #the absolute value of the difference between the frequencies 
                #in each dictionnary is added to DIFF
                x = True
        if x == False:
            #Boolean used so that frequencies of a word/n-gram are not added again
            #and again to DIFF
            DIFF += dict1[i]   
    for j in dict2:
        x = False
        #same use of boolean for same reasons as previou for loop
        for i in dict1:
            if i == j:
                #use of == due to the same reason
                x = True
                #this time the absolute value of the difference between the
                #frequencies doesn't have to be added as it already has been
        if x == False:
            DIFF += dict2[j]
    ALL = 0
    for i in dict1:
        ALL += dict1[i]
        #all the  frequencies of the first dictionnary are added to ALL
    for j in dict2:
        ALL += dict2[j]
        #same occurs as in the previous loop but for the second dictionnary
        
    #Depending on the input of dissimilarity this will occur
    if dissimilarity == False:
        result = round(100*(1 - (DIFF/ALL)))
        #similarity between the dictionnaries of word/n-grams is the result
    else:
        result = round(100*(DIFF/ALL))
        #dissimilarity between the dictionnaries of word/n-grams is the result
    return result
        
        
    
### Problem 5: Most Frequent Word(s) ###
def compute_most_frequent(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    list_freq = []
    most_freq = []
    #different frequencies of each word/n-gram in the dictionnaries will be
    #appended to list_freq in the following 2 for loops
    for i in dict1:
        list_freq.append(dict1[i])
    for i in dict2:
        list_freq.append(dict2[i])
    #Using the maximum value of list_freq, if this maximum value is the 
    #value of any of the words/n-grams in the dictionnaries, these words
    #will be added to the list most_freq
    for i in dict1:
        if dict1[i] == max(list_freq):
            most_freq.append(i)
    for i in dict2:
        if dict2[i] == max(list_freq):
            most_freq.append(i)
    return sorted(most_freq)
    #use of sorted() as specification establises that the list has to be
    #alphabetically ordered

### Problem 6: Finding closest artist ###
def find_closest_artist(artist_to_songfiles, mystery_lyrics, ngrams = 1):
    """
    Args:
        artist_to_songfiles:
            dictionary that maps string:list of strings
            where each string key is an artist name
            and the corresponding list is a list of filenames (including the extension),
            each holding lyrics to a song by that artist
        mystery_lyrics: list of single word strings
            Can be more than one or two words (can also be an empty list)
            assume each string is made of lowercase characters
        ngrams: int, optional parameter. Default set to False.
            If it is greater than 1, n-grams of text in files
            and n-grams of mystery_lyrics should be used in analysis, with n
            set to the value of the parameter ngrams
    Returns:
        list of artists (in alphabetical order) that best match the mystery lyrics
        (i.e. list of artists that share the highest average similarity score (to the nearest whole number))

    The best match is defined as the artist(s) whose songs have the highest average
    similarity score (after rounding) with the mystery lyrics
    If there is only one such artist, then this function should return a singleton list
    containing only that artist.
    However, if all artists have an average similarity score of zero with respect to the
    mystery_lyrics, then this function should return an empty list. When no artists
    are included in the artist_to_songfiles, this function returns an empty list.
    """
    if len(artist_to_songfiles) == 0:
        #if the dictionnary artist_to_songfiles is empty, an empty list is
        #returned 
        return []
    
    else:
        #artist_score is an empty dictionnary where each artist will be linked
        #to the average mean similarity of mystery_lyrics with all of the
        #artist songs
        artist_score = {}
        #the list of the scores will be the previous average mentioned
        list_scores = []
        #the closest artist will be a list of the artist/s with the maximum
        #similarity as long as it is greater than 0, otherwise the list will
        #be empty
        closest_artist = []
        for artist in artist_to_songfiles:
            sum_scores = 0
            #variable created so that the total sum of the similarity scores
            #can be added and then the average can be taken
            for song in artist_to_songfiles[artist]:
                if ngrams > 1:
                    #if value of n-grams is an integer and greater than one
                    #then ngrams will be used for the similarity comparation
                    #instead of single words
                    dict_mystery = compute_frequencies(find_ngrams(mystery_lyrics,ngrams))
                    #firstly the find_grams functions converts mystery_lyrics()
                    #into a list of n-grams and then compute_frequencies()
                    #converts it into a dictionnary with the respective
                    #frequencies
                    dict_songs = compute_frequencies(find_ngrams(load_file(song),ngrams))
                    #same as in previous case but also load_file() is used
                    #initially to convert the song into a list of single words
                else:
                    dict_mystery = compute_frequencies(mystery_lyrics)
                    dict_songs = compute_frequencies(load_file(song))
                    #in both cases, once both of mystery_lyrics and song
                    #are a list of single words, a dictionnary with the
                    #respective frequency of each word is created
                sum_scores += get_similarity_score(dict_mystery,dict_songs)
                #this is used to keep on adding each similarity score from each
                #song with the respective mystery_lyrics
            average_score = round(sum_scores/len(artist_to_songfiles[artist]))
            #aveareg obtained by dividing sum_scores by the number of songs
            #of the artist
            artist_score[artist] = average_score
            #artist and average_score are added to the artist_score dictionnary
            list_scores.append(average_score)
            #the average_score is also added to this list_scores
        for artist in artist_score:
            if max(list_scores) > 0: #otherwise an empty list of closest_artist
                #will be returned
                if artist_score[artist] == max(list_scores):
                    closest_artist.append(artist)
        return sorted(closest_artist)
        #use of sorted() as specification established that list had to be
        #alphabetically in order
    
        
            
            
                
            
        
            


if __name__ == "__main__":
    pass
    ##Uncomment the following lines to test your implementation
    ## Tests Problem 0: Prep Data
    #test_directory = "tests/student_tests/"
    #world, friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    #print(world) ## should print ['hello', 'world', 'hello']
    #print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 1: Find Ngrams
    #world_ngrams, friend_ngrams = find_ngrams(world, 2), find_ngrams(friend, 2)
    #longer_ngrams = find_ngrams(world+world, 3)
    #print(world_ngrams) ## should print ['hello world', 'world hello']
    #print(friend_ngrams) ## should print ['hello friends']
    #print(longer_ngrams) ## should print ['hello world hello', 'world hello hello', 'hello hello world', 'hello world hello']

    ## Tests Problem 2: Get frequency
    #world_word_freq, world_ngram_freq = compute_frequencies(world), compute_frequencies(world_ngrams)
    #friend_word_freq, friend_ngram_freq = compute_frequencies(friend), compute_frequencies(friend_ngrams)
    #print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    #(world_ngram_freq) ## should print {'hello world': 1, 'world hello': 1}
    #print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    #print(friend_ngram_freq) ## should print {'hello friends': 1}

    ## Tests Problem 3: Similarity
    #word_similarity = get_similarity_score(world_word_freq, friend_word_freq)
    #ngram_similarity = get_similarity_score(world_ngram_freq, friend_ngram_freq)
    #print(word_similarity) ## should print 40
    #print(ngram_similarity) ## should print 0

    ## Tests Problem 4: Most Frequent Word(s)
    #freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    #most_frequent = compute_most_frequent(freq1, freq2)
    #print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Find closest matching artist
    #test_directory = "tests/student_tests/"
    #artist_to_songfiles_map = {
    #"artist_1": [test_directory + "artist_1/song_1.txt", test_directory + "artist_1/song_2.txt", test_directory + "artist_1/song_3.txt"],
    #"artist_2": [test_directory + "artist_2/song_1.txt", test_directory + "artist_2/song_2.txt", test_directory + "artist_2/song_3.txt"],
    #}
    #mystery_lyrics = load_file(test_directory + "mystery_lyrics/mystery_5.txt") # change which number mystery lyrics (1-5)
    
    #print(find_closest_artist(artist_to_songfiles_map, mystery_lyrics, ngrams = 1)) # should print ['artist_1']
    