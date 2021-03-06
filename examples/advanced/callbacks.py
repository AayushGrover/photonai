from sklearn.datasets import load_boston
from sklearn.model_selection import KFold

from photonai.base import Hyperpipe, PipelineElement, CallbackElement, OutputSettings


# DEFINE CALLBACK ELEMENT
def my_monitor(X, y=None, **kwargs):
   print(X.shape)
   debug = True


# WE USE THE BREAST CANCER SET FROM SKLEARN
X, y = load_boston(return_X_y=True)

# DESIGN YOUR PIPELINE
settings = OutputSettings(project_folder='./tmp/')

my_pipe = Hyperpipe('basic_svm_pipe_no_performance',
                    optimizer='grid_search',
                    metrics=['mean_squared_error', 'pearson_correlation'],
                    best_config_metric='mean_squared_error',
                    outer_cv=KFold(n_splits=3),
                    inner_cv=KFold(n_splits=3),
                    verbosity=1,
                    output_settings=settings)


# ADD ELEMENTS TO YOUR PIPELINE
# first normalize all features
my_pipe += PipelineElement('StandardScaler')

my_pipe += CallbackElement("monitor", my_monitor)

# engage and optimize the good old SVM for Classification
my_pipe += PipelineElement('RandomForestRegressor', hyperparameters={'n_estimators':[10]})

# NOW TRAIN YOUR PIPELINE
my_pipe.fit(X, y)

debug = True


