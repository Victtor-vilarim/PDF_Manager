import inspect
from colorama import Fore
from pdf_manager.modules import Console
from pdf_manager.utils import print_init_message, print_user_line, print_return


def sep_user_args(func):
    def wrapper():
        raw_input: str = func().strip()
        return raw_input.split()

    return wrapper


@sep_user_args
def user_input():
    return input()


def verify_attr(arg_list, instance) -> bool:
    if hasattr(instance, arg_list[0]):
        if callable(getattr(instance, arg_list[0])):
            return True
    raise NotImplementedError(f'{arg_list[0]} não é um comando válido')


def verify_args(arg_list, instance) -> bool:
    full_args = inspect.getfullargspec(getattr(instance, arg_list[0]))
    method_args = inspect.getfullargspec(getattr(instance, arg_list[0])).args
    if full_args.varargs is not None:
        return True

    elif len(method_args) > 0:
        if method_args[0] == 'self':
            if len(method_args) - 1 == len(arg_list) - 1:
                return True

        elif len(method_args) == len(arg_list) - 1:
            return True

    elif len(method_args) == 0:
        return True

    print(exe_attr(['help', f'{arg_list[0]}'], instance))
    raise TypeError(f'Quantidade de argumentos inválida. '
                    f'Necessários: {len(method_args) - 1} enviados: {len(arg_list) - 1}')


def exe_attr(arg_list, instance):
    return getattr(instance, arg_list[0])(*arg_list[1:])


def exe():
    console = Console()

    print_init_message()
    while True:
        print_user_line(console)
        user_says = user_input()
        try:
            result = None
            if verify_attr(user_says, console):
                if verify_args(user_says, console):
                    result = exe_attr(user_says, console)
        except FileNotFoundError as e:
            print(f'{Fore.LIGHTRED_EX} {e}')
        except IsADirectoryError as e:
            print(f'{Fore.LIGHTRED_EX} {e}')
        except ValueError as e:
            print(f'{Fore.LIGHTRED_EX} {e}')
        except NotImplementedError as e:
            print(f'{Fore.LIGHTRED_EX} {e}')
        except TypeError as e:
            print(f'{Fore.LIGHTRED_EX} {e}')
        except PermissionError:
            print(f'{Fore.LIGHTRED_EX}Não é possível realizar essa operação [Permissão Negada]')

        else:
            print_return(result)
