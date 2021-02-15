# -*- coding: utf-8 -*-
***REMOVED***
Original file is located at
    https://colab.research.google.com/drive/1xqkvuNDg0Opk-aZpicTVPNY4wUdC7Y7v

# Parameters
***REMOVED***
***REMOVED***
import pathlib
raw_data_path = os.path.join(pathlib.Path(__file__).parent, 'training.csv')
destination_folder = pathlib.Path(__file__).parent

train_test_ratio = 0.10
train_valid_ratio = 0.80

first_n_words = 500

***REMOVED***# Libraries***REMOVED***

import pandas as pd
from sklearn.model_selection import train_test_split

***REMOVED***# Preprocessing***REMOVED***

def trim_string(x):
    str(x)
    x = x.split(maxsplit=first_n_words)
    x = ' '.join(x[:first_n_words])

    return x

# Read raw data
df_raw = pd.read_csv(raw_data_path)
# Prepare columns
df_raw['label'] = (df_raw['label']).astype('int')
df_raw['titletext'] = df_raw['Title'] + ". " + df_raw['Abstract']
df_raw = df_raw.reindex(columns=['label', 'Title', 'Abstract', 'titletext'])

# Drop rows with empty text
df_raw.drop( df_raw[df_raw.titletext.str.len() < 5].index, inplace=True)
df_raw = df_raw.dropna(how='any')
# Trim text and titletext to first_n_words
df_raw['Abstract'] = df_raw['Abstract'].apply(trim_string)
df_raw['titletext'] = df_raw['titletext'].apply(trim_string) 

# Split according to label
df_real = df_raw[df_raw['label'] == 0]
df_fake = df_raw[df_raw['label'] == 1]

# Train-test split
df_real_full_train, df_real_test = train_test_split(df_real, train_size = train_test_ratio, random_state = 1)
df_fake_full_train, df_fake_test = train_test_split(df_fake, train_size = train_test_ratio, random_state = 1)

# Train-valid split
df_real_train, df_real_valid = train_test_split(df_real_full_train, train_size = train_valid_ratio, random_state = 1)
df_fake_train, df_fake_valid = train_test_split(df_fake_full_train, train_size = train_valid_ratio, random_state = 1)

# Concatenate splits of different labels
df_train = pd.concat([df_real_train, df_fake_train], ignore_index=True, sort=False)
df_valid = pd.concat([df_real_valid, df_fake_valid], ignore_index=True, sort=False)
df_test = pd.concat([df_real_test, df_fake_test], ignore_index=True, sort=False)

# Write preprocessed data
df_train.to_csv(os.path.join(destination_folder , 'train.csv'), index=False)
df_valid.to_csv(os.path.join(destination_folder , 'valid.csv'), index=False)
df_test.to_csv(os.path.join(destination_folder ,'test.csv'), index=False)

