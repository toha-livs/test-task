from task_2.performers.base_performer import BasePerformer


class EmailPerformer(BasePerformer):

    @staticmethod
    def formating(name, products):
        product_template = '<product name="{name}" count="{count}" sum="{sum}" price="{price}"/>'
        result = f'<name>{name}</name>'
        result += ''.join([product_template.format(**vars(product)) for product in products])
        return result

    @staticmethod
    def pushing(data):
        print('Pushing data to mail server...')
