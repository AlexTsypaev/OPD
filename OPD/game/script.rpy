﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define admin = Character('Админ', color="#7FFFD4", image = 'admin')
define d = Character('Директор', color="#E52B50", image = 'director')
define i = Character('Игорь', color="#78DBE2", image = 'igor')
define a = Character('Алексей', color = "#7FFFD4", image = 'alex')
define g = Character('Григорий', color = "#89AC76", image = 'gregory ')
define ilya = Character("Илья", color = "#6495ED", image = 'ilya')
define ega = Character("Егор", color = "#E7C697", image = 'egor')
define sam1 = False
define admin1 = False

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    scene bg office
    with Dissolve(.5)

    "Админ приходит на работу, как обычно делает себе кофе, и в этот момент заходит директор. Диалог директора и админа."
    show admin normal at right
    with Dissolve(.5)

    show director happy at left
    with Dissolve(.5)
    d "Сегодня к нам в офис придёт команда студентов. Твоя задача, в случае необходимости, помогать им. Постарайтесь не уничтожить нашу компанию."
    admin sad "Лучшая новость с утра. Я даже кофе не успел допить… Они хоть знают как компьютер выглядит?"
    d normal "Всё в порядке. Мне сказали, что это смышлёные студенты, но расслабляться нельзя. Вдруг обманули."
    hide admin
    with moveoutright
    hide director
    with moveoutleft
    "Первый студент – Игорь. Парень учится на программиста, но никогда не сталкивался с работой сисадмина."
    #hide bg office
    scene bg server
    with fade
    #with Dissolve(.5)
    show igor normal at right
    with Dissolve(.5)
    show admin normal at left
    "Игорь первым приходит на практику, и его сразу просят решить проблемы в бухгалтерии с компьютером."
    menu:
        i "Как решить проблему?"
        "Самостоятельно попытаться решить проблему":
            $ sam1 = True
            jump choice_sam

        "Обратиться за помощью к сисадмину":
            $ admin1 = True
            jump choice_admin
    return

label choice_admin:
    "Игорь не понимает в чём проблема, поэтому он обращается к админу по телефону"
    i lost "Добрый день, не знаю, что делать, тут с сайтом проблема"
    admin "Что за проблема?"
    i lost "Да тут…Даже не знаю… в бухгалтерии не работает сайт для отчетов!"
    admin "Ладно, ты пробовал перезапустить компьютер? Всегда перезапускай компьютер – это лучший способ решения проблем! А лучше три раза перезапусти!"
    i happynes "Спасибо, сейчас сделаю."
    "После перезагрузки всё снова работает."
    hide admin
    hide bg server
    with Dissolve(.5)
    #hide igor_normal
    "Проходит некоторое время и к Игорю присоединяются два опоздавших студента: Григорий и Алексей. "
    show alex normal at left
    with moveinleft
    show gregory normal
    with moveinright
    "В это время сисадмин играет в CS, а в бухгалтерии снова возникают проблемы: у работников начинает всё жутко тормозить."
    menu:
        i "Как решить проблему?"
        "Самостоятельно попытаться решить проблему":
            jump choice_sam2

        "Обратиться за помощью к сисадмину":
            jump choice_admin2
    return
    return

label choice_sam:
    "Игорь самостоятельно решает разобраться с проблемой, но не совсем понимает в чём дело. Он решает просто выдернуть провод из розетки и обратно всё включить после чего отчитывается о проделанной работе сисадмину."
    i happy "Здравствуйте, я решил проблему с компом в бухгалтерии."
    admin "А что ты сделал?"
    i happy "Я из розетки провод выдернул, всё выключилось, и я обратно включил. "
    admin scarry "*Про себя* (Чёрт…Этот студент радикальными методами решает проблемы, он же мог операционку «убить»). Больше ничего не трогай, сейчас я приду и проверю. Никогда не выдёргивай провода. Понял?"
    hide admin
    hide bg server
    with Dissolve(.5)
    #hide igor_normal
    "Проходит некоторое время и к Игорю присоединяются два опоздавших студента: Григорий и Алексей. "
    show alex normal at left
    with moveinleft
    show gregory normal
    with moveinright
    "В это время сисадмин играет в CS, а в бухгалтерии снова возникают проблемы: у работников начинает всё жутко тормозить."
    menu:
        i "Как решить проблему?"
        "Самостоятельно попытаться решить проблему":
            jump choice_sam2

        "Обратиться за помощью к сисадмину":
            jump choice_admin2
    return
    return

