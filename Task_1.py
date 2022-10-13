# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_text = 'ываабв лповап абвцукв алоабвабв ываываыв'
my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
my_text = ' '. join(my_text)
print(my_text)