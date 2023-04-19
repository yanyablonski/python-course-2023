
print( "Введите сколько будет строк" )
n = int(input(""))
print( f"Введите {n} слова!" )
print( "и потом Введите значение слова !" )
words_dict = {}
for i in range (n):
    Word = str(input(""))
    words_dict[Word] = str(input())
print("входные данные:")
print(words_dict)
print("сколько слов будем искать")
m = int(input(""))
if n < m:
    print("вы вели то число проверяемых слов, которых нету в списке")
print("какое слово вы хотите поискать ")    
m = str(input(""))
if m in words_dict:
    print( "такое слово есть" )
else:
    print("таково слово ненайдено")

print("входные данные")
print(words_dict[m])
