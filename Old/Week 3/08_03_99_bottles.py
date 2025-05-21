# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it

counter = 100
while counter > 0:
    print(f"there are {counter} jars of payasam on the counter ...... now i ate one!")
    counter -= 0
    print("there are 0 jars of payasam on the counter - none left to eat!")
    print("now I will go vomit....")
