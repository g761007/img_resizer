import os

import click
from PIL import Image

curdir = os.path.abspath('.')

@click.command()
@click.option('--path', default=curdir, help='the directory of images (default: ".")')
@click.option('--format', default='png', help='image format (default: png)')
@click.option('--postfix', default='@3x.png', help='mapping @3x image (default: @3x.png)')
def resize(path, format, postfix):
    click.echo('current location = %s' % path)
    image_files = None
    for _, _, filenames in os.walk(path):
        image_files = [filename for filename in filenames if filename.endswith('{0}'.format(postfix))]

    success = []
    failure = []
    for filename in image_files:
        click.echo('process image: %s' % filename)
        try:
            with Image.open(os.path.join(path, filename)) as im:
                name = filename[:-len(postfix)]
                im.save(os.path.join(path, '{0}@3x.{1}'.format(name, format)), format=format)
                w, h = im.size
                im2x = im.copy()
                im2x.thumbnail((float(w) / 3 * 2, float(h) / 3 * 2))
                im2x.save(os.path.join(path, '{0}@2x.{1}'.format(name, format)), format=format)
                im1x = im.copy()
                im1x.thumbnail((float(w) / 3, float(h) / 3))
                im1x.save(os.path.join(path, '{0}.{1}'.format(name, format)), format=format)
                success.append(filename)
        except Exception as e:
            click.echo('error=%s' % e)
            failure.append(filename)
    click.echo('total success resize images: %d' % len(success))
    click.echo('total failure resize images: %d' % len(failure))
    click.echo('done.')
