import json
import os
from datetime import timedelta

DATA_FILE = "leitner_box.json"

BOXES = {
    1: timedelta(days=1), # box 1 : review every 1 day
    2: timedelta(days=3), # box 2 : review every 3 day
    3: timedelta(days=7), # box 3 : review every 7 day
    4: timedelta(days=14), # box 4 : review every 14 day
    5: timedelta(days=30), # box 5 : review every 30 day
}