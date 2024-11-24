'''

Logging in MLOps (Machine Learning Operations) is essential for tracking, 
monitoring, and debugging machine learning models throughout their lifecycle. 
It enables teams to record and analyze metrics, errors, and system states,
which is critical for reproducibility, model performance evaluation, and issue resolution.
'''



import logging # used in debugging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)