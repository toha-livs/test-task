from task_2.performers import PerformerPrinter, BasePerformer


class BasePrinter:

    performer = PerformerPrinter

    def __init__(self, check_name, sold_products: list):
        self.check_name = check_name
        self.sold_products = sold_products

    def perform(self, performer_class=None):
        if performer_class is None:
            performer_class = self.performer
        if not isinstance(performer_class, BasePerformer):
            raise TypeError('performer_class is not a <BasePerformer> instance')
        performer_class.perform(self.check_name, self.performer)


