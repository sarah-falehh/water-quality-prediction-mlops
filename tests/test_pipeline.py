from water_quality.pipeline import prepare_data
from water_quality.config import DATA_PATH


def test_prepare_data_returns_consistent_splits():
    X_train, X_test, y_train, y_test = prepare_data(DATA_PATH)
    assert len(X_train) + len(X_test) == len(y_train) + len(y_test)
    assert "Potability" not in X_train.columns
    assert not X_train.isna().any().any()
