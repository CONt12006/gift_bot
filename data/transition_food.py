from keyboards.main_keyboard import main_inline_keyboard
from keyboards.harmful_keyboard import harmful_main_inline_keyboard, snack_main_inline_keyboard
from keyboards.sweet_keyboard import sweet_main_inline_keyboard, chocolate_main_inline_keyboard


transitions = {
    "mikbtn_3": sweet_main_inline_keyboard,
    "smik_1": chocolate_main_inline_keyboard,
    "mikbtn_4": harmful_main_inline_keyboard,
    "harmful_mik_2": snack_main_inline_keyboard
}