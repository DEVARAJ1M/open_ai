OPENAI_API_KEY = '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'


class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
      SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development' : DevelopmentConfig,
    'testing' : DevelopmentConfig,
    'production' : DevelopmentConfig
}