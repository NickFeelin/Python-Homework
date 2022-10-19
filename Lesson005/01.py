# Напишите програму, удаляющую из текста все слова, содержащие "абв"

old_text = 'Съешь-ка еабвщё этих мяабвгких французских буабвлок да выпей чабвю'
print(old_text)

new_text = old_text.split()
# key = 'абв'
# print(' '.join(filter(lambda key: key in new_text, new_text)))

# def filter_words(new_text):
#     text_to_check = 'абв'
#     for word in new_text:
#         if 'абв' in word:
#             return False
#         else:
#             return True
    
# print(list(filter(filter_words, new_text)))
new_text = old_text.split()
for word in new_text:
    if 'абв' in word:
        new_text.remove(word)
        
print(' '.join(new_text))