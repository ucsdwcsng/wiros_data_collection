
class _Const:
    def __init__(self,os):
        self.AWS_ACCESS_KEY_ID = f"{os.getenv('AWS_ACCESS_KEY_ID')}"
        self.AWS_SECRET_ACCESS_KEY = f"{os.getenv('AWS_SECRET_ACCESS_KEY')}"
        self.DB_NAME = f"{os.getenv('DB_NAME')}"

    MAX_BATCH_ELEMENT_COUNT = 25
    COL_PER_ROW = 2048
    ROW_PER_FILE = 10000
    DB_NAME = None
    AWS_ACCESS_KEY_ID = None
    AWS_SECRET_ACCESS_KEY = None
    # MAX_THROTTLING_ERROR_TOLERANCE = 10
