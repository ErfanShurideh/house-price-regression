from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_FILE = DATA_DIR / "raw" / "housing.csv"
TRAIN_FILE = DATA_DIR / "processed" / "train.csv"
TEST_FILE = DATA_DIR / "processed" / "test.csv"
SQLTE_FILE = DATA_DIR / "processed" / "housing.db"


MODELS_DIR = PROJECT_ROOT / "models"
MODEL_FILE = MODELS_DIR / "final_model.joblib"
MODEL_INFO_FILE = MODELS_DIR / "model_info.json"

DATA_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
EXPECTED_ROW = 20640


TARGET = "medin_house_value"

TARGET_CAP = 500001

RANDOM_SEED = 42
TEST_SIZE = 0.2
CV_FOLDS = 5 