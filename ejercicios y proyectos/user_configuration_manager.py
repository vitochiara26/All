'''Construir un administrador de configuracion de usarios'''

test_settings = {}
tuple_settings = ('tHeMe', 'liGhT')
tuple_settings2 = ('nOtiFIcatIOns' , 'eNAbleD')
tuple_settings3 = ('VolUMe', 'hiGH')
tuple_settings4 = ('sIZe', 'BiG')

tuple_update = ('THEme', 'DArk')
tuple_update2 = ('notiFICATIons' , 'diSABled')
tuple_update3 = ('fONt', 'tIMes neW ROman')
tuple_update4 = ('vOLumE', 'mEDiuM')


test_settings_void = {}

settings = list(test_settings.keys())

def add_setting(dict_settings, tupla_settings):
    '''Crear las claves dentro del diccionario'''
    key, value = tupla_settings
    key = key.lower()
    value = value.lower()

    if key in dict_settings:
        print(f"Setting '{key}' already exists! Cannot add a new setting with this name.\n")
    else:
        dict_settings[key] = value
        print(f"Setting '{key}' added with value '{value}' successfully!\n")



def update_setting(dict_settings, tupla_settings):
    '''Actualizar las claves dentro del diccionario'''
    key, value = tupla_settings
    key = key.lower()
    value = value.lower()
    if key in dict_settings:
        dict_settings[key] = value
        print(f"Setting '{key}' updated to '{value}' successfully)!\n")
    else:
        print(f"Setting '{key}' does not exist! Cannot update a non-existing setting.\n")


def delete_setting(dict_settings,key):
    '''Eliminar una claves dentro del diccionario'''
    key = key.lower()

    if key in dict_settings:
        dict_settings.pop(key)
        print(f"Setting '{key}' deleted successfully!")
    else:
        print("Setting not found!")

def view_settings(dict_settings):
    '''Mostrar todas las claves dentro del diccionario'''
    if not dict_settings:
        print("No settings available.")
    else:
        result = "Current User Settings:"
        for key, value in dict_settings.items():
            result += f"\n{key.capitalize()}: {value}"
        result += "\n"
        print(result)

add_setting(test_settings, tuple_settings)
add_setting(test_settings, tuple_settings2)
add_setting(test_settings, tuple_settings3)
add_setting(test_settings, tuple_settings)
add_setting(test_settings, tuple_settings4)
print()
print(test_settings)


update_setting(test_settings, tuple_update)
update_setting(test_settings, tuple_update2)
update_setting(test_settings, tuple_update3)
print()
print(test_settings)

settings = list(test_settings.keys())
delete_setting(test_settings, settings[3])
print(test_settings)
print()

view_settings(test_settings_void)
print()

print(test_settings)
view_settings(test_settings)

update_setting(test_settings, tuple_update4)
print(test_settings)
view_settings(test_settings)
