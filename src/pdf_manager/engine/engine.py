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


def verify_attr(arg_list, instance):
    if hasattr(instance, arg_list[0]):
        if callable(getattr(instance, arg_list[0])):
            return True
    raise NotImplementedError(f'{arg_list[0]} não é um comando válido')


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
                result = exe_attr(user_says, console)
        except FileNotFoundError as e:
            print(e)
        except IsADirectoryError as e:
            print(e)
        except ValueError as e:
            print(e)
        except NotImplementedError as e:
            print(e)
        except PermissionError:
            print('Não é possível realizar essa operação [Permissão Negada]')

        else:
            print_return(result)
