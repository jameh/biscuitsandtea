#! /usr/bin/env python2
from mysite import app

if __name__ == '__main__':
    app.debug=True
    try:
        from flask.ext.scss import Scss
        Scss(app, static_dir="mysite/static/css",
             asset_dir="mysite/static/scss")
    except ImportError:
        print("Not compiling scss, not installed.")

    app.run(host="0.0.0.0")
