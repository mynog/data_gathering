import logging
import requests

logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrap_process(self, storage):

        api_url = 'https://api.opendota.com/api/proMatches'

        matches_limit = 1250
        api_param_value = 0
        scraped_matches = 0

        while scraped_matches < matches_limit:

            response = requests.get(api_url, {'less_than_match_id': api_param_value}) if scraped_matches != 0 \
                else requests.get(api_url)

            if not response.ok:
                logger.error(response.text)
            else:
                data = response.text

                line = ["{0}\t{1}".format(response.url, data.replace('\n', ''))]

                if scraped_matches == 0:
                    storage.write_data(line)
                else:
                    storage.append_data(line)

                scraped_matches += 100
                api_param_value = response.json()[-1]['match_id']
