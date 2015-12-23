import os

import click
from PIL import Image

curdir = os.path.abspath('.')

@click.command()
@click.option('--path', default=curdir, help='the directory of images (default: ".")')
@click.option('--format', default='png', help='image format (default: png)')
def resize(path, format):
    click.echo('current location = %s' % path)
    image_files = None
    for _, _, filenames in os.walk(path):
        image_files = [filename for filename in filenames if filename.endswith('@3x.{0}'.format(format))]

    success = []
    failure = []
    for filename in image_files:
        click.echo('process image: %s' % filename)
        try:
            with Image.open(os.path.join(path, filename)) as im:
                w, h = im.size
                im2x = im.copy()
                im2x.thumbnail((float(w) / 3 * 2, float(h) / 3 * 2))
                im2x.save(os.path.join(path, filename).replace('@3x', '@2x'))
                im1x = im.copy()
                im1x.thumbnail((float(w) / 3, float(h) / 3))
                im1x.save(os.path.join(path, filename).replace('@3x', ''))
                success.append(filename)
        except Exception as e:
            click.echo('error=%s' % e)
            failure.append(filename)
    click.echo('total success resize images: %d' % len(success))
    click.echo('total failure resize images: %d' % len(failure))
    click.echo('done.')
