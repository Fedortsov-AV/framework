from jinja2 import Template


def render(template_name, context=None):
    with open(f'template/{template_name}', encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())

    return template.render(context=context)


if __name__ == '__main__':
    pass
    # context = {
    #     'name': 'MyName',
    # }
    # output_test = rendering('index.html', context)
    # print(output_test)
