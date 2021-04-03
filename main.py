import jinja2
import yaml
import markdown

def main():
    config = 'config.yaml'
    template = 'index.jinja2'
    outputfile = 'index.html'

    with open(config) as f:
        data = yaml.safe_load(f)

    for job in data["experience"]:
        job["description"] = markdown.markdown(job["description"])[3:-4]

    for project in data["projects"]:
        project["description"] = markdown.markdown(project["description"])[3:-4]

    subs = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./')
    ).get_template(template).render(data=data)

    with open(outputfile, 'w') as f:
        f.write(subs)

    return 0

if __name__ == '__main__':
    main()