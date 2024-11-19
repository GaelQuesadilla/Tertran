import click
import src.data.langs as lg
import requests_cache
import urllib.parse
from src.data.symbols import goodArrow, badArrow


@click.command()
@click.argument("source_lang", type=click.Choice(lg.langs.keys()))
@click.argument("target_lang", type=click.Choice(lg.langs.keys()))
@click.argument("input_text")
def translate(source_lang, target_lang, input_text):
    '''
      Command line to translate any text
    '''
    api_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}"

    input_text = input_text.replace("\n", " ")
    input_text = urllib.parse.quote(input_text)
    try:
        session = requests_cache.CachedSession(
            cache_name="cache", expire_after=604800)
        r = session.get(api_url.format(source_lang, target_lang, input_text))

        if r.status_code == 200:
            click.echo(f"\n{goodArrow} {r.json()[0][0][0]}\n")
        else:
            click.echo(f"{badArrow} Error ... status code {r.status_code}")
    except Exception as e:
        click.echo(f"{badArrow} Connection error")
