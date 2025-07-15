from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import root_mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

from sklearn.model_selection import KFold

def perform_cv(cv_data, n_splits, error_function, model, sigma=None):
    
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        
    train_error, cv_error = [], []

    for _, (train_index, val_index) in enumerate(kf.split(cv_data)):
        train_data = cv_data[train_index, :]
        val_data = cv_data[val_index, :]

        X_train, y_train = train_data[:, :-1], train_data[:, -1]
        X_val, y_val = val_data[:, :-1], val_data[:, -1]

        model.fit(X_train, y_train)

        y_train_pred = model.predict(X_train)
        y_val_pred = model.predict(X_val)

        train_error.append(error_function(y_train_pred, y_train, sigma))
        cv_error.append(error_function(y_val_pred, y_val, sigma))
        
    return np.sqrt(np.mean(train_error)), np.sqrt(np.mean(cv_error))


def LR_error(prediction, true):
    return np.mean((true - prediction)**2)