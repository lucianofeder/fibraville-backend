class DataNotFound(Exception):
    def __init__(self, data):
        self.message = {"error": f'{data} nao foi encontrado'}