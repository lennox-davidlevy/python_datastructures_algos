from Progression import Progression
from ArithmeticProgression import ArithmeticProgression
from GeometricProgression import GeometricProgression
from FibonacciProgression import FibonacciProgression

if __name__ == "__main__":
    print("Default Progrssion:")
    Progression().print_progressions(10)
    print("-------------------")
    print("ArithmeticProgression with increment 5:")
    ArithmeticProgression(5).print_progressions(10)
    print("-------------------")
    print("ArithmeticProgression with increment 5 and start 2:")
    ArithmeticProgression(5, 2).print_progressions(10)
    print("-------------------")
    print("GeometricProgression with default base:")
    GeometricProgression().print_progressions(10)
    print("-------------------")
    print("GeometricProgression with base of 3:")
    GeometricProgression(3).print_progressions(10)
    print("-------------------")
    print("FibonacciProgression with base start value:")
    FibonacciProgression().print_progressions(10)
    print("-------------------")
    print("FibonacciProgression with start values 4 and 6:")
    FibonacciProgression(4, 6).print_progressions(10)
    print("-------------------")
