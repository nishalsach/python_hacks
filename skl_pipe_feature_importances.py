# Using models trained with sklearn pipelines, to conduct permutation importance for feature evaluation 

# How Permutation importance works: 

# permutation_importance(estimator, X, y, *, scoring=None, n_repeats=5, n_jobs=None, random_state=None, sample_weight=None) 

# The estimator is required to be a fitted estimator. 
# X can be the data set used to train the estimator or a hold-out set. The permutation importance of a feature is calculated as follows: 
# First, a baseline metric, defined by scoring, is evaluated on a (potentially different) dataset defined by the X. Next, a feature column from the validation set is permuted and the metric is evaluated again. 
# The permutation importance is defined to be the difference between the baseline metric and metric from permutating the feature column.


# First we setup the pre-processing
categorical_preprocessing = OneHotEncoder(handle_unknown='ignore')

numeric_preprocessing = Pipeline([
    ('imputer', SimpleImputer(strategy='mean'))
])

# CountVectorizer
text_preprocessing_cv =  Pipeline(steps=[
    ('CV',CountVectorizer())
]) 

# TF-IDF
text_preprocessing_tfidf = Pipeline(steps=[
    ('TF-IDF',TfidfVectorizer())       
]) 

# Now the main pipeline
preprocessing_cv = ColumnTransformer(
    transformers=[
        ('text',text_preprocessing_cv, 'Text'),
        ('category', categorical_preprocessing, categorical_features),
        ('numeric', numeric_preprocessing, numerical_features)
], remainder='passthrough')

clf_nb = Pipeline(steps=[('preprocessor', preprocessing_cv),
                      ('classifier', MultinomialNB())])

# Now the issue with directly applying permutation importance to this pipeline, i.e.: 

from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

result = permutation_importance(clf, X_test, y_test, n_repeats=5, random_state=42, n_jobs=2)
sorted_idx = result.importances_mean.argsort()

plt.boxplot(result.importances[sorted_idx].T,
            vert=False, labels=X.columns[sorted_idx]);

# THIS DOESN'T WORK - permutation_importance is considering the top-level features. It is permuting each one sequentially and learning the importance. 

# So, the inner encoding i.e. OHE/tfid is not visible to it.

# To get the importance of components of the top-level feature, you should encode it separately and then pass the encoded data to the permutation_importance

# Get the pre-processed data using preprocessing_cv.fit_transform(X_train)
# Call your permutation_importance code on the above data and any model of your choice

# CODE THAT WORKS: 

X_trans = preprocessing_cv.fit_transform(X_train)

clf = DecisionTreeClassifier().fit(X_trans, y_train)

permutation_importance(clf_nb, X_trans, y_train, n_repeats=10, random_state=42, n_jobs=2)