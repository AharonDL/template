import dtlpy as dl

class ServiceRunner(dl.BaseModelAdapter):
    def __init__(self, model):
        super().__init__(model=model)