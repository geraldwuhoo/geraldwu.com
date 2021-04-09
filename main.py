import jinja2
import yaml
import markdown
import os


def main():
    config = 'config.yaml'
    template = 'index.jinja2'
    outputfile = 'index.html'

    # Load in config file
    with open(config) as f:
        data = yaml.safe_load(f)

    # Convert descriptions from markdown to html
    def convert(to_convert):
        for item in to_convert:
            item['description'] = markdown.markdown(item['description'])[3:-4]
    to_convert = ['about', 'experience', 'projects']
    for i in to_convert:
        convert(data[i])

    # Fill in predefined variables from GitLab CI/CD
    data['repo'] = {}
    data['commit'] = {}
    data['pipeline'] = {}

    data['repo']['path'] = os.getenv('CI_PROJECT_PATH', 'N/A')
    data['repo']['url'] = os.getenv('CI_PROJECT_URL', '')
    data['commit']['sha'] = os.getenv('CI_COMMIT_SHORT_SHA', 'N/A')
    if os.environ.get('CI_PROJECT_URL'):
        data['commit']['url'] = "{}/commit/{}".format(
            os.environ['CI_PROJECT_URL'],
            os.environ['CI_COMMIT_SHA']
        )
    data['pipeline']['id'] = os.getenv('CI_PIPELINE_ID', 'N/A')
    data['pipeline']['url'] = os.getenv('CI_PIPELINE_URL', '')

    # Execute the jinja2 template
    subs = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./')
    ).get_template(template).render(data=data)

    # Save jinja2 templating result
    with open(outputfile, 'w') as f:
        f.write(subs)

    return 0


if __name__ == '__main__':
    main()
