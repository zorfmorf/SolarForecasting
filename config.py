"""
This config file should hold all static parameters - everything is changed here (except from the networks structure)
"""
import pandas as pd

################### PARAMETER for Preprocessing ###########################
data = dict(
        # datalist = ['data2014','data2015','data2016'],
        datalist=['data'],
        filterbool=False,
        frequency=1,  # values per hour
        minmaxscale=True,
        sequencelength=24,  # 24h
        num_of_samples=64,
        batch_size=32,
        test_data_size=8760,  # 24*365=8760,
        train_data_perc=0.8,
)
usedfields = ['Global Irradiation', 'Max incomming solar irradiation',
                    'Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Rainfall',
                    'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind Direction']
#usedfields = ['Global Irradiation',
#                    'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind Direction']
usedfields_w_sin = usedfields.copy()
usedfields_w_sin.append('Wind sin')
usedfields_w_sin.append('Wind cos')

usedfields_kart = usedfields.copy()
usedfields_kart.append('Wind x')
usedfields_kart.append('Wind y')

usedfields_ohne_wind = usedfields.copy()
usedfields_ohne_wind.remove('Wind Direction')

usedfields_weekday = usedfields_ohne_wind.copy()
usedfields_weekday.append('weekday')

usedfields_weekday_sin = usedfields_ohne_wind.copy()
usedfields_weekday_sin.append('weekday sin')
usedfields_weekday_sin.append('weekday cos')

usedfields_weekday_kart = usedfields_ohne_wind.copy()
usedfields_weekday_kart.append('weekday x')
usedfields_weekday_kart.append('weekday y')

fields = dict(
        loadedfields=['Date', 'Temperature', 'Global Irradiation', 'Max incomming solar irradiation',
                      'Humidity', 'Pressure', 'Wind Speed', 'Rainfall', 'Wind Direction'],
        # loadedfields=['date', 'temp', 'glo', 'maxIncoming', 'difference', 'maxInc_dayAhead',
        #              'humidity', 'pressure', 'wind_speed', 'rainfall'],
        # Input
        # usedfields=['glo', 'maxIncoming', 'maxInc_dayAhead', 'difference',
        #             'temp', 'pressure', 'wind_speed', 'rainfall',
        #             'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        # usedfields1=['glo', 'maxIncoming', 'difference',
        #              'temp', 'pressure', 'wind_speed', 'rainfall',
        #              'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        # usedfields2=['glo',
        #              'temp', 'pressure', 'wind_speed', 'rainfall',
        #              'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        usedfields=usedfields.copy(), # ['Global Irradiation', 'Max incomming solar irradiation',
                    # 'Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Rainfall',
                    # 'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind Direction'],
        usedfields_w_sin=usedfields_w_sin.copy(),#['Global Irradiation', 'Max incomming solar irradiation',
                    #'Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Rainfall',
                    #'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind sin', 'Wind cos'],
        usedfields_kart=usedfields_kart.copy(),#['Global Irradiation', 'Max incomming solar irradiation',
                    # 'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    # 'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind x', 'Wind y'],
        usedfields_ohne_wind=usedfields_ohne_wind.copy(),#['Global Irradiation', 'Max incomming solar irradiation',
                    #'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    #'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        usedfields_sin_kart=['Global Irradiation', 'Max incomming solar irradiation',
                    'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind sin', 'Wind cos', 'Wind x', 'Wind y'],
        usedfields_rad_sin_kart=['Global Irradiation', 'Max incomming solar irradiation',
                    'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind sin', 'Wind cos',
                    'Wind x', 'Wind y', 'Wind Direction'],
        usedfields_rad_sin=['Global Irradiation', 'Max incomming solar irradiation',
                    'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    'Day sin', 'Day cos', 'Year sin', 'Year cos', 'Wind sin', 'Wind cos',
                    'Wind Direction'],
        usedfields_rad_kart=['Global Irradiation', 'Max incomming solar irradiation',
                    'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    'Day sin', 'Day cos', 'Year sin', 'Year cos',
                    'Wind x', 'Wind y', 'Wind Direction'],
        usedfields_weekday=usedfields_weekday.copy(),#['Global Irradiation', 'Max incomming solar irradiation',
                    #'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    #'Day sin', 'Day cos', 'Year sin', 'Year cos', 'weekday'],
        usedfields_weekday_sin=usedfields_weekday_sin.copy(),#['Global Irradiation', 'Max incomming solar irradiation',
                    #'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    #'Day sin', 'Day cos', 'Year sin', 'Year cos', 'weekday sin', 'weekday cos'],
        usedfields_weekday_kart=usedfields_weekday_kart.copy(),#['Global Irradiation', 'Max incomming solar irradiation',
                    #'Temperature', 'Humidity', 'Pressure', 'Rainfall',
                    #'Day sin', 'Day cos', 'Year sin', 'Year cos', 'weekday x', 'weekday y'],
        # usedfields11=['glo', 'maxIncoming', 'maxInc_dayAhead', 'difference',
        #             'temp', 'humidity', 'pressure', 'wind_speed', 'rainfall',
        #             'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        # usedfields1=['glo', 'maxIncoming', 'difference',
        #              'temp', 'humidity', 'pressure', 'wind_speed', 'rainfall',
        #              'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        # usedfields2=['glo',
        #              'temp', 'humidity', 'pressure', 'wind_speed', 'rainfall',
        #              'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        # usedfields3=['glo',
        #              'Day sin', 'Day cos', 'Year sin', 'Year cos'],
        )

# vorhersage parameter
label = 'Temperature'#'Global Irradiation'#'glo'

training = dict(
    max_epochs=200,
    patience=3,
    learning_rate=0.00001,  # standard: 0.001
    lr_lstm=0.0001,
    lr_convolutional=0.0001,
    lr_conv_lstm=0.0001,
    lr_lstm_conv=0.00001,
)

prediction = dict(
              pos=fields['usedfields'].index(label),
              num_predictions=24,
              input_len=24,
              num_features=len(fields['usedfields']),
              label=label,
              )

plotting = dict(
    days=list(map(lambda x: pd.to_datetime(x, format='%d.%m.%y %H:%M'),
                  # ['22.03.20 06:00', '16.02.20 06:00'],
                  # ['22.03.20 08:00', '22.03.20 10:00'],
                  # ['17.06.20 04:00', '17.06.20 06:00', '17.06.20 08:00', '17.06.20 10:00'],
                  # ['18.06.20 04:00', '18.06.20 06:00', '18.06.20 08:00', '18.06.20 10:00'],
                  # ['24.07.20 04:00', '24.07.20 06:00', '24.07.20 08:00', '24.07.20 10:00'],
                  # ['30.07.20 04:00', '30.07.20 06:00', '30.07.20 08:00', '30.07.20 10:00'],
                  # ['22.03.20 04:00', '22.03.20 06:00', '22.03.20 08:00', '22.03.20 10:00'],
                  # ['20.10.20 04:00', '20.10.20 06:00', '20.10.20 08:00', '20.10.20 10:00'],
                  # ['05.01.20 06:00', '21.03.20 06:00', '10.05.20 06:00', '16.06.20 06:00', '15.08.20 06:00']
                  ['16.02.20 06:00', '22.03.20 06:00']
                  ),
              ),
)

errors = dict(
    metric='mae',  # for multi plot
    error_to_excel=False,
)


rmse = dict(
              nob=300,  # number of batches
              )

sarima = dict(
        train_len=30*24,  # 30days * 24h
)
