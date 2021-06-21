punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# Funtion to remove punctuation for the string.

def strip_punctuation(str1):
    word_no_punct = ''
    for w in str1:
        if w not in punctuation_chars:
            word_no_punct = word_no_punct + w
    return word_no_punct
    

# Function for count positive words.

def get_pos(sentence):
    low_sent =  sentence.lower()
    strip_sent = strip_punctuation(low_sent)
    spl_sent = strip_sent.split()
    
    
    count_pos = 0
    
    for w in spl_sent:
        if w in positive_words:
            count_pos = count_pos + 1
            
    return count_pos

# Function for count negative words.


def get_neg(sentence):
    low_sent = sentence.lower()
    strip_sent = strip_punctuation(low_sent)
    spl_sent = strip_sent.split()
    
    count_neg = 0
    
    for w in spl_sent:
        if w in negative_words:
            count_neg = count_neg + 1
            
    return count_neg

# open 'project_twitter_data.csv' file
with open("project_twitter_data.csv","r") as file_obj:
    file_cont = file_obj.readlines()


# write in 'resulting_data.csv' file

with open("resulting_data.csv","w") as file_obj2:
    file_obj2.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    file_obj2.write("\n")

    for line in file_cont[1:]:
        data_rows = ""
        spl_line = line.strip().split(",")           
        data_rows = ("{},{},{},{},{}".format(spl_line[1], spl_line[2], get_pos(spl_line[0]), get_neg(spl_line[0]), (get_pos(spl_line[0])-get_neg(spl_line[0]))))
        file_obj2.write(data_rows)
        file_obj2.write("\n")
        
    file_obj2.close()





