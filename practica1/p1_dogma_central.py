"""
Integrantes:
- Shai Léger Hernández - 316321761

Práctica 1 -  El dogma central de la biología molecular - 17/Septiembre/2022
"""
import argparse
import re
from itertools import groupby

# Generamos un diccionario que indica como reemplazar cada caracter, el primer argumento son los caracteres
# originales y el segundo sus reemplazos. Posteriormente usaremos el método translate para toda la secuencia.
INTERCAMBIOS_COMPLEMENTO = str.maketrans("ACTG", "TGAC")
INTERCAMBIOS_ARNm = str.maketrans("ACTG", "ACUG")

# Standard Code
CODON_INICIAL = "ATG"
TRADUCCION_CODONES = {
    # Alanina
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Cisteina
    "UGU": "C", "UGC": "C",
    # Acido aspartico
    "GAU": "D", "GAC": "D",
    # Acido glutamico
    "GAA": "E", "GAG": "E",
    # Fenilalanina
    "UUU": "F", "UUC": "F",
    # Glicina
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    # Histidina
    "CAU": "H", "CAC": "H",
    # Isoleucina
    "AUA": "I", "AUU": "I", "AUC": "I",
    # Lisina
    "AAA": "K", "AAG": "K",
    # Leucina
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    # Metionina
    "AUG": "M",
    # Aspargina
    "AAU": "N", "AAC": "N",
    # Prolina
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Glutamina
    "CAA": "Q", "CAG": "Q",
    # Arginina
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    # Serina
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    # Treonina
    "ACU": "U", "ACC": "U", "ACA": "U", "ACG": "U",
    # Valina
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    # Triptofano
    "UGG": "W",
    # Tirosina
    "UAU": "Y", "UAC": "Y",
    # Stop
    "UAA": "_", "UAG": "_", "UGA": "_"
}


def leer_archivo_fasta(ruta: str):
    """
    Lee un archivo FASTA con evaluación perezosa y devuelve un generador que contiene el nombre y la secuencia de
    cada gen.

    :param ruta: ruta donde se encuentra el archivo
    :return: generador con nombre y secuencia
    """
    with open(ruta, encoding='utf-8') as fasta:
        nombre_secuencia = ''
        # Utilizamos groupby cuya funcion es agrupar lineas de acuerdo a una llave, en este caso nuestra llave
        # es el caracter '>', con esto capturamos la cabecera y las secuencias de un archivo.
        for cabecera, grupo in groupby(fasta, lambda linea: linea[0] == ">"):
            # Si la linea actual es la llave entonces eliminamos el caracter ">" y guardamos el nombre
            if cabecera:
                linea = next(grupo)
                nombre_secuencia = linea[1:].strip()
                continue

            # Si no hemos encontrado la llave ignoramos la línea actual
            if nombre_secuencia == '':
                continue

            # Si ya encontramos la llave tomamos toda la secuencia del grupo
            secuencia = ''.join(linea.strip() for linea in grupo)
            yield nombre_secuencia, secuencia


def obtener_complemento(secuencia: str) -> str:
    """
    Obtiene el complemento de una secuencia de ADN

    :param secuencia: secuencia de ADN a transformar
    :return: complemento de la secuencia de ADN
    """
    return secuencia.translate(INTERCAMBIOS_COMPLEMENTO)


def obtener_arnm(secuencia: str) -> str:
    """
    Obtiene el ARNm de una secuencia de ADN

    :param secuencia: secuencia de ADN a transformar
    :return: ARNm de la secuencia de ADN
    """
    return secuencia.translate(INTERCAMBIOS_ARNm)


def obtener_aminoacidos(secuencia: str) -> str:
    """
    Traduce la secuencia de RNAm a aminoácidos utilizando un diccionario de codones

    :param secuencia: secuencia RNA a traducir
    :return: secuencia de aminoácidos
    """
    aminoacidos = ''
    for i in range(0, len(secuencia), 3):
        codon = secuencia[i:i + 3]

        try:
            aminoacidos += TRADUCCION_CODONES[codon]
        except KeyError:
            aminoacidos += "-"

    return aminoacidos


def validar_secuencia(secuencia: str) -> bool:
    """
    Valida que:
    - Pueda separarse la secuencia en grupos de tres
    - Sólo contenga caracteres de bases nitrogenadas
    - Exista un codón inicial

    :param secuencia: secuencia de ADN a validar
    :return: si es válida o no
    """
    if len(secuencia) % 3 != 0:
        print("La longitud de la secuencia es inválida.")
        return False

    caracteres_permitidos = re.compile('^[ATCG]+$', re.IGNORECASE)
    if not caracteres_permitidos.match(secuencia):
        print("La secuencia contiene caracteres inválidos.")
        return False

    if not secuencia[0:3] == CODON_INICIAL:
        print("La secuencia no contiene un codón de inicio.")
        return False

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Práctica 1 - Genómica Computacional: Este programa procesa y extrae información de archivos FASTA')
    parser.add_argument('ruta', type=str, help='Ruta del archivo FASTA a procesar')
    args = parser.parse_args()

    contenido = leer_archivo_fasta(args.ruta)
    for indice, gen in enumerate(contenido, start=1):
        nombre, secuencia = gen

        complemento = obtener_complemento(secuencia)
        ARNm = obtener_arnm(complemento)

        print("____________________________________")
        print("Secuencia #" + str(indice))
        print("Nombre: " + nombre)
        print("Secuencia: " + secuencia)
        print("Complemento: " + complemento)
        print("ARNm: " + ARNm)
        print("Aminoácidos: ", end='')
        if validar_secuencia(secuencia):
            aminoacidos = obtener_aminoacidos(ARNm)
            print(aminoacidos)
