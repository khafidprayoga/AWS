"""
Created by: Khafid Prayoga
"""

import click
import boto3

@click.command()
@click.option('-s', '--src', 'source', default='en',
                help='Source language', type=str)
@click.option('-d', '--dst', 'destination', default='id',
                help='Destination language', type=str)
@click.option('-r', '--reg', 'region', default='us-east-1',
                help='AWS Translate region')
def translate(source, destination, region):
    """This script is used to translate text, powered by AWS Translate
    \f
    Parameters:

        * source = Country code of source text, [en]\n
        * destination = Country code of result text, [id]\n
        * region = AWS region to run Translate service, [us-east-1]\n

    For more information about country code, you can visit
    AWS documentation at https://docs.aws.amazon.com/translate/index.html
    """
    textinput = click.prompt('Original text')
    aws = boto3.client(service_name='translate',
                            region_name=region, use_ssl=True)
    result = aws.translate_text(Text=textinput,
                                SourceLanguageCode=source,
                                TargetLanguageCode=destination)
    click.echo(message=result.get('TranslatedText'))
