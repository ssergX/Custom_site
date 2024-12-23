from jinja2 import Environment, FileSystemLoader
import markdown



def build_site():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.html')

    with open('content/index.md', 'r') as md_file:
        content = markdown.markdown(md_file.read())

    output = template.render(content=content, title="Мой Сайт", description="Описание сайта")
    with open('index.html', 'w') as html_file:
        html_file.write(output)


if __name__ == "__main__":
    build_site()