label choice_admin2:
    g uncertainty "У нас сегодня первая практика и я думаю, что это прекрасный шанс её провалить если не обратиться к админу. Что думаете?"
    a optimism "Ну чего ты, нужно быть уверенней. Я вот думаю, что это шанс доказать, что мы здесь не просто так находимся. "
    if sam1:
        i normal "Я согласен с Лёшей можно попробовать самим всё исправить. Я сегодня уже общался с админом и думаю, что мне повезло, что я общался по телефону. Он очень злой."
    if admin1:
        i normal " Может быть, мы сами всё решим? Я вот сегодня уже просил помощи сисадмина, мне кажется, что, если за нас будут всё делать, мы ничему не научимся."
        a normal "Красиво сказано. Я поддерживаю эту идею."
    g normal "Ну и с чего начнём?"
    i lost "Ну… Админ вроде говорил нужно сайт перезапустить."
    a happy "Сайт работает на каком-то сервере, нам нужно найти серверную и перезапустить сервер."
    i lost "*Одновременно с Алексеем, но неуверенно и тихо* а может и не сайт."
    "Студенты вышли в коридор и перед глазами увидели стальную дверь с надписью «Серверная»."
    a happy "Нам сегодня везёт. Вот оно сердце компании!"
    "Они зашли в серверную и решили всё перезапустить разом. Ну а дальше понятно. Директор в панике забегает к админу…"
    show director normal:
        xalign 0.75
    d panika "Что ты с серверами сделал? Ты перезапустил их?"
    admin scarry "*Быстро сворачивает окно с CS и судорожно смотрит в программу мониторинга работы сетевого оборудования*"
    admin scarry "Я ничего не делал. Кто-то в серверной решил всё перезапустить.  Вот же… админ в предчувствии нехорошего ринулся к дверям серверной комнаты, а из нее выходили с радостными улыбками три студента – они «решили» проблему с тормозами сервера! Нет сервера – нет проблем!"
    hide admin
    hide director
    hide igor
    hide gregory
    hide alex
    "Новая история"
    menu:
        i "Какой сюжет вы хотите выбрать ?"
        "За Илью":
            jump choice_Ilyxa

        "За Егора":
            jump choice_Egor
    return
    return

label choice_sam2:
    "Студенты решают разобраться с проблемой общими усилиями, без привлечения системного администратора."
    if sam1:
        i lost "Слушайте я сегодня уже успел поговорить с админом и у меня такое чувство, что он злой на меня. Я предлагаю самим всё сделать, вроде ничего сложного."
        a happy "Ну в принципе можем попробовать, мы же с компьютерами на «Ты»."

    if admin1:
        "Я не знаю, что здесь за вариант ответа)"
    g normal "Ну и с чего начнём?"
    i lost "Ну… Админ вроде говорил нужно сайт перезапустить."
    a happy "Сайт работает на каком-то сервере, нам нужно найти серверную и перезапустить сервер."
    i lost "*Одновременно с Алексеем, но неуверенно и тихо* а может и не сайт."
    "Студенты вышли в коридор и перед глазами увидели стальную дверь с надписью «Серверная»."
    a happy "Нам сегодня везёт. Вот оно сердце компании!"
    "Они зашли в серверную и решили всё перезапустить разом. Ну а дальше понятно. Директор в панике забегает к админу…"
    show director normal:
        xalign 0.75
    d panika "Что ты с серверами сделал? Ты перезапустил их?"
    admin scarry "*Быстро сворачивает окно с CS и судорожно смотрит в программу мониторинга работы сетевого оборудования*"
    admin scarry "Я ничего не делал. Кто-то в серверной решил всё перезапустить.  Вот же… админ в предчувствии нехорошего ринулся к дверям серверной комнаты, а из нее выходили с радостными улыбками три студента – они «решили» проблему с тормозами сервера! Нет сервера – нет проблем!"
    hide admin
    hide director
    hide igor
    hide gregory
    hide alex
    "Новая история"
    menu:
        i "Какой сюжет вы хотите выбрать ?"
        "За Илью":
            jump choice_Ilyxa

        "За Егора":
            jump choice_Egor
    return
    return

