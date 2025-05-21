# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay


story = """

At a great meeting of the Animals, who had gathered to elect a new ruler, the Monkey was asked to dance. This he did so well, with a thousand funny capers and grimaces, that the Animals were carried entirely off their feet with enthusiasm, and then and there, elected him their king.

The Fox did not vote for the Monkey and was much disgusted with the Animals for electing so unworthy a ruler.

One day he found a trap with a bit of meat in it. Hurrying to King Monkey, he told him he had found a rich treasure, which he had not touched because it belonged by right to his majesty the Monkey.

The greedy Monkey followed the Fox to the trap. As soon as he saw the meat he grasped eagerly for it, only to find himself held fast in the trap. The Fox stood off and laughed.

"You pretend to be our king," he said, "and cannot even take care of yourself!"

Shortly after that, another election among the Animals was held."""



# Function to translate a word to pig latin
def translate_to_pig_latin(word):
    if word:
        return word[1:] + word[0] + "ay"
    return word

# Split the story into words
words = story.split()

# Translate each word to pig latin
translated_words = [translate_to_pig_latin(word) for word in words]

# Join the translated words back into a string
translated_story = " ".join(translated_words)

print(translated_story)
