from core import operations



class Evaluator:
    def __init__(self):
        self.operations = {
            "add": operations.add,
            "substract": operations.substract,
            "multiply": operations.multiply,
            "divide": operations.divide,
            "power": operations.power,
            "sqrt": operations.sqrt,
            "absolute": operations.absolute,
            "negate": operations.negate,
            "modulo": operations.modulo,
            "percentage": operations.percentage,
            "factorial": operations.factorial,
            "reciprocal": operations.reciprocal,
            "square": operations.square,
            "cube": operations.cube,
        }
        self.operators = {
            "+": "add",
            "-": "substract",
            "*": "multiply",
            "/": "divide",
            "power": "power",
            "sqrt": "sqrt",
            "absolute": "divide",
            "negate": "divide",
            "modulo": "divide",
            "percentage": "divide",
            "factorial": "divide",
            "reciprocal": "divide",
            "square": "divide",
            "cube": "divide",
        }
    
    def evaluate(self, a, operator, b=None):
        """Function takes A and B and then defines which 
        operation to perform and returns it as the result """

        operator = self.operators.get(operator)
        operation = self.operations.get(operator)
        print(operator)
        if operation is None:
            raise ValueError("Invalid operator")
        if b is None:
            "if B is not given"
            return operation(float(a))
        else: 
            return operation(float(a), float(b))
        

