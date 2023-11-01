"""TODO: полоса загрузки для отслеживания прогресса"""
import json
import uuid
import warnings
from connectionz.exceptions import ObjectIsNotExistException


class Operation:
    """
    Operation implementation.

    Examples:
        >>> operation_1 = Operation(name='Calculation', expression='x = 2 + 2')
        >>> operation_2 = Operation(name='Print result', expression='print(x)')
    """
    def __init__(self, name: str, expression: str):
        self.name = name
        self.expression = expression


class Template:
    """
    Template implementation.

    Import template example:
        >>> template = Template()
        >>> template.import_template('path/to/template.json')
        >>> template.show_description()
        >>> template.run()

    Export template example:
        >>> template = Template()
        >>> template.add_operation(Operation(name='Assign', expression='x = 2'))
        >>> template.add_operation(Operation(name='Assign', expression='y = 3'))
        >>> template.add_operation(Operation(name='Sum', expression='x + y'))
        >>> template.edit_description('New template description.')
        >>> template.run()
        >>> template.export_template('path/to/template.json')
    """
    def __init__(self, *operation: Operation, template_description: str = None):
        self.description = template_description
        self.operations = [*operation]

    def run(self, **kwargs):
        for variable, value in kwargs.items():
            if isinstance(value, str):
                exec(f'{variable} = "{value}"', globals())
            else:
                exec(f'{variable} = {value}', globals())
        for operation in self.operations:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                warnings.warn('deprecatd', DeprecationWarning)
                exec(operation.expression, globals())

    def add_operation(self, operation: Operation) -> None:
        self.operations.append(operation)

    def del_operation(self, operation: Operation) -> None:
        if operation in self.operations:
            self.operations.remove(operation)
        else:
            raise ObjectIsNotExistException()

    def edit_description(self, template_description: str) -> None:
        self.description = template_description

    def show_description(self) -> None:
        print(self.description)

    def import_template(self, path_to_template: str) -> None:
        with open(path_to_template, 'r+', encoding='utf-8') as file:
            template = json.load(file)
        template_description = template['description']
        template_operations = template['operations']
        for operation in template_operations:
            self.add_operation(
                Operation(
                    name=operation['name'],
                    expression=operation['expression']
                )
            )
        self.description = template_description

    def export_template(self, path_to_template: str) -> None:
        template = {
            'description': self.description,
            'operations': [
                item.__dict__
                for item in self.operations
            ]
        }
        with open(path_to_template, 'w+', encoding='utf-8') as file:
            json.dump(template, file)
