# Práctica 1 - El dogma central de la biología molecular

## Integrantes

- Martha Yunnuen Pacheco Ramírez - 315068830
- Shai Léger Hernández - 316321761

## Descripción
Este script recibe un archivo FASTA, extrae el nombre y la secuencia, finalmente imprime los siguientes datos:

- Nombre de la proteína
- Cadena ADN original
- Cadena ADN complementaria
- Cadena transcrita de ARNm 
- Cadena traducida de aminoácidos

> ⚠️El script imprime la cadena de aminoácidos solo cuando la secuencia tiene caracteres permitidos, codon de inicio y longitud válida.

## Requisitos

- Python 3.10 o superior
> 💡 Es muy probable que el script funcione en versiones anteriores, sin embargo, no se ha probado.

## Ejecución

```bash
python p1_dogma_central.py [RUTA_ARCHIVO_FASTA]
```
> 💡 En la carpeta `data` se propocionan varios archivos FASTA.

## Ejemplos

- Botulinum neurotoxina tipo A 
    ```bash
    python p1_dogma_central.py .\data\bont.txt
    ```

    ```
    ____________________________________
    Secuencia #1
    Nombre: NC_009495.1:909709-913599 bont [organism=Clostridium botulinum A str. ATCC 3502] [GeneID=5185061] [chromosome=]
    Secuencia: ATGCCATTTGTTAATAAACAATTTAATTATAAAGATCCTGTAAATGGTGTTGATATTGCTTATATAAAAATTCCAAATGCAGGACAAATGCAACCAGTAAAAGCTTTT...
    Complemento: TACGGTAAACAATTATTTGTTAAATTAATATTTCTAGGACATTTACCACAACTATAACGAATATATTTTTAAGGTTTACGTCCTGTTTACGTTGGTCATTTTCGAA...
    ARNm: UACGGUAAACAAUUAUUUGUUAAAUUAAUAUUUCUAGGACAUUUACCACAACUAUAACGAAUAUAUUUUUAAGGUUUACGUCCUGUUUACGUUGGUCAUUUUCGAAAAUUUUA...
    Aminoácidos: YGKQLFVKLIFLGHLPQL_RIYF_GLRPVYVGHFRKF_VLFYUQ_GLSLCKCLGLLPLNLGGGLRFVQGQSIILSCINSCLLLFLLINFPQCFNKLS_IS_LEPSY...
    ```

- Mioglobina
    ```bash
    python p1_dogma_central.py .\data\MB.txt
    ```

    ```
    ____________________________________
    Gen #1
    Nombre: NW_021145510.1:c39467-28809 MB [organism=Physeter catodon] [GeneID=102975021] [chromosome=Un]
    Secuencia: AGCTGTCGGAGCCAGGACACCCGGTCAGCCCACTCTCGCTCTTCTTCTCTTCTTCAGACTGTGCCATGGTGCTCAGCGAGGGAGAATGGC...
    Complemento: TCGACAGCCTCGGTCCTGTGGGCCAGTCGGGTGAGAGCGAGAAGAAGAGAAGAAGTCTGACACGGTACCACGAGTCGCTCCCTCTTAC...
    ARNm: UCGACAGCCUCGGUCCUGUGGGCCAGUCGGGUGAGAGCGAGAAGAAGAGAAGAAGUCUGACACGGUACCACGAGUCGCUCCCUCUUACCGUCAAC...
    Aminoácidos: La secuencia no contiene un codón de inicio.
    ```
  
- Miembro 1 de la subfamilia B del casete de unión a ATP
    ```bash
    python p1_dogma_central.py .\data\ABCB1.txt
    ```

    ```
    ____________________________________
    Secuencia #1
    Nombre: NC_051818.1:c13507439-13410127 ABCB1 [organism=Canis lupus familiaris] [GeneID=403879] [chromosome=14]
    Secuencia: GCCCCCGCCTCACTCCCCGGGACGCAGGAAACCCGGGCGCCTGCGAGCAGCGGCTCCTCCTGGCTCCAAGGAGCCCAGGCCGTTGTTCGTGCCCTCCGG...
    Complemento: CGGGGGCGGAGTGAGGGGCCCTGCGTCCTTTGGGCCCGCGGACGCTCGTCGCCGAGGAGGACCGAGGTTCCTCGGGTCCGGCAACAAGCACGGGAGG...
    ARNm: CGGGGGCGGAGUGAGGGGCCCUGCGUCCUUUGGGCCCGCGGACGCUCGUCGCCGAGGAGGACCGAGGUUCCUCGGGUCCGGCAACAAGCACGGGAGGCCCAGAA...
    Aminoácidos: La longitud de la secuencia es inválida.
    ____________________________________
    Secuencia #2
    Nombre: NC_049274.1:c13710576-13613256 ABCB1 [organism=Canis lupus familiaris] [GeneID=403879] [chromosome=14]
    Secuencia: ATGGATCCTGAAGGAGGCCGTAAGGGGAGTGCAGAGAAGAACTTCTGGAAAATGGGCAAAAAAAGGTAGCCAGTTTCTTTCACTTTCATACCTTACATG...
    Complemento: TACCTAGGACTTCCTCCGGCATTCCCCTCACGTCTCTTCTTGAAGACCTTTTACCCGTTTTTTTCCATCGGTCAAAGAAAGTGAAAGTATGGAATGT...
    ARNm: UACCUAGGACUUCCUCCGGCAUUCCCCUCACGUCUCUUCUUGAAGACCUUUUACCCGUUUUUUUCCAUCGGUCAAAGAAAGUGAAAGUAUGGAAUGUACCGAAC...
    Aminoácidos: La longitud de la secuencia es inválida.
    ____________________________________
    Secuencia #3
    Nombre: NC_049755.1:c13436445-13339096 ABCB1 [organism=Canis lupus familiaris] [GeneID=403879] [chromosome=14]
    Secuencia: ATGGATCCTGAAGGAGGCCGTAAGGGGAGTGCAGAGAAGAACTTCTGGAAAATGGGCAAAAAAAGGTAGCCAGTTTCTTTCACTTTCATACCTTACATG...
    Complemento: TACCTAGGACTTCCTCCGGCATTCCCCTCACGTCTCTTCTTGAAGACCTTTTACCCGTTTTTTTCCATCGGTCAAAGAAAGTGAAAGTATGGAATGT...
    ARNm: UACCUAGGACUUCCUCCGGCAUUCCCCUCACGUCUCUUCUUGAAGACCUUUUACCCGUUUUUUUCCAUCGGUCAAAGAAAGUGAAAGUAUGGAAUGUACCGAAC...
    Aminoácidos: YLGLPPAFPSRLFLKUFYPFFSIGQRK_KYGMYRUL_PLYLKIRGRDFIYFCUVKIGAYVRQEDVSK_PUQLLSQM_KGAGPEARRRSRKDGGRAGH...
    ____________________________________
    .
    .
    .
    ```

## Recursos

- [Práctica 1](https://nayeli-luis.github.io/GC-2023.1/#pr%C3%A1ctica-1--el-dogma-central-de-la-biolog%C3%ADa-molecular)
- [Correct way to parse a FASTA file in Python](https://www.biostars.org/p/710/)
- [DNA Utilities](https://arep.med.harvard.edu/labgc/adnan/projects/Utilities/revcomp.html)
- [Codon to sequence](https://www.macromoltek.com/utilities/codon2sequence/)