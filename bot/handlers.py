from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext


class User_Registor(StatesGroup):
    name = State()
    password = State()

test_hello = '''Доброво врермни соток!
этот бот для проверки IMEI устройств

пройдите регистрацию:
    '''
router = Router()

@router.message(Command("start"))
async def start_message(mes: Message, state: FSMContext):
    await mes.answer(test_hello)
    await state.set_state(User_Registor.name)
    await mes.answer("Введите имя:")

@router.message(User_Registor.name)
async def name(mes: Message, state: FSMContext):
    await state.update_data(name=mes.text)
    await state.set_state(User_Registor.password)
    await mes.answer("Придумайте пороль (не больше 10 символов):")

@router.message(User_Registor.password)
async def password(mes: Message, state: FSMContext):
    if len(mes.text) > 10:
        await mes.answer("Пароль больше 10 символов")
    else:
        await state.update_data(password=mes.text)
        user_data = await state.get_data()