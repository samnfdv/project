import logging
import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from prediction import prediction
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot_token = os.getenv('BOT_TOKEN')
bot = Bot(token=bot_token)
dp = Dispatcher()
user_data = {}


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Да",
        callback_data='Да'),
        types.InlineKeyboardButton(
            text="Нет",
            callback_data='Нет')
    )

    await message.answer(
        text=f'Привет, {message.from_user.full_name}!\nЯ телеграм бот, созданный в рамках проекта _Прогнозирование'
             f' степени тяжести заболевания у больных раком лёгких на основе синтезированных данных_, чтобы помочь '
             f'врачам в борьбе с раком лёгких.\nЕсли вы болеете раком лёгких или ваш лечащий врач имеет подозрение, '
             f'что вы больны раком лёгких, то прошу вас принять участие в проекте, ответить на следующие 23 вопроса'
             f' и узнать результат прогнозирования степени тяжести заболевания рака лёгких на основе ваших ответов!'
             f' \nВы готовы начать?',
        reply_markup=builder.as_markup(),
        parse_mode='Markdown')


@dp.callback_query(F.data == 'Нет')
async def negativ_answer(message: types.CallbackQuery):
    await message.message.answer(text=f'Досвидания {message.from_user.full_name}')


@dp.callback_query(F.data == 'Да')
async def positiv_answer(message: types.CallbackQuery):
    user_id = message.from_user.id
    user_data[user_id] = {}
    builder = InlineKeyboardBuilder()
    g = ['Мужской', 'Женский']
    for j, i in enumerate(g):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data=i + str(g.index(i) + 1)),
        )
    await message.message.answer(
        text="Выбирете одно из значений соответствующих вашему полу",
        reply_markup=builder.as_markup()
    )



@dp.callback_query(lambda x: x.data in ['Мужской1', 'Женский2'])
async def questions3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['gender'] = int(callback.data[-1])
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer3_' + str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих частоте курения вами по _7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6] == '3')
async def question(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer3'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in [[14, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90]]:
        builder.add(types.InlineKeyboardButton(
            text=f"{i[0]}–{i[-1]}",
            callback_data='age1_' + str(i[0]) + '-' + str(i[1])),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих диапазону вашего возраста",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '14')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(14, 21):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '21')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(21, 31):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '31')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(31, 41):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '41')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(41, 51):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '51')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(51, 61):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '61')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(61, 71):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '71')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(71, 81):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '71')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(71, 81):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[5:7] == '81')
async def question56(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(81, 91):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='age2__'+str(i)),
        )
    builder.adjust(4)
    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему возрасту",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[3] == '2')
async def questions4(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer3-1'] = callback.data[-2:]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer4_'+str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню воздействия на вас загрязнённого воздуха по "
             "_7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6] == '4')
async def questions5(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer4'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer5_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих частоте употребления вами алкоголя по _8 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6] == '5')
async def questions6(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer5'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer6_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашей аллергии на пыль по _8 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6] == '6')
async def questions7(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer6'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer7_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню ваших профессиональных рисков связанных с дыханием по "
             "_8 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6] == '7')
async def questions8(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer7'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer8_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашему генетическому риску связанному с раком по "
             "_7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6] == '8')
async def questions10(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer9'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer10_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих вашей степени тяжести хронических заболеваний лёгких "
             "_по 7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '10')
async def questions11(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer10'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer11_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню сбалансированности вашей диеты по _7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '11')
async def questions12(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer11'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer12_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего ожирения по _7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '12')
async def questions13(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer12'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer13_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего пасивного курения по _8 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '13')
async def questions14(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer13'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer14_' + str(i)),
        )
    builder.adjust(3)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашей боли в груди по _9 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '14')
async def questions15(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer14'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer15_' + str(i)),
        )
    builder.adjust(3)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего кашля с кровью по _9 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '15')
async def questions16(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer15'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer16_' + str(i)),
        )
    builder.adjust(3)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашей усталости по _9 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '16')
async def questions17(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer16'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer17_' + str(i)),
        )
    builder.adjust(3)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашей потери веса по _9 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '17')
async def questions18(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer17'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer18_' + str(i)),
        )
    builder.adjust(3)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашей одышки по _9 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '18')
async def questions19(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer18'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer19_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего хрипения  по _8 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '19')
async def questions20(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer19'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer20_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего затруднения в глотании  по _8 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '20')
async def questions21(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer20'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer21_' + str(i)),
        )
    builder.adjust(3)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего скручивания ногтей  по _9 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '21')
async def questions22(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer21'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer22_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашей частоты заболеваимости простудами"
             " _по 7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '22')
async def questions23(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer22'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer23_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего сухого кашля"
             " _по 7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '23')
async def questions24(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer23'] = callback.data[-1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
            text=f"{i}",
            callback_data='answer24_' + str(i)),
        )
    builder.adjust(4)

    await callback.message.answer(
        text="Выбирете одно из значений соответствующих уровню вашего храпа"
             " _по 7 бальной шкале_",
        reply_markup=builder.as_markup(),
        parse_mode='Markdown'
    )


@dp.callback_query(lambda x: x.data[6:8] == '24')
async def answer_prediction(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]['answer24'] = callback.data[-1]
    print(user_data)
    # Вызвать функцию для прогноза значений, вернет 1, 2 или 3
    pred = prediction(user_data, user_id)
    if pred == 1:
        await callback.message.answer(
            text='Тестирование показало, что вы находитесь в группе с низкой степенью тяжести, несмотря на это '
                 'рекомендую вам обратиться к врачу, если вы этого ещё не сделали, и предпринять меры для профилактики'
                 ' рака на которые вы способны.'
                 '\nБлагодарю вас, за то что приняли участие в этом проекте!'
        )
    elif pred == 2:
        await callback.message.answer(
            text='Тестирование показало, что вы находитесь в группе со средней степенью тяжести, поэтому рекомендую вам'
                 ' обратиться к врачу, если вы этого ещё не сделали, и предпринять меры для профилактики'
                 ' рака на которые вы способны.'
                 '\nБлагодарю вас, за то что приняли участие в этом проекте!'
        )
    else:
        await callback.message.answer(
            text='Тестирование показало, что вы находитесь в группе с высокой степенью тяжести, поэтому рекрмендую вам'
                 ' незамедлительно обратиться к врачу, если вы этого ещё не сделали, и предпринять меры'
                 ' для профилактики рака на которые вы способны.'
                 '\nБлагодарю вас, за то что приняли участие в этом проекте!'
        )


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
