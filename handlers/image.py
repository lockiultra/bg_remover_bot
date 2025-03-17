import os

from aiogram import types, Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from services.background import process_image, process_image_with_custom_background
from keyboards.image import get_mode_choose_keyboard
from states.image import ImageStates

router = Router()


@router.message(StateFilter(None), F.photo)
async def main_photo_handler(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(ImageStates.waiting_for_main_photo)

    user_folder = f'downloads/{message.from_user.id}'
    os.makedirs(user_folder, exist_ok=True)
    file_id = message.photo[-1].file_id
    file_path = os.path.join(user_folder, f'{file_id}.png')

    await bot.download(message.photo[-1], destination=file_path)

    await state.update_data(main_photo_path=file_path)

    keyboard = get_mode_choose_keyboard()
    await message.answer("Выберите тип фона для изображения:", reply_markup=keyboard)
    await state.set_state(ImageStates.waiting_for_background_choice)


@router.message(ImageStates.waiting_for_background_choice)
async def background_choice_handler(message: types.Message, state: FSMContext):
    choice = message.text
    data = await state.get_data()
    main_photo_path = data.get("main_photo_path")
    if choice == "Однотонный фон":
        res_path = process_image(main_photo_path, color=(255, 255, 255))
        await state.clear()
        with open(res_path, 'rb') as f:
            await message.answer_photo(types.BufferedInputFile(f.read(), filename="result.png"))
    elif choice == "Своя картинка":
        await message.answer("Отправьте изображение, которое хотите использовать в качестве фона.")
        await state.set_state(ImageStates.waiting_for_background_photo)
    else:
        await message.answer("Неверный выбор. Пожалуйста, выберите один из предложенных вариантов.")


@router.message(ImageStates.waiting_for_background_photo, F.photo)
async def custom_background_photo_handler(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    main_photo_path = data.get("main_photo_path")
    if not main_photo_path:
        await message.answer("Основное изображение не найдено. Пожалуйста, начните заново.")
        await state.clear()
        return
    user_folder = f'downloads/{message.from_user.id}'
    os.makedirs(user_folder, exist_ok=True)
    file_id = message.photo[-1].file_id
    background_path = os.path.join(user_folder, f'bg_{file_id}.png')
    await bot.download(message.photo[-1], destination=background_path)

    res_path = process_image_with_custom_background(main_photo_path, background_path)
    await state.clear()
    with open(res_path, 'rb') as f:
        await message.answer_photo(types.BufferedInputFile(f.read(), filename="result_custom.png"))