if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Nieprawidłowa liczba argumentów. Program nie ожидает аргументы командной строки.')
        sys.exit(1)

    input_file = input('Podaj ścieżkę do pliku wejściowego: ')
    output_file = input('Podaj ścieżkę do pliku wyjściowego: ')

    convert_file(input_file, output_file)