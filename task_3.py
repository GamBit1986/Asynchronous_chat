import yaml


data = {'Наименование': ['сосиски', 'молоко', 'яйца', 'мороженое'],
        'Порции': 15,
        'Стоимости': {'сосиски': '2€',
                      'молоко': '1€',
                      'яйца': '3€',
                      'мороженое': '4€'}
        }

with open('niyam.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=True
              )

with open("niyam.yaml", 'r', encoding='utf-8') as f_out:
    data_load = yaml.load(f_out, Loader=yaml.SafeLoader)

print(data == data_load)
