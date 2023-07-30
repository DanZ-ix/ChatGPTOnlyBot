
from loader import dp, types, keyboard, bot, start_state, welcome_message, isChat, channel_subscribe, logging, FSMContext, channels_auto_join, connect_bd
from filters.filter_commands import isUser
from aiogram.types import InputFile


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest, state: FSMContext):
  chat, user_id = update.chat.id, update.from_user.id
  print("handled")
  user, channels = await connect_bd.mongo_conn.db.users.find_one({'user_id': str(user_id)}), []
  if user:
    if user.get('necessary_channel'):
      channels.append(user['necessary_channel']['id'])

  if str(chat) in channels_auto_join or str(chat) in channels:
    try:
      await update.approve()
      photo = InputFile("send_auto_join.png")
      m = await keyboard.auto_join_keys()
      await bot.send_photo(user_id, photo, caption="Вы молодец")
      await bot.send_message(user_id, "Вот, поробуйте нейросеть", reply_markup=m)
      print("Joined")
      #await bot.send_message(user_id, "Спасибо за подписку на канал Работа,найдись! (https://t.me/+vZP28DCNCeAyYzFi)\n\nДля доступа ко всем функциям бота нажми  /start\n\n/start\n/start", parse_mode='html')
      await start_state.select_neiro.set()
    except Exception as e:
      print("Exception occurred")
      logging.error("Exception occurred", exc_info=True)