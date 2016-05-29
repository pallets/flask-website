from urlparse import urljoin


server = 'http://pypi.python.org/'
detail_path = '/pypi/Flask/%s'


class Release(object):

    def __init__(self, version):
        self.version = version

    def to_json(self):
        return dict(version=self.version,
                    detail_url=self.detail_url)

    @property
    def detail_url(self):
        return urljoin(server, detail_path % self.version)


releases = map(Release, [
    '0.1',
    '0.2',
    '0.3',
    '0.3.1',
    '0.4',
    '0.5',
    '0.5.1',
    '0.5.2',
    '0.6',
    '0.6.1',
    '0.7',
    '0.7.1',
    '0.7.2',
    '0.8',
    '0.8.1',
    '0.9',
    '0.10',
    '0.10.1',
    '0.11',
])
