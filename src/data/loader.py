import seaborn as sns
from project.config import RAW_DATA

def load_data():
    return sns.load_dataset(RAW_DATA)