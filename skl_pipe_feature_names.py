
########### KEEP TRACK OF FEATURE LABELS IN SKLEARN PIPELINES ###############


# From this one answer on SO: https://stackoverflow.com/questions/57528350/can-you-consistently-keep-track-of-column-labels-using-sklearns-transformer-api/57534118#57534118
# This one answer justifies all of SO's existence in my opinion. 
# What a beautiful answer.

# First we make the pipeline

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.feature_extraction.text import _VectorizerMixin
from sklearn.feature_selection._base import SelectorMixin
from sklearn.feature_selection import SelectKBest
from sklearn.feature_extraction.text import CountVectorizer

train = pd.DataFrame({'age': [23,12, 12, np.nan],
                      'Gender': ['M','F', np.nan, 'F'],
                      'income': ['high','low','low','medium'],
                      'sales': [10000, 100020, 110000, 100],
                      'foo' : [1,0,0,1],
                      'text': ['I will test this',
                               'need to write more sentence',
                               'want to keep it simple',
                               'hope you got that these sentences are junk'],
                      'y': [0,1,1,1]})
numeric_columns = ['age']
cat_columns     = ['Gender','income']

numeric_pipeline = make_pipeline(SimpleImputer(strategy='median'), StandardScaler())
cat_pipeline     = make_pipeline(SimpleImputer(strategy='most_frequent'), OneHotEncoder())
text_pipeline = make_pipeline(CountVectorizer(), SelectKBest(k=5))

transformers = [
('num', numeric_pipeline, numeric_columns),
('cat', cat_pipeline, cat_columns),
('text', text_pipeline, 'text'),
('simple_transformer', MinMaxScaler(), ['sales']),
]

combined_pipe = ColumnTransformer(transformers, remainder='passthrough')

transformed_data = combined_pipe.fit_transform(train.drop('y',1), train['y'])


# Now we write functions to extract column names

def get_feature_out(estimator, feature_in):

    '''
    Function to get feature names from some type of estimator that's
    part of the ColumnTransformer Pipeline. 
    '''

    if hasattr(estimator,'get_feature_names'):
        if isinstance(estimator, _VectorizerMixin):
            # handling all vectorizers
            return [f'vec_{f}' \
                for f in estimator.get_feature_names()]
        else:
            return estimator.get_feature_names(feature_in)
    elif isinstance(estimator, SelectorMixin):
        return np.array(feature_in)[estimator.get_support()]
    else:
        return feature_in


def get_ct_feature_names(ct):

    '''
    Function to get feature names from pipelines inside a given ColumnTransfomer

    - handles all estimators, pipelines inside ColumnTransfomer
    - doesn't work when remainder =='passthrough', which requires the input column names.

    '''


    output_features = []

    for name, estimator, features in ct.transformers_:
        if name!='remainder':
            if isinstance(estimator, Pipeline):
                current_features = features
                for step in estimator:
                    current_features = get_feature_out(step, current_features)
                features_out = current_features
            else:
                features_out = get_feature_out(estimator, features)
            output_features.extend(features_out)
        elif estimator=='passthrough':
            output_features.extend(ct._feature_names_in[features])
                
    return output_features


pd.DataFrame(transformed_data, 
             columns=get_ct_feature_names(combined_pipe))


###############################################

# Another cool answer for a slightly different question: How do you get feature names after you do 
# feature selection as part of your pipeline???

# Pipeline and Model Setup
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn import feature_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import numpy as np

X = ['I am a sentence', 'an example']
Y = [1, 2]
X_dev = ['another sentence']

# classifier
LinearSVC1 = LinearSVC(tol=1e-4,  C = 0.10000000000000001)
f5 = feature_selection.RFE(estimator=LinearSVC1, n_features_to_select=500, step=1)

pipeline = Pipeline([
    ('features', FeatureUnion([
       ('tfidf', TfidfVectorizer(ngram_range=(1, 3), max_features= 4000))])), 
    ('rfe_feature_selection', f5),
    ('clf', LinearSVC1),
    ])

pipeline.fit(X, Y)
y_pred = pipeline.predict(X_dev)

# With named_steps you can access the attributes and methods of the transform object in the pipeline. 
# The RFE attribute support_ (or the method get_support()) will return a boolean mask of the selected features:

support = pipeline.named_steps['rfe_feature_selection'].support_

# Now support is an array, you can use that to efficiently extract the name of your selected features (columns).
# Make sure your feature names are in a numpy array, not a python list.

feature_names = pipeline.named_steps['features'].get_feature_names()
np.array(feature_names)[support]

