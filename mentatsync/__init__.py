# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import mozsvc.config


def includeme(config):
    """Install MentatSync application into the given Pyramid configurator."""
    # Disable cornice default exception-handling views.
    config.registry.settings.setdefault("handle_exceptions", False)
    # Include dependencies from other packages.
    config.include("cornice")
    config.include("mozsvc")
    # Add in the stuff we define ourselves.
    config.include("mentatsync.storage")
    config.scan("mentatsync.views")


def get_configurator(global_config, **settings):
    """Load a MentatSync configurator object from deployment settings."""
    config = mozsvc.config.get_configurator(global_config, **settings)
    config.begin()
    try:
        config.include(includeme)
    finally:
        config.end()
    return config


def main(global_config, **settings):
    """Load a MentatSync WSGI app from deployment settings."""
    config = get_configurator(global_config, **settings)
    return config.make_wsgi_app()
