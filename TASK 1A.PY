text = 'I love Python [red_heart] , it is brilliant [thumbs_up]'
text_tokens = text.split(" ")

new_text = ""
for i in text_tokens:
    if i in emoji_dictionary2:
        new_text += " " + emoji_dictionary2[i]
    else:
        new_text += " " + i

print(new_text)