from pyDatalog import pyDatalog

print('\n''------------START------------''\n')

# страница 1
print('\n''------------страница 1------------''\n')

pyDatalog.create_terms('FACULTY, GROUP, YEARS, NAME, HEAD, GROUPHEAD, univ, infogroup, zapr3')

+(univ('Электротехнический факультет', '19/20 год', 'декан Костыгов'))
+(infogroup('Электротехнический факультет', 'группа АСУ2-19-1м', 'направление интеллектуальные системы', 'староста Фоминых'))
print('Запрос 1: Чей журнал? ''\n')
zapr3(FACULTY, GROUP) <= (univ(FACULTY, YEARS, HEAD)) & (infogroup(FACULTY, GROUP, NAME, GROUPHEAD))
print(zapr3('Электротехнический факультет', GROUP))

#_страница 2__
print('\n''------------страница 2------------''\n')

pyDatalog.create_terms('FACULTY, GROUP, YEARS, NAME, HEAD, GROUPHEAD, univ, infogroup, zapr2')
+(univ('Электротехнический факультет', '19/20 год', 'декан Костыгов'))
+(infogroup('Электротехнический факультет', 'группа АСУ2-19-1м', 'направление интеллектуальные системы', 'староста Фоминых'))
print('Запрос 2:В каком году староста Фоминых? ''\n')
zapr2(GROUPHEAD, YEARS) <= (univ(FACULTY, YEARS, HEAD)) & (infogroup(FACULTY, GROUP, NAME, GROUPHEAD))
print(zapr2('староста Фоминых', YEARS))

# страница 3
print('\n''------------страница 3------------''\n')

pyDatalog.create_terms('GROUP, Z, Y, NUMBER, STUDENT, lst, prog, zap4')
+(lst('1', 'Аюпов Александр Дамирович'))
+(lst('2', 'Барсуков Андрей Сергеевич'))
+(lst('3', 'Беляев Евгений Леонидович'))
+(lst('4', 'Боброва Ирина Александровна'))
+(lst('5', 'Гребеньщикова Елизавета Витальевна'))
+(lst('6', 'Клейменова Вероника Альбертовна'))
+(lst('7', 'Князев Александр Игоревич'))
+(lst('8', 'Орлова Екатерина Дмитриевна'))
+(lst('9', 'Фоминых Полина Юрьевна'))
+(lst('10', 'Швецов Владислав Валерьевич'))
print('Запрос 3: Кто находится в списке под номером 5?''\n')
zap4(NUMBER, STUDENT) <= lst(NUMBER, STUDENT)
print(zap4('5', STUDENT))

# страница 4
print('\n''------------страница 4------------''\n')

pyDatalog.create_terms('LESSON,HOUR,TEACHER,PAGE,lesson,teacher,page_journal,zap1')
+(lesson('Высокоинтеллектуальные платформы цифровой экономики', '144', '8-9'))
+(lesson('Алгоритмические языки программирования', '180', '10-11'))
+(lesson('Высокопроизводительные вычисления и облачные технологии', '144', '12-13'))
+(lesson('Математические методы теории и систем', '144', '14-15'))
+(lesson('Профессиональный иностранный язык', '72', '16-17'))
+(lesson('Философские проблемы науки и техники', '72', '18-19'))
+(lesson('Деловое сотрудничество и психология взаимодействия в коллективе', '20-21'))
+(lesson('Моделирование знаний', '22-23'))
+(teacher('Мартин Кютц', 'Высокоинтеллектуальные платформы цифровой экономики', ))
+(teacher('Курушин Даниил Сергеевич', 'Алгоритмические языки программирования'))
+(teacher('Сивков Сергей Павлович', 'Высокопроизводительные вычисления и облачные технологии'))
+(teacher('Бернд Краузе', 'Математические методы теории и систем'))
+(teacher('Хабибрахмановна Фарида Рафиковна', 'Профессиональный иностранный язык'))
+(teacher('Оконская Наталья Камильевна', 'Философские проблемы науки и техники'))
+(teacher('Дуванская Мария Константиновна', 'Деловое сотрудничество и психология взаимодействия в коллективе'))
+(teacher('Долгова Елена Владимировна', 'Моделирование знаний'))
print('Запрос 4: На какой странице находится предмет, который ведет Хабибрахмановна Фарида Рафиковна?''\n')
page_journal(PAGE, TEACHER) <= teacher(TEACHER, LESSON) & lesson(LESSON, HOUR, PAGE)
print(page_journal(PAGE, 'Хабибрахмановна Фарида Рафиковна'))
print('\n''Запрос 5: Какие предметы ведет Кютц и кол-во часов?''\n')
zap1(TEACHER, LESSON, HOUR) <= (teacher(TEACHER, LESSON)) & (lesson(LESSON, HOUR, PAGE))
print(zap1('Мартин Кютц', LESSON, HOUR))

