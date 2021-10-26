from sklearn.base import TransformerMixin, BaseEstimator

class Debug(BaseEstimator, TransformerMixin):

    def transform(self, X):
        print(pd.DataFrame(X).head())
        print(X.shape)
        return X

    def fit(self, X, y=None, **fit_params):
        return self

# Create a pipeline
gs_pipe = Pipeline(
        steps=[
            ('preprocessor', preprocessor),  # preprocessor pipeline
            ('dbg', Debug()), ################ -> POSITION THIS WHEREVER YOU WANT TO SEE THE OUTPUT
            ('selector', SelectPercentile(
                score_func = mutual_info_regression)
                ),  # Feature selection
            
            ('classifier', ExtraTreesClassifier(n_jobs = -1))  # the regression model
        ]
    )