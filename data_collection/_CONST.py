
class _Const:
    # def __init__(self,os):
    #     self.AWS_ACCESS_KEY_ID = f"{os.getenv('AWS_ACCESS_KEY_ID')}"
    #     self.AWS_SECRET_ACCESS_KEY = f"{os.getenv('AWS_SECRET_ACCESS_KEY')}"
    #     self.DB_NAME = f"{os.getenv('DB_NAME')}"
    #     self.BUCKET_NAME = f"{os.getenv('BUCKET_NAME')}"
    #     self.SERVER_AREA = f"{os.getenv('SERVER_AREA')}"
    #     self.ROW_PER_FILE = int(f"{os.getenv('ROW_PER_FILE')}")
    #     self.LOCAL_COPY = bool(int(f"{os.getenv('LOCAL_COPY')}"))

    MAX_BATCH_ELEMENT_COUNT = 25
    COL_PER_ROW = 2048
    ROW_PER_FILE = 10000
    DB_NAME = "your db name"
    AWS_ACCESS_KEY_ID = "your access key"
    AWS_SECRET_ACCESS_KEY = "your secret key"
    BUCKET_NAME = "your bucket name"
    SERVER_AREA = "your server area"
    LOCAL_COPY = True
