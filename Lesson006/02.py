# Напишите програму, удаляющую из текста все слова, содержащие "абв"

old_text = 'Съешь-ка еабвщё этих мяабвгких французских буабвлок да выпей чабвю'
print(old_text)
new_text = old_text.split()
new_list = [word for word in new_text if 'абв' not in word] 
        
print(' '.join(new_list))