# страница 5
print('\n''------------страница 5------------''\n')

pyDatalog.create_terms('GROUP, Z, Y, NUMBER, PR_N, PR, STUDENT, lst, prog, zap2, summ_')
+(lst('1', 'Аюпов Александр Дамирович'))
+(lst('2', 'Барсуков Андрей Сергеевич'))
+(lst('3', 'Беляев Евгений Леонидович'))
+(lst('4', 'Боброва Ирина Александровна'))
+(lst('5', 'Гребеньщикова Елизавета Витальевна'))
+(lst('6', 'Клейменова Вероника Альбертовна'))
+(lst('7', 'Князев Александр Игоревич'))
+(lst('8', 'Орлова Екатерина Дмитриевна'))
+(lst('9', 'Фоминых Полина Юрьевна'))
+(lst('10', 'Швецов Владислав Валерьевич'))
+(prog('АСУ2', '1', 3, 2))
+(prog('АСУ2', '2', 1, 0))
+(prog('АСУ2', '1', 5, 1))
+(prog('АСУ2', '4', 7, 3))
+(prog('АСУ2', '5', 0, 6))
+(prog('АСУ2', '6', 0, 2))
+(prog('АСУ2', '7', 7, 10))
+(prog('АСУ2', '8', 6, 0))
+(prog('АСУ2', '9', 0, 0))
+(prog('АСУ2', '10', 10, 10))
print('Запрос 6: Вывести кол-во уважительных прогулов у Князева''\n')
zap2(STUDENT, PR) <= lst(NUMBER, STUDENT) & prog(GROUP, NUMBER, PR, PR_N)
print(zap2('Князев Александр Игоревич', PR))
print('\n''Запрос 7: Вывести количество неуважительных прогулов в группе АСУ2''\n')
(summ_[GROUP] == _sum(PR_N, for_each=NUMBER)) <= (prog(GROUP, NUMBER, PR, PR_N))
print(summ_['АСУ2'] == PR_N)

#страница 6
print('\n''------------страница 6------------''\n')

pyDatalog.create_terms('DATA, TYPE, TOPIC, HOURS, les, info, zap6, zap7')
+(les('22.10', 'алгоритм'))
+(les('23.10', 'логическое программирование'))
+(les('23.10', 'лямбда функции'))
+(les('25.10', 'мультипроцессинг'))
+(info('П', 'алгоритм', '2'))
+(info('П', 'логическое программирование', '4'))
+(info('Л', 'лямбда функции2', '2'))
+(info('Л', 'мультипроцессинг', '2'))
print('Запрос 8: Какой урок был 22.10?''\n')
zap6(DATA, TOPIC) <= (les(DATA, TOPIC))
print(zap6('22.10', TOPIC))
print('\n''Запрос 9: Когда и как называлось 4-х часовое занятие?''\n')
zap7(DATA, HOURS, TOPIC) <= les(DATA, TOPIC) & info(TYPE, TOPIC, HOURS)
print(zap7(DATA, '4', TOPIC))

print('\n''------------END------------''\n')
