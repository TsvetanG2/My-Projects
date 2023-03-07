#result = []
entries = [[u'man', u'thats'],[u'right', u'awesome']]

element = [sub_element for elements in entries for sub_element in elements]
print(element)

#'''''''
# Това е много бавен процес, защото се проеверя лист от лист
#'''''''


#for tag in tags:
    #for entry in entries:
        #if tag in entry:
          #  result.extend(entry)