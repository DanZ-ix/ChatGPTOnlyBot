from configobj import ConfigObj

conf = ConfigObj("data/settings.ini", encoding='UTF8')

bot_token = conf['aio']['bot_token']

server_ip = conf['server']['ip']

dc_host_api = conf['discord']['host']
dc_server_id = conf['discord']['server_id']
dc_channel_id = conf['discord']['channel_id']

gpt_host_api = conf['gpt']['host']
dialog_max_tokens = int(conf['gpt']['limit_dialog_tokens'])

channel_subscribe = conf['subscribe']['channels']
channels_auto_join = conf['subscribe']['channels_auto_join']
attempts_channels = conf['subscribe']['attempts_channels']

account_number = conf['youmoney']['account']

invite_count_max_to_day = 20

channel_in = '<a href="https://t.me/+khaZwmg2C61lNjBi">тест подписки</a>'
channel_in1 = ''

midjorny_error_text = 'Ошибка. Убедитесь, что в вашем запросе не использованы запрещенные слова(мат, жестокость, ненависть и тд). Так же можете обратиться в поддержку: @helper_midjourney'

welcome_message = '<b>Отлично! Давай приступим к работе.</b>\n\nВыбери нейросеть с которой будем взаимодействовать:\n\n<b>ChatGPT</b> - работа с текстом, ответы на любые запросы и собеседник.\n\n<b>Midjoutney</b> - генерация изображений по запросу, редактирование изображений.'