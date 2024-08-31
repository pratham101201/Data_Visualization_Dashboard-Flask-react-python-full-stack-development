from controllers import get_all_data, filtered_by_year, filtered_by_topic, filtered_by_title, filtered_by_sector, filtered_by_region, filtered_by_country, filtered_by_pestle, filtered_by_source, filtered_by_intensity, filtered_by_likelihood, filtered_by_any
from flask import Blueprint
api = Blueprint('api', __name__)

api.route('/data', methods=['GET'])(get_all_data)
api.route('/data/year/<year>', methods=['GET'])(filtered_by_year)
api.route('/data/topic/<topic>', methods=['GET'])(filtered_by_topic)
api.route('/data/title/<title>', methods=['GET'])(filtered_by_title)
api.route('/data/sector/<sector>', methods=['GET'])(filtered_by_sector)
api.route('/data/region/<region>', methods=['GET'])(filtered_by_region)
api.route('/data/country/<country>', methods=['GET'])(filtered_by_country)
api.route('/data/pestle/<pestle>', methods=['GET'])(filtered_by_pestle)
api.route('/data/source/<source>', methods=['GET'])(filtered_by_source)
api.route('/data/intensity/<intensity>', methods=['GET'])(filtered_by_intensity)
api.route('/data/likelihood/<likelihood>', methods=['GET'])(filtered_by_likelihood)
api.route('/data/search/<search>', methods=['GET'])(filtered_by_any)


