with open("demo.txt", "a") as file:
    data1 = "good morning\n"
    data2 = "good evening\n"
    data3 = "good night"
    file.writelines([data1, data2, data3])

# wap to count the total no of words present in demo.txt file
# count = 0
# for _ in data.split():
#     count += 1

# readline
# with open("demo.txt")
# Writing the data using append mode:
"""
with open("demo.txt","a") as file:
    # write the data using append
    # file.write("ASAP Get place soon\n")
    data1 = "Chandan Submitted the Documents\n"
    data2 = "Soon HTC will release the offer letter\n"
    data3 = "Already 2 Students got placed\n"
    file.writelines([data1,data2,data3])
    print("Data Added Successfully")
"""
# Read the data from the file:

# --> read() --> It will entire data in the form of string
# --> readline() --> It will read the data line by line nd give the output in the form of string
# --> readlines() --> It will read all the data and return the output in the form of list


# read():
"""
with open("demo.txt") as file:
    # reading  the data
    data = file.read()
    # print(data)
    # wap to check the length of the string
    # print(len(data))

    # wap to count the total no of words present in demo.txt file
    '''
    count = 0
    for _ in data.split():
        count+=1
    print("Total word count:",count)
    '''

    # wap to count the special characters present in demo.txt
    '''
    special_characters = 0
    for i in data:
        if not i.isalpha() and i.isdigit():
            special_characters+=1
    print("Special Character count:",special_characters)
    '''
    # wap to count the words which is starts with vowels present in demo.txt

    # wap to extract the words which startswith vowels from demo.txt file
    '''
    vowel_words = []

    for i in data.split():
        if i[0] in 'aeiouAEIOU':
            vowel_words.append(i)
    print("Total Count:",len(vowel_words))
    print(vowel_words)
    '''
"""

# readline():
"""
with open("demo.txt") as file:
    # Reading the first Line data
    data1 = file.readline()
    data2 = file.readline()
    print(data1)
    print(data2)
"""

# readlines():

with open("demo.txt") as file:
    # Reading all the lines of data
    # all = file.readlines()
    # print(all)

    # wap to count how many lines of data present in demo.txt file
    # all = file.readlines()
    # print("Total Lines:",len(all))

    # wap count the vowels from each and every line from the demo.txt file
    """
    all = file.readlines()
    out = {}
    for lineno,data in enumerate(all,start=1):
        vowel_count = 0
        for j in data:
            if j in 'aeiouAEIOU':
                vowel_count+=1
        out[lineno] = vowel_count
    print(out)
    """
