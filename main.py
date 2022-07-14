#!/usr/bin/env python3

'''
Create static website and output to file.
'''

import os
from argparse import ArgumentParser
import jinja2
import yaml
import markdown


def generate_website_data(data):
    '''
    Generate data to embed in the static website, including pipeline details.
    '''
    # Convert descriptions from markdown to html
    def convert(to_convert):
        for item in to_convert:
            item['description'] = markdown.markdown(item['description'])
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
        data['commit']['url'] = f"{os.environ['CI_PROJECT_URL']}/commit/" \
            f"{os.environ['CI_COMMIT_SHA']}"
    data['pipeline']['id'] = os.getenv('CI_PIPELINE_ID', 'N/A')
    data['pipeline']['url'] = os.getenv('CI_PIPELINE_URL', '')


def execute_template(data, template, output_file):
    '''
    Use generated data to create static website using the template, and output
    it to `output_file`.
    '''
    # Execute the jinja2 template
    subs = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./')
    ).get_template(template).render(data=data)

    # Save jinja2 templating result
    with open(output_file, 'w', encoding="utf8") as out_file:
        out_file.write(subs)


def main():
    '''
    Create static website and output to file.
    '''
    # Parse the cli arguments
    parser = ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, help='Output dir')
    args = parser.parse_args()

    if args.output_dir is None:
        output_dir = 'out'
    else:
        output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f'{output_dir} directory not found, creating.')

    # Load in config file
    with open('config.yml', 'r', encoding="utf8") as config_file:
        data = yaml.safe_load(config_file)

    # Modify data for website
    website_data = data.copy()
    generate_website_data(website_data)

    # Create website
    execute_template(website_data, 'website/index.jinja2',
                     f'{output_dir}/index.html')

    # Create markdown resume
    execute_template(data, 'resume/resume.jinja2',
                     f'{output_dir}/resume.md')

    return 0


if __name__ == '__main__':
    main()
