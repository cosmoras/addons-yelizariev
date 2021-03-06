{
    'name' : 'Last viewed records',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Base',
    'website' : 'https://it-projects.info',
    'description': """
The idea is taken from SugarCRM's "Last viewed" feature.

This module doesn't affect on server performance, because it uses browser's localStorage to save history. But dissadvantage is that history is not synced accross browsers.

FIXME: doesn't work in a res.config view

Tested on 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d.
    """,
    'depends' : ['web', 'mail'],
    'data':[
        'views.xml',
        ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'installable': True
}
