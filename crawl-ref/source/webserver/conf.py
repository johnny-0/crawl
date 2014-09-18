import os, os.path, toml, logging, sys

class Conf(object):
    def __init__(self):
        self.data = None
        self.load()

    def load(self):
        path = os.environ.get("WEBTILES_CONF")
        if path is None:
            if os.path.exists("./config.toml"):
                path = "./config.toml"
            else:
                path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "config.toml")

        if not os.path.exists(path):
            errmsg = "Could not find config file!"
            logging.error(errmsg)
            sys.exit(errmsg)

        self.data = toml.load(open(path, "r"))
        self.games = {data["id"]: data for data in self.data["games"]}

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError(name)

    def get(self, *args):
        return self.data.get(*args)

config = Conf()
