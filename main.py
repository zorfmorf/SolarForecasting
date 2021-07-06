import data_preprocessing.preprocessing as pp
from data_preprocessing.WindowGenerator import WindowGenerator
import models.train_model as tm

import config as cfg
import config_models as cfg_mod
import visualization.plotting as plotting
import tensorflow as tf

import os

import numpy as np
import pandas as pd
import pickle
from datetime import date


def main():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    models = prepare_models(cfg_mod.models)
    # print_metrics(models)
    # plotting.multi_plot(cfg_mod.cities, cfg.errors['metric'])
    ################ Plot RMSE ###################
    # plotting.plot_metric(models, 'skewness').show()
    # plotting.plot_metric(models, 'rmse').show()

    datestring = date.today().strftime("%y-%m-%d")
    for model in models:
        current_dir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(current_dir, "results\\" + datestring + "_" + model["name"] + "_" +cfg.label + ".txt")
        file = open(filename, "w")

        for element in model['fields']:
            file.write(element + "\n")

        mae = model['mae']
        for i in range(0, 24):
            file.write(str(mae[i]) + "\n")
        file.close()

    plot = plotting.plot_metric(models, 'mae')
    plot.savefig(datestring + "_" + model["name"] + "_" + cfg.label + '.png')
    plot.show()

def prepare_models(models):
    for model in models:
        #df = pd.read_pickle('data/pickles/' + model['city'] + '.pickle')
        string = 'data/' + model['city'] + '.xlsx'
        df = pd.read_excel(string, sheet_name='Tabelle1')
        if 'Wind sin' in model['fields']:
            df = pp.change_wind_sin(df)

        if 'Wind x' in model['fields']:
            df = pp.change_wind_kart(df)

        if 'weekday' in model['fields'] or 'weekday sin' in model['fields'] or 'weekday x' in model['fields']:
            df = pp.add_weekday(df)

        if 'weekday sin' in model['fields']:
            df = pp.add_weekday_sin(df)

        if 'weekday x' in model['fields']:
            df = pp.add_weekday_kart(df)
        train, val, test, num_features, date_time, column_indices = \
            pp.preprocess(df, model['fields'], city=model['city'], time=True)

        model['train'] = train
        model['val'] = val
        model['test'] = test
        model['test_datetime'] = date_time
        model['num_features'] = num_features
        model['column_indices'] = column_indices

        with open('./saver/outputs/scaler/output_scaler_' + model['city'] + '.pckl', 'rb') as file_scaler:
            model['scaler'] = pickle.load(file_scaler)

        model['window'] = WindowGenerator(input_width=cfg.prediction['input_len'],
                                          label_width=cfg.prediction['num_predictions'],
                                          train_df=model['train'], val_df=model['val'], test_df=model['test'],
                                          shift=cfg.prediction['num_predictions'],
                                          label_columns=[cfg.label],
                                          )
        mae = np.zeros(24)
        iterate = 30
        for i in range(iterate):
            print(i+1)
            model['model'] = tm.build_model(tm.choose_model(model), model['window'],
                                        './checkpoints/' + model['city'] + '/' + model['type'] + '_' +
                                        model['city'] + model.get('number', ''),
                                        train=model['train_bool'])
            if model.get('baseline'):
                model['baseline']['model'] = tm.build_model(tm.choose_model(model['baseline']), model['window'],
                                                        './checkpoints/' + model['city'] + '/' + model['type'] + '_' +
                                                        model['city'] + model.get('number', ''),
                                                        train=model['train_bool'])
                model['baseline']['rmse'], model['baseline']['mae'], model['baseline']['skewness'] = \
                    model['window'].get_metrics(model['baseline']['model'], model['scaler'], model['city'])
            model['rmse'], model['mae'], model['skewness'] = \
                model['window'].get_metrics(model['model'], model['scaler'], model['city'])
            mae = model['window'].update_mae(model, mae)
        mae = mae / iterate
        model['mae'] = mae
    return models


def print_metrics(models):
    rmse_baseline = None
    mae_baseline = None
    for model in models:
        if model.get('baseline'):
            rmse_baseline = sum(model['baseline']['rmse']) / 24
            mae_baseline = sum(model['baseline']['mae']) / 24
    for model in models:
        rmse_model = sum(model['rmse'])/24
        mae_model = sum(model['mae'])/24
        print(model['name'] + ': ' + model['city'].capitalize() + ' ' + model['type'])
        if rmse_baseline is not None:
            print('Percentage RMSE: ', rmse_model/rmse_baseline)
            print('Percentage MAE: ', mae_model/mae_baseline)
        else:
            print('No Baseline defined, can not give RMSE Percentage!')
        print('Total RMSE: ', rmse_model)
        print('Total MAE: ', mae_model)


if __name__ == '__main__':
    main()
