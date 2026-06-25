from keyboards.berries_keyboard import berries_main_inline_keyboard
from keyboards.fruits_keyboard import fruits_main_inline_keyboard
from keyboards.harmful_keyboard import harmful_main_inline_keyboard, popcorn_main_inline_keyboard, fast_food_main_inline_keyboard, chips_main_inline_keyboard
from keyboards.hearty_keyboard import hearty_main_inline_keyboard
from keyboards.main_keyboard import main_inline_keyboard
from keyboards.sweet_keyboard import bakery_main_inline_keyboard, Cake_main_inline_keyboard, popular_chocolate_main_inline_keyboard, Ritter_sport_chocolate_main_inline_keyboard, Alpen_Gold_chocolate_main_inline_keyboard, sweet_main_inline_keyboard, milka_chocolate_main_inline_keyboard, Kinder_chocolate_main_inline_keyboard


end_food = {
    "mikbtn_2": {
        "name": ["Суши", "Рамен", "Хинкали", "Шаурма", "Пицца"],
        "emoji": ["🍣", "🍜", "🥟", "🌯", "🍕"],
        "photo": ["photo/hearty_food/photo_1.jpg", "photo/hearty_food/photo_2.jpg", "photo/hearty_food/photo_3.jpg", "photo/hearty_food/photo_4.jpg", "photo/hearty_food/photo_5.jpg"],
        "keyboard": hearty_main_inline_keyboard
    },

    "mikbtn_6": {
        "name": ["Мандарины", "Апельсины", "Бананы", "Персики", "Абрикосы", "Ананас"],
        "emoji": ["🍊", "🍊", "🍌", "🍑", "", "🍍"],
        "photo": ["photo/fruits/photo_1.jpg", "photo/fruits/photo_2.jpg", "photo/fruits/photo_3.jpg", "photo/fruits/photo_4.jpg", "photo/fruits/photo_5.jpg", "photo/fruits/photo_6.jpg"],
        "keyboard": fruits_main_inline_keyboard
    },

    "mikbtn_5": {
        "name": ["Клубника", "Голубика", "Малина", "Виноград", "Вишня", "Арбуз"],
        "emoji": ["🍓", "🫐", "", "🍇", "🍒", "🍉"],
        "photo": ["photo/berries/photo_1.jpg", "photo/berries/photo_2.jpg", "photo/berries/photo_3.jpg", "photo/berries/photo_4.jpg", "photo/berries/photo_5.jpg", "photo/berries/photo_6.jpg"],
        "keyboard": berries_main_inline_keyboard
    },

    "harmful_mik_1": {
        "name": ["Снэк бокс", "Картошка фри", "Нагетсы"],
        "emoji": ["", "", ""],
        "photo": ["photo/fast_food/fast_food/photo_1.jpg", "photo/fast_food/fast_food/photo_2.jpg", "photo/fast_food/fast_food/photo_3.jpg"],
        "keyboard": fast_food_main_inline_keyboard
    },

    "snack_mik_1": {
        "name": ["Lay`s из печи с лисичками", "Lay`s из печи с нежный сыр с зеленью", "Начос с сыром"],
        "emoji": ["", "", ""],
        "photo": ["photo/fast_food/snack/photo_1.jpg", "photo/fast_food/snack/photo_2.jpg", "photo/fast_food/snack/photo_3.jpg"],
        "keyboard": chips_main_inline_keyboard
    },

    "snack_mik_2": {
        "name": ["Сырный", "Карамельный", "С солью"],
        "emoji": ["", "", ""],
        "photo": ["photo/fast_food/snack/photo_4.jpg", "photo/fast_food/snack/photo_5.jpg", "photo/fast_food/snack/photo_6.jpg"],
        "keyboard": popcorn_main_inline_keyboard
    },

    "chocomik_1": {
        "name": ["Bubbles молочный", "Bubbles с бананом", "Bubbles с капучино", "Caramel"],
        "emoji": ["", "", "", ""],
        "photo": ["photo/sweet/milka/photo_1.jpg", "photo/sweet/milka/photo_2.jpg", "photo/sweet/milka/photo_3.jpg", "photo/sweet/milka/photo_4.jpg"],
        "keyboard": milka_chocolate_main_inline_keyboard
    }, 

    "chocomik_2": {
        "name": ["Kinder Bueno", "Kinder Country", "Kinder сюрприз", "Kinder Maxi"],
        "emoji": ["", "", "", ""],
        "photo": ["photo/sweet/Kinder/photo_1.jpg", "photo/sweet/Kinder/photo_2.jpg", "photo/sweet/Kinder/photo_3.jpg", "photo/sweet/Kinder/photo_4.jpg"],
        "keyboard": Kinder_chocolate_main_inline_keyboard
    }, 

    "chocomik_3": {
        "name": ["Max Fun драже-арахис-карамель", "Max Fun с тропическими фруктами и взрывной карамелью", "Max Fun со взрывной карамелью-мармеладом-печеньем", "С Oreo", "С капучино", "Соленый арахис и крекер"],
        "emoji": ["", "", "", "", "", ""],
        "photo": ["photo/sweet/Alpen_gold/photo_1.jpg", "photo/sweet/Kinder/photo_2.jpg", "photo/sweet/Kinder/photo_3.jpg", "photo/sweet/Kinder/photo_4.jpg", "photo/sweet/Alpen_gold/photo_5.jpg", "photo/sweet/Alpen_gold/photo_6.jpg"],
        "keyboard": Alpen_Gold_chocolate_main_inline_keyboard
    }, 

    "chocomik_4": {
        "name": ["Ром, изюм, орех", "Марципан", "Соленая карамель/шоколадный брауни", "Яркая смородина/нежная малина"],
        "emoji": ["", "", "", ""],
        "photo": ["photo/sweet/Ritter_sport/photo_1.jpg", "photo/sweet/Ritter_sport/photo_2.jpg", "photo/sweet/Ritter_sport/photo_3.jpg", "photo/sweet/Ritter_sport/photo_4.jpg"],
        "keyboard": Ritter_sport_chocolate_main_inline_keyboard
    }, 

    "chocomik_5": {
        "name": ["Snikers", "Twix", "Milky Way", "MM`s"],
        "emoji": ["", "", "", ""],
        "photo": ["photo/sweet/popular_chocolate/photo_1.jpg", "photo/sweet/popular_chocolate/photo_2.jpg", "photo/sweet/popular_chocolate/photo_3.jpg", "photo/sweet/popular_chocolate/photo_4.jpg"],
        "keyboard": popular_chocolate_main_inline_keyboard
    }, 

    "smik_2": {
        "name": ["Наполеон", "Медовик"],
        "emoji": ["", ""],
        "photo": ["photo/sweet/Cake/photo_1.jpg", "photo/sweet/Cake/photo_2.jpg"],
        "keyboard": Cake_main_inline_keyboard
    }, 

    "smik_4": {
        "name": ["Круассан с миндалем", "Синнабон", "Вафли Яшкино с карамелью", "Печенье шарлиз", "Маковый рулет"],
        "emoji": ["", "", "", "", ""],
        "photo": ["photo/sweet/Bakery/photo_1.jpg", "photo/sweet/Bakery/photo_2.jpg", "photo/sweet/Bakery/photo_3.jpg", "photo/sweet/Bakery/photo_4.jpg", "photo/sweet/Bakery/photo_5.jpg"],
        "keyboard": bakery_main_inline_keyboard
    }, 
}
