import TgBotMapi as l
import time as t
tg = l.TgBot('mapi')

words = ['Молодая','Яркая', 'Красивая', 'Талантливая', 'Искрящая юмором', 'Романтическая', 'Гармоничная', 'Успешная','Позитивная', 'Целеустремленная', 'Рррразные и Непррэдсказуэмые', 'Милая', 'Трогательная','Любящая','Заботливая','Чувственная','Восхищающая','Вызывающая искренние эмоции','Умеющая блистать и удивлять','Креативная','Энергичная', 'Верная','Крепкая', 'Рождающая замечательных, талантливых детей пара!']
gifs = ['1.mp4', '2.mp4', '3.mp4', '4.jpg', '5.mp4', '6.mp4', '7.mp4', '8.jpg', '9.mp4', '10.mp4', '11.jpg', '12.mp4', '13.mp4', '14.mp4', '15.mp4', '16.mp4', '17.mp4', '18.mp4', '19.jpg', '20.mp4', '21.mp4', '22.mp4', '23.mp4', '24.jpg']

def startik(message):
    tg.message("Юра и Вика, поздравляем с серебряной свадьбой!\nВы -", message)
    t.sleep(3.0)
    for i in range(len(words)):
       tg.message(words[i], message)
       t.sleep(1.0)
       img = open(gifs[i], 'rb')
       if i == 3 or i == 7 or i == 10 or i == 18 or i == 23:
          tg.bot.send_photo(message.chat.id, img, None, 'Text')
          if i == 18:
             video = open('19.mp4', 'rb')
             tg.bot.send_video(message.chat.id, video, None, 'Text')
             video.close()
       else:
         tg.bot.send_video(message.chat.id, img, None, 'Text')
       img.close()
       t.sleep(3.0)
    tg.message("Желаем (кроме банальностей-здоровья, любви, долгих лет жизни) , миллиарды букетов счастья! В этих букетиках все ваши желания пусть будут наполнены улыбками, исполнениями желаний, страстью, взаимопониманием, пониманием, компромиссами, позитивом и оптимизмом! И пусть ни один из букетиков никогда не завянет!\n\nПусть жизнь будет наполнена большим количеством прекрасных моментов! ", message)
    img = open('end.mp4', 'rb')
    tg.bot.send_video(message.chat.id, img, None, 'Text')
    img.close()

tg.hadler('start', startik)


tg.start()