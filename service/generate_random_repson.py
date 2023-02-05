from model.patient_model import Patient
import random
from  datetime import datetime
name_female = ['Анастасия', 'Анна', 'Мария', 'Елена', 'Дарья', 'Алина', 'Ирина',
               'Екатерина', 'Арина', 'Полина', 'Ольга', 'Юлия', 'Татьяна', 'Наталья',
               'Виктория', 'Елизавета', 'Ксения', 'Милана', 'Вероника', 'Алиса',
               'Валерия', 'Александра', 'Ульяна', 'Кристина', 'София', 'Марина',
               'Светлана', 'Варвара', 'Софья', 'Диана', 'Яна', 'Кира', 'Ангелина',
               'Маргарита', 'Ева', 'Алёна', 'Дарина', 'Карина', 'Василиса', 'Олеся',
               'Аделина', 'Оксана', 'Таисия']

name_male = ['Александр', 'Дмитрий', 'Максим', 'Сергей',
             'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил', 'Никита', 'Матвей',
             'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Даниил', 'Тимофей',
             'Владислав', 'Игорь', 'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур',
             'Олег', 'Ярослав', 'Антон', 'Николай', 'Глеб', 'Данил', 'Савелий', 'Вадим',
             'Степан', 'Юрий', 'Богдан', 'Артур', 'Семен', 'Макар', 'Лев']

female_middle_name = ['Александровна', 'Алексеевна', 'Анатольевна', 'Андреевна', 'Антоновна',
                      'Аркадьевна', 'Артемовна', 'Богдановна', 'Борисовна', 'Валентиновна', 'Валерьевна',
                      'Васильевна', 'Викторовна', 'Виталиевна', 'Владимировна', 'Владиславовна', 'Вячеславовна',
                      'Геннадиевна', 'Георгиевна', 'Григорьевна', 'Даниловна', 'Денисовна',
                      'Дмитриевна', 'Евгеньевна', 'Егоровна', 'Ефимовна']

male_last_name = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов',
                  'Новиков', 'Морозов', 'Петров', 'Волков', 'Соловьёв', 'Васильев', 'Зайцев',
                  'Павлов', 'Семёнов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьёв', 'Фёдоров',
                  'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселёв', 'Макаров',
                  'Андреев', 'Ковалёв', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов',
                  'Куликов', 'Алексеев', 'Степанов', 'Яковлев', 'Сорокин', 'Сергеев', 'Романов', 'Захаров',
                  'Борисов', 'Королёв', 'Герасимов', 'Пономарёв', 'Григорьев', 'Лазарев', 'Медведев', 'Ершов',
                  'Никитин', 'Соболев', 'Рябов', 'Поляков', 'Цветков', 'Данилов']

male_middle_name = ['Алексеевич', 'Анатольевич', 'Андреевич', 'Антонович', 'Аркадьевич',
                    'Артемович', 'Бедросович', 'Богданович', 'Борисович', 'Валентинович',
                    'Валерьевич', 'Васильевич', 'Викторович', 'Витальевич', 'Владимирович',
                    'Владиславович', 'Вольфович', 'Вячеславович', 'Геннадиевич', 'Георгиевич',
                    'Григорьевич', 'Данилович', 'Денисович', 'Дмитриевич', 'Евгеньевич', 'Егорович',
                    'Ефимович', 'Иванович', 'Иваныч', 'Игнатьевич', 'Игоревич', 'Ильич', 'Иосифович',
                    'Исаакович', 'Кириллович', 'Константинович', 'Леонидович', 'Львович', 'Максимович',
                    'Матвеевич', 'Михайлович', 'Николаевич', 'Олегович']

female_last_name = ['Иванова', 'Петрова', 'Смирнова', 'Кузнецова', 'Васильева', 'Попова', 'Новикова', 'Волкова',
                    'Романова', 'Козлова', 'Соколова', 'Андреева', 'Морозова', 'Николаева', 'Михайлова', 'Павлова',
                    'Алексеева', 'Макарова', 'Сергеева', 'Егорова', 'Орлова', 'Александрова', 'Степанова', 'Никитина',
                    'Лебедева', 'Зайцева', 'Захарова', 'Яковлева', 'Максимова', 'Фролова', 'Григорьева', 'Шевченко',
                    'Миронова', 'Белова', 'Мельникова', 'Борисова', 'Кузьмина', 'Дмитриева', 'Федорова', 'Семенова',
                    'Антонова', 'Медведева', 'Полякова', 'Матвеева', 'Тарасова', 'Власова', 'Жукова']


street = ['Проспект Революции', 'Плехановская', 'Кольцовская', 'Карла Маркса', 'Театральная', 'Орджоникидзе',
          '25 октября', 'Проспект Московский', 'Краснознаменная', 'Бульвар Победы',
          'Антонова-Овсиенко', 'Минская', 'Остужева', 'Димитрова', 'Волгоградская']

def generate_person():
    patient = Patient()
    women = random.randint(0, 10)
    if women > 5:
        patient.gender = 'female'
        patient.firstname = random.choice(name_female)
        patient.middle_name = random.choice(female_middle_name)
        patient.last_name = random.choice(female_last_name)
    else:
        patient.gender = 'male'
        patient.firstname = random.choice(name_male)
        patient.middle_name = random.choice(male_middle_name)
        patient.last_name = random.choice(male_last_name)

    date_str = f'{random.randint(1, 28)}.{random.randint(1, 12)}.{random.randint(1960, 2000)}'
    date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
    patient.date_of_birth = date_obj
    patient.address = f'г.Воронеж ул. {random.choice(street)} дом. {random.randint(1, 100)}' \
                      f' кв. {random.randint(1, 200)}'

    patient.phone = f'+7({random.randint(900, 999)})-{random.randint(100, 999)}' \
                    f'-{random.randint(10,99)}-{random.randint(10, 99)}'
    for i in range(4):
        patient.polis_oms += str(random.randint(1000, 9999))
        if i == 3:
            break
        patient.polis_oms += ' '

    patient.document = f'Паспорт серия: {random.randint(10, 20)} {random.randint(10, 20)} №:{random.randint(100000, 999999)}'
    patient.snils = f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(10, 99)}'
    # print(patient.full_name)

    return patient


if __name__ == '__main__':
    generate_person()
