from colorama import Fore, init

LIGHT_GREEN = Fore.LIGHTGREEN_EX
LIGHT_MAGENTA = Fore.LIGHTMAGENTA_EX

init(autoreset=True)


def print_user_line(instance):
    print(f'{instance.wd}{LIGHT_MAGENTA}>>>', end=' ')


def print_init_message():
    print('----- PDF_manager 0.1 -----')
    print('Escreva \'listmethods\' para listar os métodos disponíveis.')
    print(f'Escreva {LIGHT_GREEN}\'help\'{Fore.RESET} + [nome da função] para mais informações.')
    print('Escreva \'exit\' para sair.')


def print_return(result):
    if isinstance(result, str):
        print(result)
    elif hasattr(result, '__iter__'):
        for item in result:
            print(item)
    return
