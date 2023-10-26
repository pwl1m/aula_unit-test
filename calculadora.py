def soma(x,y):
    #doc test
    """ Soma x e y
    >>> soma(10,20)
    30
    >>> soma(-110,50)
    10
    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: x deve ser int ou float
    """
    # desfazer assertion -O no terminal antes de rodar o programa
    assert isinstance(x, (int, float)), 'x deve ser int ou float'
    assert isinstance(y, (int, float)), 'y deve ser int ou float'
    return x + y

def subtrai(x,y):
    #doc teste
    """ Subtrai x e y
    >>> subtrai (10,5)
    5
    >>> subtrai ('10',5)
    Traceback (most recent call last):
    ...
    AssertionError: x deve ser int ou float
    """
    # assertion
    assert isinstance(x, (int, float)), 'x deve ser int ou float'
    assert isinstance(y, (int, float)), 'y deve ser int ou float'
    return x-y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)