import telebot
from telebot import types

bot = telebot.TeleBot('6361832970:AAGrmSdY2yIVd4flbtb1EuZb4E92wjQ1ZXk')
wizard_chat_id = -4109398904
id = 0
dictionary = dict()

try:
    @bot.message_handler(func=lambda message: message.chat.id == wizard_chat_id)
    def handle_reply(message):
        try:
            global id
            global dictionary
            original_message = message.reply_to_message
            idd = int(original_message.text.split('/')[0])
            bot.reply_to(dictionary[idd], message.text)
        except:
            bot.send_message(message.chat.id,
                             'Вам нужно обязательно ответить на сообщение! (либо Вы ответили не на то сообщение)')


    @bot.message_handler(commands=['start'])
    def main(message):
        global id
        global dictionary
        hide_markup = types.ReplyKeyboardRemove()
        dictionary[id] = message
        id += 1
        txt = (
            'Привет, Сосед! Я с радостью помогу тебе и твоим соседям классно провести время, а возможно даже улучшить взаимоотношения. \n'
            'Немного расскажу, как это все будет проходить. Каждый из участников команды пишет мне и отвечает на вопросы, которые я буду задавать. '
            'На основе этой информации подбираются активности для вас, так что отвечайте честно) \n'
            'Всё, что от тебя требуется - собраться со своими друзьями в одном помещении, и всем вместе написать мне.\n\n'
            'Для того, чтобы начать отвечать на вопросы - нажми /team_name \n'
            'Если ты ошибся, то нажми - /help')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=hide_markup)


    @bot.message_handler(commands=['team_name'])
    def main(message):
        global id
        global dictionary
        hide_markup = types.ReplyKeyboardRemove()
        dictionary[id] = message
        id += 1
        txt = (
            'Придумайте название для своей компании. Например: Смешарики. (каждый участник должен указать одно и то же название, иначе бот не сможет корректно обработать Ваш запрос): \n'
            'После ответа на данное сообщение нажмите на /set_name')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=hide_markup)


    @bot.message_handler(commands=['set_name'])
    def main(message):
        global id
        global dictionary
        hide_markup = types.ReplyKeyboardRemove()
        dictionary[id] = message
        id += 1
        txt = ('Укажите Ваше имя: \n'
               'После ответа на данное сообщение нажмите на /set_gender')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=hide_markup)


    @bot.message_handler(commands=['set_gender'])
    def main(message):
        global id
        global dictionary
        dictionary[id] = message
        id += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 - Мужской")
        button2 = types.KeyboardButton("2 - Женский")
        markup.add(button1, button2)
        txt = ('Укажите Ваш пол: \n'
               '1 - Мужской \n'
               '2 - Женский \n'
               'После ответа на данное сообщение нажмите на /purpose_of_use')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=markup)


    @bot.message_handler(commands=['purpose_of_use'])
    def main(message):
        global id
        global dictionary
        dictionary[id] = message
        id += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 - развлечься")
        button2 = types.KeyboardButton("2 - узнать друг друга получше")
        button3 = types.KeyboardButton("3 - снизить психологическое напряжение, улучшить отношения")
        markup.add(button1, button2, button3)
        txt = ('Укажите цель использования бота: \n'
               '1 - развлечься \n'
               '2 - узнать друг друга получше \n'
               '3 - снизить психологическое напряжение, улучшить отношения \n'
               'После ответа на данное сообщение нажмите на /how_you_want_to_spend_your_time')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=markup)


    @bot.message_handler(commands=['how_you_want_to_spend_your_time'])
    def main(message):
        global id
        global dictionary
        dictionary[id] = message
        id += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 - спокойные активности в помещении")
        button2 = types.KeyboardButton("2 - подвижные активности в помещении")
        button3 = types.KeyboardButton("3 - активности с необходимостью в предварительной подготовке")
        button4 = types.KeyboardButton("4 - активности на открытом воздухе")
        button5 = types.KeyboardButton("5 - другое (напишу сообщением)")
        markup.add(button1, button2, button3, button4, button5)
        txt = ('Укажите, как бы хотели провести время: \n'
               '1 - спокойные активности в помещении \n'
               '2 - подвижные активности в помещении \n'
               '3 - активности с необходимостью в предварительной подготовкеи \n'
               '4 - активности на открытом воздухе \n'
               '5 - другое (напишу сообщением) \n'
               'После ответа на данное сообщение нажмите на /how_you_do_not_want_to_spend_time')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=markup)


    @bot.message_handler(commands=['how_you_do_not_want_to_spend_time'])
    def main(message):
        global id
        global dictionary
        dictionary[id] = message
        id += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 - спокойные активности в помещении")
        button2 = types.KeyboardButton("2 - подвижные активности в помещении")
        button3 = types.KeyboardButton("3 - активности с необходимостью в предварительной подготовке")
        button4 = types.KeyboardButton("4 - активности на открытом воздухе")
        button5 = types.KeyboardButton("5 - другое (напишу сообщением)")
        markup.add(button1, button2, button3, button4, button5)
        txt = ('Укажите, как точно бы не хотели провести время: \n'
               '1 - спокойные активности в помещении \n'
               '2 - подвижные активности в помещении \n'
               '3 - активности с необходимостью в предварительной подготовкеи \n'
               '4 - активности на открытом воздухе \n'
               '5 - другое (напишу сообщением) \n'
               'После ответа на данное сообщение нажмите на /spent_time')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=markup)


    @bot.message_handler(commands=['spent_time'])
    def main(message):
        global id
        global dictionary
        dictionary[id] = message
        id += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1 - 15мин")
        button2 = types.KeyboardButton("2 - 30мин")
        button3 = types.KeyboardButton("3 - 45мин")
        button4 = types.KeyboardButton("4 - 60мин")
        button5 = types.KeyboardButton("5 - 60мин+")
        markup.add(button1, button2, button3, button4, button5)
        txt = ('Укажите, сколько времени готовы потратить: \n'
               '1 - 15мин \n'
               '2 - 30мин \n'
               '3 - 45мин \n'
               '4 - 60мин \n'
               '5 - 60мин+ \n'
               'После ответа на данное сообщение нажмите на /leader')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=markup)


    @bot.message_handler(commands=['leader'])
    def main(message):
        global id
        global dictionary
        hide_markup = types.ReplyKeyboardRemove()
        dictionary[id] = message
        id += 1
        txt = ('Кому из участников компании будут отправлены правила проведения активностей? (введите сами имя): \n'
               'После ответа на данное сообщение вы получите перечень возможных вариантов проведения времени вместе со своими соседями, собранный исходя из предпочтений и антипредпочтений каждого участника (на анализ информации и подбор активностей может уйти какое-то время)\n'
               'Если вы при вводе какой-либо информации ошиблись - нажмите на /help')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}\n <b><u>Ожидает ответа "Волшебников"</u></b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, txt, reply_markup=hide_markup)


    @bot.message_handler(commands=['help'])
    def main(message):
        global id
        global dictionary
        hide_markup = types.ReplyKeyboardRemove()
        dictionary[id] = message
        id += 1
        txt = ('Если вы ошиблись в заполнении информации или же хотите ее поменять, то:\n'
               'Для изменения названия компании: /team_name \n'
               'Для изменения своего имени: /set_name \n'
               'Для изменения своего пола: /set_gender \n'
               'Для изменения цели использования бота: /purpose_of_use \n'
               'Для изменения того, как бы хотели провести время: /how_you_want_to_spend_your_time \n'
               'Для изменения того, как бы точно не хотели провести время: /how_you_do_not_want_to_spend_time \n'
               'Для изменения времени, которое вы готовы потратить: /spent_time \n'
               'Для изменения лидера компании: /leader \n')
        bot.send_message(wizard_chat_id,
                         f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\n\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n{txt}')
        bot.send_message(message.chat.id, txt, reply_markup=hide_markup)


    @bot.message_handler(func=lambda message: message.chat.id != wizard_chat_id)
    def handle_reply(message):
        try:
            global id
            global dictionary
            dictionary[id] = message
            id += 1
            bot.send_message(wizard_chat_id,
                             f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\nОтправил сообщение: {message.text}')
        except:
            bot.send_message(wizard_chat_id,
                             f'{id - 1}/\nПользователь {message.from_user.first_name} (username пользователя: {message.from_user.username})\nОтправил сообщение:\n{message.text}\n\nОтвет бота:\n Не можем обработать ваш запрос, пожалуйста, повторите ввод')
            bot.send_message(message.chat.id,
                             'Не можем обработать ваш запрос, пожалуйста, повторите ввод')

    bot.polling(none_stop=True)
except:
    bot.send_message(wizard_chat_id,
                             '<b><u>БОТ УПАЛ</b></u>', parse_mode='html')