label choice_Egor:
    "Начинается всё со звонка одного из работников сисадмину."
    show admin normal at left
    show egor standart at right
    ega standart "Привет, через час мне нужно будет рассказать доклад на собрании, а у меня папка пустая, в которою я сохранял отчёт. Нужна твоя помощь."
    admin normal "Ты точно его сохранил?"
    ega yverenno "Да, конечно."
    admin normal "Можешь сказать в какой папке находится твой доклад. Я подключусь к твоему компу и посмотрю, что не так."
    ega yverenno "Я скину тебе, где он должен хранится и его название."
    admin normal "У тебя две одинаковые папки. Только папку с докладом ты назвал с английской буквы с (стат. отчёт) Могу отправить твой доклад сразу секретарю, чтобы он тебе всё распечатал."
    ega dovolnyi "Было бы неплохо, спасибо за помощь."
    return



label choice_Ilyxa:
    "Начинается всё со звонка одного из работников сисадмину."
    show admin normal at left
    show ilya scary at right
    ilya scary "Привет, у меня критическая ситуация: через 10 минут у нас собрание, а у меня не открывается доклад."
    admin normal " А что в докладе было?"
    ilya scary "Нет времени на объяснения. Ты сможешь помочь открыть его?"
    admin normal "Ладно не важно. В какой папке лежит доклад?"
    ilya standart "В папке…? Папки у меня в сейфе хранятся, а документ лежит в word и его нужно как-то открыть."
    admin chastliv "Нет. Ты меня не понял. Я про папку или каталог, или директорию. Ну объект в файловой системе, упрощающий организацию файлов."
    ilya standart  "Ааа подожди… Как всё, что ты сейчас сказал, относится к моему докладу. Ты можешь просто открыть его? Ты же знаешь я в компах не разбираюсь."
    admin normal "Сейчас я найду тебе его. Так стоп у тебя на компе 20 докладов какой из них нужен?"
    ilya happy "Который последний."
    admin normal "Я отправлю секретарю, и он распечатает тебе."
    ilya happy "Ну всё я побежал, у меня через минуту собрание. Спасибо большое."
    "Те 20 докладов были отсортированы по дате. И то, что было нужно Илье, было первым в списке, а не последним."
    "После собрания Илья решил поговорить с админом."
    menu:
        i "Как вы хотите поговорить с админом?"
        "Проявить агрессию":
            jump choice_Ilyx_zloy

        "Решить вопрос без агрессии":
            jump choice_Ilyx_norm
    return
    return
label choice_Ilyx_zloy:
    admin normal "Новые проблемы?"
    ilya zloy "Нет. Только одна. Меня из-за твоего доклада чуть не уволили."
    admin ponimat "Не понял. Почему из-за моего?"
    ilya zloy "Мне распечатали не тот доклад. Я же сказал, что это очень важно."
    admin ponimat "Я отправил то, что ты меня попросил. Какие ко мне могут быть вопросы. Просто научись нормально называть свои файлы и таких проблем не будет."
    ilya  ydiv "Я ещё и виноват. У меня такое подозрение, что вы не работаете, а развлекаетесь."
    ilya ydiv "Раньше у нас был админ, который постоянно ходил в наших кабинетах, что-то настраивал. По нему было видно, что он выкладывался на работе. Вас я видел только 1 раз, когда вы к нам устроились, и директор представил вас."
    admin sad "Вы не понимаете суть работы сисадмина. Хорошего сисадмина не должно быть видно в офисе, потому что у него всё настроено как нужно и сбои решаются удалённо и быстро. Он знает, что делать, и, как делать."
    ilya standart "Я понял, у вас на всё будут отговорки."
    return
label choice_Ilyx_norm:
    admin normal "Новые проблемы?"
    ilya ydiv "Мне не тот доклад распечатали, и из-за этого меня чуть не уволили. Вы точно тот скинули секретарю. "
    admin ponimat "Не может быть. Я скинул тот доклад, который вы мне назвали. Странно, конечно, что вам понадобился доклад годичной давности. "
    ilya scary "Как годичной? Ему максимум неделя."
    admin normal "Ну вы же сказали вам нужен был последний, а не первый."
    ilya scaryy "..."
    return