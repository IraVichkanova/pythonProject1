
#### Вычисления с помщью Numpy
### Задание 1
import numpy as np

a = np.array(
    [[1, 2, 3, 3, 1], 
    [6, 8, 11, 10, 7]]
).transpose()
print(a)

print("Размерность a {}".format(a.ndim))

print("Форма a {}".format(a.shape))

mean_a = np.mean(a,axis=0)
print(mean_a)

###Задание 2

a_centered = np.subtract(a, mean_a)
print(a_centered)

###Задание 3
a_centered_sp = a_centered.T[0]@a_centered.T[1]
print(a_centered_sp)
a_centered_sp/(a_centered.shape[0]-1)
np.cov(a.T)[0,1]



### Работа с Pandas



##Задание 1

import pandas as pd
authors = pd.DataFrame({'author_id':[1, 2, 3], 
                        'author_name':['Тургенев', 'Чехов', 'Островский']}, 
                       columns=['author_id', 'author_name'])
print(authors)

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                    'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 
                                   'Таланты и поклонники'],
                    'price': [450, 300, 350, 500, 450, 370, 290]},
                   columns=['author_id', 'book_title', 'price'])
print(book)


##Задание 2

authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)

##Задание 3

top5 = authors_price.nlargest(5, 'price')
print(top5)

##Задание 4
authors_stat = authors_price['author_name'].value_counts()
print(authors_stat)
authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)

#Задание 5**

authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
print(authors_price)
book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
book_info['мягкая'] = book_info['мягкая'].fillna(0)
book_info['твердая'] = book_info['твердая'].fillna(0)
print(book_info)
book_info.to_pickle("book_info.pkl")
book_info2 = pd.read_pickle("book_info.pkl")
print(book_info2)