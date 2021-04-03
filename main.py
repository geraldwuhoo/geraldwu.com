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
    convert(data['experience'])
    convert(data['projects'])
    
    # Fill in predefined variables from GitLab CI/CD
    data['commit'] = os.getenv('CI_COMMIT_SHORT_SHA', 'N/A')
    data['repo'] = os.getenv('CI_REPOSITORY_URL', '#')
    data['pipeline'] = os.getenv('CI_PIPELINE_URL', '#')
    data['pipeline_id'] = os.getenv('CI_PIPELINE_ID', 'N/A')

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