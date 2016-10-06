import os
import json
import newspaper
import time

# http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python
import logging
import logging.config
logger = logging.getLogger(__name__)

def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()


url = 'http://cnn.com'
DATA_FILENAME = 'cnn.json'

paper = newspaper.build(url, memoize_articles=False)

done = 0
start = time.time()

articles = []
for article in paper.articles:
    article.download()
    article.parse()
    articles.append({
        'url': article.canonical_link,
        'title': article.title,
        'text': article.text,
    })
    logger.info(article.title)
    done += 1
    if done % 10 == 0:
        end = time.time()
        logger.info('Done ' + str(done) + ' in ' + str((end - start)))

with open(DATA_FILENAME,'w') as outfile:
    json.dump(articles, outfile, indent=2)

