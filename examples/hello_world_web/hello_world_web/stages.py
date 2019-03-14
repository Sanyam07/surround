from surround import Stage, SurroundData
from surround.runner.wrapper import Wrapper
from surround import Surround

class HelloStage(Stage):
    def operate(self, surround_data, config):
        surround_data.text = "hello"

class BasicData(SurroundData):
    text = None

    def __init__(self, uploaded_data):
        self.uploaded_data = uploaded_data

class RotateImage(Stage):
    def operate(self, surround_data, config):
        print(surround_data.uploaded_data)

class WebWrapper(Wrapper):
    def __init__(self):
        surround = Surround([HelloStage(), RotateImage()])
        self.config = surround.config
        super().__init__(surround)

    def run(self, uploaded_data):
        data = BasicData(uploaded_data)
        self.surround.process(data)
        print(data.text)
