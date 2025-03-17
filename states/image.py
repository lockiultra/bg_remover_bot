from aiogram.fsm.state import StatesGroup, State


class ImageStates(StatesGroup):
    waiting_for_main_photo = State()
    waiting_for_background_choice = State()
    waiting_for_background_photo = State()
