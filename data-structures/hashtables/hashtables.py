def castSpell(spell):
    print(spell, '!!!!!!!!!!!!')


user = {
    'age': 17,
    'name': 'Harry',
    'magic': True,
    'cast_spell': castSpell
}


print(user['name'])
print(user['age'])

user['spell'] = 'Expecto Patronum'

user['cast_spell'](user['spell'])

print(user.keys())
print(user.values())
print(user.items())