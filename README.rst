================
Flickr Pony Demo
================

This project is a Django project for demonstrate Flick Pony. For use it: ::

    git clone https://github.com/ZuluPro/flickr-pony-demo
    cd flickr-pony-demo
    pip install requirements.txt
    cd demo_project
    export FLICKR_API_KEY="YourFlickrApiKey" # Mandatory
    # export FLICKR_USER_ID="YourFlickrUserId"
    ./manage runserver

You can also deploy it on Heroku:

.. image:: https://www.herokucdn.com/deploy/button.svg
        :target: https://heroku.com/deploy?template=https://github.com/ZuluPro/flickr-pony-demo

Put your ``FLICKR_API_KEY`` and optionaly ``FLICKR_USER_ID`` in your
application environment variables.
