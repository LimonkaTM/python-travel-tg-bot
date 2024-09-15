from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from loader import bot

from keyboards.about import create_about_kb


router: Router = Router(name='aboutRouter')


@router.callback_query(F.data == 'send_about_tour_msg')
async def send_about_tour_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение с описанием тура
    '''

    text = '💫 <b>Описание путешествия по Архангельску</b> 💫\n\nНаш маршрут берет своё начало в сквере имени Резицкого, после чего мы отправимся в Северодвинск, а затем вернёмся обратно в Архангельск. По пути нас ждут множество интересных и красивых мест, которые мы посетим Северодвинский пляж, музей архитектуры Архангельска и другие захватывающие места.\n\nНаш не простой маршрут расчитан на <b>2</b> дня и выйдет нам, примерно, в <b>13 000 рублей</b>.\n\n📋 <b>Маршрут</b> 📋\n1. Старфудс\n2. Сквер имнеи Резицкого П. Р.\n3. Кафе "Чайка на море"\n4. Отель "Мама Леоне"\n5. Пляж\n6. Кафе "Восточный Бриз"\n7. Отель "Мама Леоне"\n8. Музей "Архангельский пряник"\n9. Non-Stop (прокат велосипедов)\n10. Ресторан "Боброфф"\n11. Вокзал "Архангельск"\n\nПутешественник, а ты точно уже подготовился к увлекательному маршруту на 2 дня?\nЕсли уверен на 100%, не стоит жать ни минуты, по коням 🏇!\n\n<i>P.S. Не переживай, оставлю напоминалку о том, что следует взять с собой: документы, деньги, теплая одежда, зонт или дождевик, хорошее настроение.</i>'

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/about_map.jpg'),
                            caption=text)

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_about_kb())

    return None
