
from loader import dp, types, keyboard, bot, start_state, welcome_message, isChat, channel_subscribe, logging, FSMContext, channels_auto_join, connect_bd
from filters.filter_commands import isUser

@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest, state: FSMContext):
  chat, user_id = update.chat.id, update.from_user.id

  user, channels = await connect_bd.mongo_conn.db.users.find_one({'user_id': str(user_id)}), []
  if user:
    if user.get('necessary_channel'):
      channels.append(user['necessary_channel']['id'])

  if str(chat) in channels_auto_join or str(chat) in channels:
    try:
      await update.approve()
      await bot.send_message(user_id, "Спасибо за подписку на канал Работа,найдись! (https://t.me/+vZP28DCNCeAyYzFi)\n\nДля доступа ко всем функциям бота нажми  /start\n\n/start\n/start", parse_mode='html')
      await start_state.select_neiro.set()
    except Exception as e:
      logging.error("Exception occurred", exc_info=True)