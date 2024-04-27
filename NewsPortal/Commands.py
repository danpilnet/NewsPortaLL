#
#
# 1)   Создать двух пользователей (с помощью метода User.objects.create_user('username')).
#
# from news.models import *
#
# u1 = User.objects.create_user('Василий')
# u2 = User.objects.create_user('Иван')
#
#
#
# 2)   Создать два объекта модели Author, связанные с пользователями.
#
# a1 = Author.objects.create(user=u1)
# a2 = a1 = Author.objects.create(user=u2)
#
#
#
# 3)   Добавить 4 категории в модель Category.
#
# cat1=Category.objects.create(name='Спорт')
# cat2=Category.objects.create(name='Политика')
# cat3=Category.objects.create(name='Погода')
# cat4=Category.objects.create(name='Здоровье')
#
#
# 4)  cat4=Category.objects.create(name='Здоровье')
#
# Post.objects.create(author_id=1,pole_ar_ne='AR',zagolovok='В Приморском крае наблюдается сложная пожарная обстановка',text='Пожарная обстановка осложнилась из-за сильного ветра и сухой погоды. По данным спутникового мониторинга наблюдается большое количество очагов возгорания.')
# Post.objects.create(author_id=1,pole_ar_ne='AR',zagolovok='Мир был в шоке, когда узнал... Большунов проиграл лыжнику, не попадавшему в сборную Р
# оссии',text='Все хорошее когда-нибудь заканчивается. Правда, в данном случае для русских лыжных гонок скорее плохое. Победная серия Александра Больш
# унова, тянувшаяся по всей огромной России, от Сибири до Севера, с ранней осени до марта, наконец прервалась. Большунов, безусловно, уже великий спортсмен, но хотелось, чтобы и другим дали порулить. И то, как это произошло, получилось эффектно.')
# Post.objects.create(author_id=2,pole_ar_ne='NE',zagolovok='Как выбрать хороший увлажнитель воздуха для квартиры?',text='Увлажнитель – прибор, ко
# торый максимально быстро решает проблему сухого воздуха и все связанные с ним неприятные последствия. Специалисты не раз подчёркивали, что в период отопительного сезона нужно озаботиться вопросом искусственного увлажнения климата в помещении.')
#
#
# 5)   Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий)
#
# PostCategory.objects.create(category_id=3,post_id=1)
# PostCategory.objects.create(category_id=1,post_id=2)
# PostCategory.objects.create(category_id=4,post_id=3)
#
#
#
#
# 6)   Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
#
# Comment.objects.create(text_comment='Вот это новость',comment_id=1,post_comment_id=2)
# Comment.objects.create(text_comment='Плохая погода', comment_id=2, post_comment_id=1)
# Comment.objects.create(text_comment='Спасибо за статью',comment_id=3,post_comment_id=3)



# 7)   Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
#
# post=Post.objects.all()
# post[0].like()
# post[1].like()
# post[1].like()
# post[1].like()
# post[0].like()
# post[4].like()
# post[2].like()
# post[2].like()
# post[2].like()
# post[2].like()
# post[2].like()
#
# post[2].dislike()
# post[2].dislike()
# post[1].dislike()
# post[0].dislike()
# coments=Comment.objects.all()
# coments[0]like()
# coments[0].like()
# coments[0].like()
# coments[0].like()
# coments[1].like()
# coments[2].dislike()
# coments[1].dislike()
#
#
# 8)   Обновить рейтинги пользователей.
#
# authors=Author.objects.all()
# >>> authors[0].uptade_rating()
# >>> authors[1].uptade_rating()



# 9)   Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# Author.objects.all().order_by('-rating').values('user_id__username','rating')[0]




# 10)   Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
#
# b=Post.objects.all().order_by('-rating').values('add_time','author_id__user_id__username','rating','text')[0]
# >>> b['preview']=Post.objects.all().order_by('-rating').first().preview()




# 11)   Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.


# post=Post.objects.all().order_by('-rating')[0]
# Comment.objects.filter(post_comment_id=post).values('time_comment','comment_id__username','rating_comment')













































