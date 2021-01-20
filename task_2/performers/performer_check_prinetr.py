from task_2.performers.performer_printer import PerformerPrinter


class PerformerCheckPrinter(PerformerPrinter):

    @staticmethod
    def pushing(data):
        print('Pushing data to Check printer...')
