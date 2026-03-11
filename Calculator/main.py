from core.evaluator import Evaluator
from app.controller import Controller
from ui.gui import CalculatorGUI

def main():
    evaluator = Evaluator()
    controller = Controller(evaluator)
    gui = CalculatorGUI(controller)
    gui.run()


if __name__ == "__main__":
    main()