# coding=utf-8
"""Using dis module to see bytecodes.

    Python provides a dis module which can take the function, class, method, or code object as its single argument and provides a more human-readable source code in the level of assembler. You can also run the disassembler from the command line. It compiles the given script and prints the disassembled byte codes to the STDOUT.
"""
from dis import dis

def run():
    # Bytecodes for a list creation
    print(dis('[1, 2, 3, 4, 5]'))
    """
    >>>   1   0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 LOAD_CONST               3 (4)
              8 LOAD_CONST               4 (5)
             10 BUILD_LIST               5
             12 RETURN_VALUE
        None
    """

    # Bytecodes for a set creation
    print(dis('{1, 2, 3}'))
    """
    >>>   1   0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 BUILD_SET                3
              8 RETURN_VALUE
        None
    """

    # Bytecodes for a convertion from list to set
    print(dis('set([1, 2, 3])'))
    """
    >>>   1   0 LOAD_NAME                0 (set)
              2 LOAD_CONST               0 (1)
              4 LOAD_CONST               1 (2)
              6 LOAD_CONST               2 (3)
              8 BUILD_LIST               3
             10 CALL_FUNCTION            1
             12 RETURN_VALUE
        None
    """

    # Bytecodes for a function
    print(dis('sum2numbers(100, 200)'))
    """
    >>>   1   0 LOAD_NAME                0 (sum2numbers)
              2 LOAD_CONST               0 (100)
              4 LOAD_CONST               1 (200)
              6 CALL_FUNCTION            2
              8 RETURN_VALUE
        None
    """

    # You can use dis for debugging too.
    # For example if you try execute a division by 0 and use dis.distb(),
    # you can see where is the error in bytecode level
    """
        >>> 1/0
        -----------------------------------------------------------------------
        ZeroDivisionError       Traceback (most recent call last)
        <ipython-input-2-9e1622b385b6> in <module>()
        ----> 1 1/0

        ZeroDivisionError: division by zero


        >>> dis.distb()

        dis.distb()

        1     0 LOAD_CONST               0 (1)
              3 LOAD_CONST               1 (0)
    -->       6 BINARY_TRUE_DIVIDE
              7 PRINT_EXPR
              8 LOAD_CONST               2 (None)
             11 RETURN_VALUE

    """

def sum2numbers(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    run()
