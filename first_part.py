

class RomanNumberError(Exception):
    pass



numero_romano = (
    (1000, "M"), (500, "D"), (100, "C"), (50, "D"), (10, "X"), (5, "V"), (1, "I")
)

componentes = (
    ( # millares
        (1000, 'M'), (2000, 'MM'), (3000, 'MMM')
    ), 
    ( # centenas
        (100, 'C'), (200, 'CC'), (300, 'CCC'),
        (400, 'CD'), (500, 'D'), (600, 'DC'),
        (700, 'DCC'), (800, 'DCCC'), (900, 'CM')
    ),
    ( # decenas
        (10, 'X'), (20, 'XX'), (30, 'XXX'),
        (40, 'XL'), (50, 'L'), (60, 'LX'),
        (70, 'LXX'), (80, 'LXXX'), (90, 'XC')
    ),
    ( # unidades
        (1, 'I'), (2, 'II'), (3, 'III'),
        (4, 'IL'), (5, 'V'), (6, 'VI'),
        (7, 'VII'), (8, 'VIII'), (9, 'IX')
    )

)


def entero_a_romano(numero):
    """
    numero = str(numero)
    longitud = len(numero)

    if longitud < 4:
        numero = "{:0>4s}".format(numero)
    """
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    ix = 0
    longitud = len(digitos)
    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        ix += 1

  