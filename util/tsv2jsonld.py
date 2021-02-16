#!/usr/bin/env python
import json
import csv
import click

@click.command()
@click.option('--context', '-C', help='context file')
@click.argument('input')
def convert(input, context):
    """
    generates jsonld
    """
    with open(context) as context_file:
        cobj = json.load(context_file)['@context']
    items = []
    with open(input) as csvfile:
        rr = csv.DictReader(csvfile, delimiter='\t', quotechar='|')
        items = [process(item) for item in rr]
    obj = {'@context': cobj,
           'associations': items}
    print(json.dumps(obj, indent=4, sort_keys=True))

def process(x):
    for k,v in x.items():
        x[k] = process_atom(v)
    return x
    
    
def process_atom(s):
    if '|' in s:
        return s.split('|')
    else:
        return s
    
if __name__ == '__main__':
    convert()

