class BasePerformer:

    @staticmethod
    def formating(name, products):
        raise NotImplementedError

    @staticmethod
    def pushing(data):
        raise NotImplementedError

    @classmethod
    def perform(cls, name, products):
        data = cls.formating(name, products)
        cls.pushing(data)
