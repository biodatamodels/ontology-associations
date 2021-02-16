#!/usr/bin/env python
import yaml
import click

@click.command()
@click.option('--source-class', '-c', help='class to use')
@click.argument('schema')
def gen_header(schema, source_class):
    """
    generates header from linkml yaml
    """
    obj = yaml.safe_load(open(schema))
    for cn,cobj in obj['classes'].items():
        if source_class is None or source_class == cn:
            if 'slots' in cobj:
                slots=[s.replace(' ', '_') for s in cobj['slots']]
                print(f'create table {cn.replace(" ","")} (')
                print(",\n".join([f'  {s} text' for s in slots]))
                print(');')

if __name__ == '__main__':
    gen_header()

