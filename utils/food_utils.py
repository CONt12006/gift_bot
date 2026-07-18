from data.food import FOODS

def get_photo_path(food_name: str) -> str | None:
    for item in FOODS.values():
        if item.get("name") == food_name:
            path = item.get("photo", "").strip()
            return path if path else None
    return None