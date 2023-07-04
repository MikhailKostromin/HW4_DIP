""" 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""


def dict_work(**kwargs) -> dict:
    res_dict = {}
    for name, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        res_dict[value] = name

    return res_dict


print(dict_work(X=123, y='qwe', C=[43, 45, 7], d=-0.5, e={'qwe': 132, 'ewq': 54}, f={12, 54, 45}))
