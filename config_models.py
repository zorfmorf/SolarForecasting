import config as cfg

################### Models ###########################
# Example for configuration
# model_var = {
#     'name': 'Name for identification and plotting',
#     'city': 'city_of_dataset',
#     'type': 'network_type: lstm, convolutional, conv_lstm, lstm_conv, naive',
#     'fields': 'list_of_features',
#     'train_bool': 'train_network_bool',
#     'number': 'String number_of_model if same city and type but different weights',
#     'plotting': {'color': 'b/g/r/c/m/y/k/w', 'marker': 'o/v/^/</>/s/*/x/d', 'linestyle': '-/--/-./:'},
#     'baseline': {'type'}
# }

# almeria = {
#         'name': 'Almeria', 'city': 'almeria', 'type': 'lstm',
#         'fields': cfg.fields['usedfields'],
#         'train_bool': True,
#         'plotting': {'marker': '*', 'linestyle': '-'},
#         # 'baseline': {'type': 'naive'},
# }
# almeria1 = {
#     'name': 'Almeria_wo_MSI_DayAhead', 'city': 'almeria', 'type': 'lstm', 'number': '1',
#     'fields': cfg.fields['usedfields1'],
#     'train_bool': True,
#     # 'baseline': {'type': 'naive'},
#     'plotting': {'marker': '^', 'linestyle': '-'}
# }
model_alg = {'name': 'bordeaux'}
model_alg['city'] = model_alg['name']
model_alg['type'] = 'lstm'
model_alg['fields'] = cfg.fields['usedfields']
model_alg['train_bool'] = True
model_alg['plotting'] = {'marker': '*', 'linestyle': '-'}

model_w_sin = model_alg.copy()
model_w_sin['name'] += '_w_sin'
model_w_sin['fields'] = cfg.fields['usedfields_w_sin']

model_w_kart = model_alg.copy()
model_w_kart['name'] += '_w_kart'
model_w_kart['fields'] = cfg.fields['usedfields_kart']

model_o_w = model_alg.copy()
model_o_w['name'] += '_o_w'
model_o_w['fields'] = cfg.fields['usedfields_ohne_wind']

model_weekday = model_alg.copy()
model_weekday['name'] += '_weekday'
model_weekday['fields'] = cfg.fields['usedfields_weekday']

model_weekday_sin = model_alg.copy()
model_weekday_sin['name'] += '_weekday_sin'
model_weekday_sin['fields'] = cfg.fields['usedfields_weekday_sin']

model_weekday_kart = model_alg.copy()
model_weekday_kart['name'] += '_weekday_kart'
model_weekday_kart['fields'] = cfg.fields['usedfields_weekday_kart']

#models = [model_alg]
models = [model_alg, model_o_w, model_weekday, model_w_sin, model_w_kart, model_weekday_sin, model_weekday_kart]

