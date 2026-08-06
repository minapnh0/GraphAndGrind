def kettle_has_water():
    return True


def fill_kettle_with_water():
    print("Filling kettle with water")


def plug_in_kettle():
    print("Plugging in kettle")


def boil_water():
    print("Boiling water")


def is_cup_clean():
    return True


def clean_cup():
    print("Cleaning cup")


def add_tea_leaves_to_cup():
    print("Adding tea leaves to cup")


def pour_boiled_water_into_cup():
    print("Pouring boiled water into cup")


def add_milk_to_cup():
    print("Adding milk to cup")


def add_sugar_to_cup():
    print("Adding sugar to cup")


def serve_chai():
    print("Serving chai")


def make_chai():
    if not kettle_has_water():
        fill_kettle_with_water()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        clean_cup()
    add_tea_leaves_to_cup()
    pour_boiled_water_into_cup()
    add_milk_to_cup()
    add_sugar_to_cup()
    serve_chai()
    return "Chai is ready!"


print(make_chai())
    
    