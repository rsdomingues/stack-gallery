import logging
from client import TechAnalytics

FORMAT = '%(name)s %(levelname)-5s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('stack')
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.INFO)
logging.getLogger('elasticsearch').setLevel(logging.ERROR)

ta = TechAnalytics()
ta.load_skill()