from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from state import State
from storage import Measure, Storage
from measurements import Types

state = State()
storage = Storage()


class Handlers:
    def add(client, callback_query: CallbackQuery):
        command = CommandFactory.create(callback_query.data)
        state.add_command(command)
        command.execute(client, callback_query.message)
        
        
    def add_request(client: Client, message: Message):
        message.reply(
            "Выберите тип показаний",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Газ 🔥",
                        callback_data="add_gas"
                    ),
                    InlineKeyboardButton(
                        "Вода 🚰",
                        callback_data="add_water"
                    ),
                    InlineKeyboardButton(
                        "Свет 💡",
                        callback_data="add_electro"
                    ),
                ]
            ])
        )

    def last(client: Client, message: Message):
        last = storage.get_last_measure()
        message.reply(
            """Ваши последние показания за %s:\n%s\t%s""" 
            % (last.date.strftime('%d.%m.%Y'), Types.get_label(last.type), last.value)
        )


    def calc(client: Client, message: Message):
        message.reply(
            "Расход за месяц:"
        )


    def read_input(client: Client, message: Message):
        command = state.get_last_command()
        if not command:
            message.reply("Выберите команду из меню")
            return
        command.execute(client, message)
        

       
class CommandFactory:
    def create(data: str):
        commands_mnemo = {
            "add_gas": AddGasCommand,
            "add_water": AddWaterCommand,
            "add_electro": AddWaterCommand
        }
        return commands_mnemo[data]()


class AddGasCommand:
    STATE_DEFAULT = 0
    STATE_INPUT = 1
    STATE_COMPLETE = 2

    def __init__(self) -> None:
        self.measure = Measure(Types.TYPE_GAS)
        self.state = self.STATE_DEFAULT


    def execute(self, client: Client, message: Message):
        if self.state == self.STATE_INPUT:
            self.save(client, message)
            return
        self.read_input(client, message)


    def read_input(self, client: Client, message: Message):
        self.state = self.STATE_INPUT
        message.reply(
            "Введите показания газа"
        )


    def save(self, client: Client, message: Message):
        self.measure.value = message.text
        storage.add_measure(self.measure)
        self.state = self.STATE_COMPLETE
        message.reply(
            "Сохранено"
        )


class AddWaterCommand:
    STATE_DEFAULT = 0
    STATE_INPUT = 1
    STATE_COMPLETE = 2

    def __init__(self) -> None:
        self.measure = Measure(Types.TYPE_WATER)
        self.state = self.STATE_DEFAULT


    def execute(self, client: Client, message: Message):
        if self.state == self.STATE_INPUT:
            self.save(client, message)
            return
        self.read_input(client, message)


    def read_input(self, client: Client, message: Message):
        self.state = self.STATE_INPUT
        message.reply(
            "Введите показания воды"
        )


    def save(self, client: Client, message: Message):
        self.measure.value = message.text
        storage.add_measure(self.measure)
        self.state = self.STATE_COMPLETE
        message.reply(
            "Сохранено"
        )


class AddElectroCommand:
    STATE_DEFAULT = 0
    STATE_INPUT = 1
    STATE_COMPLETE = 2

    def __init__(self) -> None:
        self.measure = Measure(Types.TYPE_ELECTRO)
        self.state = self.STATE_DEFAULT


    def execute(self, client: Client, message: Message):
        if self.state == self.STATE_INPUT:
            self.save(client, message)
            return
        self.read_input(client, message)


    def read_input(self, client: Client, message: Message):
        self.state = self.STATE_INPUT
        message.reply(
            "Введите показания электроэнергии"
        )


    def save(self, client: Client, message: Message):
        self.measure.value = message.text
        storage.add_measure(self.measure)
        self.state = self.STATE_COMPLETE
        message.reply(
            "Сохранено"
        )