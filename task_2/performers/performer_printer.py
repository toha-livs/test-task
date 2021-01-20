from task_2.performers.base_performer import BasePerformer


class PerformerPrinter(BasePerformer):

    @staticmethod
    def formating(name, products):
        return {'name': name, products: products}

    @staticmethod
    def pushing(data):
        print('Pushing data to printer...')

