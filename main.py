import vk

INTRO_TEXT = 'Хай, как дела?) Ты как сюда попал?!. ' \
    'Чтобы выйти, скажи "Хватит".'
POST_TEXT = 'Хорошо, я запостил фразу Hello World! на твоей стене'
# токен прилоги - d0e78ffb7185866fbe6ccdc608d25b71b74aaf32e10c545e64e750c71318153ee759303586b2c25427468
session = vk.Session(access_token='3c2198cd0f703b110c6bb8e24000ab1d03bf7f8bdaf3382b8a41cb73cd7da82db5f9150e5d3457dab2d43')
api = vk.API(session, v='5.85')

def remove_char(s):
    result = s.replace("Новый пост ", "")
    return result

def remove_char1(s):
    result = s.replace("новый пост ", "")
    return result

def handler(event, context):
    intents = event.get('request', {}).get('nlu', {}).get('intents', {})
    command = event.get('request', {}).get('command')

    text = INTRO_TEXT
    end_session = 'false'

    if intents.get('exit'):
        text = 'Ну пока) Жду снова!'
        end_session = 'true'
    elif intents.get('help'):
        text = INTRO_TEXT
    elif intents.get('vkpost'):
        messagepost1 = remove_char(command)
        messagepost = remove_char1(messagepost1)
        text = messagepost
        api.wall.post(message = messagepost)
    elif command:
        text = 'Не поняла тебя. Для выхода, скажите "Хватит".'

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': end_session
        },
    }
