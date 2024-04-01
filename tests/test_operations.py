import pytest
from app.plugins.calculator.add import Add
from app.plugins.calculator.subtract import Subtract
from app.plugins.calculator.multiply import Multiply
from app.plugins.calculator.divide import Divide

@pytest.mark.parametrize("operand1, operand2, expected", [
    (1, 2, 3),
    (5.5, 4.5, 10),
    (-1, -1, -2),
])
def test_add_command(operand1, operand2, expected):
    command = Add()
    assert command.execute(operand1, operand2) == expected

@pytest.mark.parametrize("operand1, operand2, expected", [
    (1, 2, -1),
    (5.5, 4.5, 1),
    (-1, -1, 0),
])
def test_subtract_command(operand1, operand2, expected):
    command = Subtract()
    assert command.execute(operand1, operand2) == expected

@pytest.mark.parametrize("operand1, operand2, expected", [
    (2, 3, 6),
    (5.5, 2, 11),
    (-2, -2, 4),
])
def test_multiply_command(operand1, operand2, expected):
    command = Multiply()
    assert command.execute(operand1, operand2) == expected

@pytest.mark.parametrize("operand1, operand2, expected", [
    (6, 3, 2),
    (5.5, 2, 2.75),
    (-4, -2, 2),
])
def test_divide_command(operand1, operand2, expected):
    command = Divide()
    assert command.execute(operand1, operand2) == expected

