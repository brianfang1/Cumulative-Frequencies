## Brian Fang, brian.fang@csu.fullerton.edu
## Edward Le, edwardl@csu.fullerton.edu
## Ashu Singh, ashusingh28@csu.fullerton.edu
## CPSC 535
## May 12, 2021

## Example 1 ##
WF = [['foot', 5], ['feet', 12], ['day', 3], ['days', 8], ['fear', 2], ['scared', 1],
 ['long', 12], ['large', 5], ['big',5], ['was', 4], ['is', 4], ['are', 15]]

SYN = [['foot', 'feet'], ['day','days'], ['fear', 'scared'], ['long' ,'big'], ['big' , 'large'], ['is', 'are'], ['is', 'was']]
##

## Example 2 ##
# WF = [['tons of', 2], ['large number of ', 12], ['mystical', 13], ['magical', 28], ['magic', 5], 
#  ['unexplained', 11], ['huge', 2], ['large', 51], ['horses', 25], ['horse', 24], ['large mammal', 24], ['herbivore', 5]]

# SYN = [['herbivore', 'horses'], ['horse','large mammal'], ['horses', 'large mammal'], ['large number of' ,'huge'],
#  ['tons of' , 'large'], ['huge', 'large'], ['mystical', 'magical'] , ['magical','unexplained'], ['magic', 'magical']]
## 

## Example 3 ##
# WF = [['tons of', 2], ['large number of ', 12], ['mystical', 13], ['magical', 28], ['magic', 5], ['unexplained', 11],
#  ['huge', 2], ['large', 51], ['horses', 25], ['horse', 24],['large mammal', 24], ['herbivore', 5], ['large number of', 12]]


# SYN = [["herbivore", "horses"], ["horse","large mammal"], ["horses", "large mammal"], ["large number of" ,"huge"],
#  ["tons of" , "large"], ["huge", "large"], ["mystical", "magical"] , ["magical","unexplained"], ["magic", "magical"],  ["horse","large mammal"]]
##

## Example 4##
# WF = [["white", 12], ["sun yellow", 8], ["sun yellow ", 8], ["blood red", 17], ["pearl", 2], ["green", 15], ["red", 1], ["yellow", 5], ["bone white", 20], ["powder", 60], ["cream", 7]]

# SYN = [["white", "pearl"], ["pearl", "bone white"], ["red", "blood red"], ["powder", "cream",], ["cream", "bone white"], ["yellow", "sun yellow"]]
##



##Create empty dictionary CF for frequency count
CF = {}
    
##Convert WF into a dictionary of form "word : count". Strip leading and ending white space
WF_dict = {} 
for i in WF:
    WF_dict[i[0].strip()] = i[1]


# choose a root name in the alphabet
def get_root_name(word1, word2):
    name = [word1, word2]
    name.sort(key=lambda x:(not x.islower(), x))
    return name[0]

# check if words existing in current hash table
def pairs_in_hash(crosswords, word):
    for row_index, row in enumerate(crosswords):
        if word[0] in crosswords[row_index]:
            return [word[0], row_index, word[1]]
        if word[1] in crosswords[row_index]:
            return [word[1], row_index, word[0]]


# merge and remove duplicates in hash table
def remove_duplicates(hash_list):
    lengthOfHash = len(hash_list)
    index_to_remove = []

    # find duplicate tuples
    if lengthOfHash > 1:
        for i in range(1, lengthOfHash):
            for j in range(0, i):
                for word in hash_list[i]:
                    if word in hash_list[j]:
                        index_to_remove.append([i, j])
                        break

    # merge tuples and remove duplicates
    index_to_remove.reverse()
    for i in range(0, len(index_to_remove)):
        for keyword in hash_list[index_to_remove[i][0]]:
            if keyword not in hash_list[index_to_remove[i][1]]:
                hash_list[index_to_remove[i][1]].append(keyword)

        hash_list.remove(hash_list[index_to_remove[i][0]])
    return hash_list


# generate hash table
def hash_table(syn_list):
    hash_tb = []
    # add words to hash table
    for word in syn_list:
        is_found = pairs_in_hash(hash_tb, word)
        if is_found:
            key_name = get_root_name(hash_tb[is_found[1]][0], is_found[2])
            hash_tb[is_found[1]][0] = key_name
            hash_tb[is_found[1]].append(is_found[2].strip())
        else:
            key_name = get_root_name(word[0], word[1])
            hash_tb.append([key_name.strip(), word[0].strip(), word[1].strip()])

    # remove duplicates
    remove_duplicates(hash_tb)
    return hash_tb

# Generate our hash table of merged synonyms
tempHash = hash_table(SYN)

# Iterate through our new hash table and count the frequency of each word per related words list
# Then add the total frequency of related words list and store it into CF to output
for i in tempHash:
    tempCount = 0
    for j in i:
        tempCount += WF_dict.get(j, 0)
    tempCount -= WF_dict.get(i[0])
    CF[i[0]] = tempCount
    
print("Word Frequencies: WF = " + str(WF) + " of size " + str(len(WF)))
print("Synonyms: SYN = " + str(SYN) + " of size " + str(len(SYN)))
print("CF = " + str(CF) + " of size " + str(len(CF)))