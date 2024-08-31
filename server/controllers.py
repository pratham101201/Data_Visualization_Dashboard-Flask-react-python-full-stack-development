from flask import jsonify
from models import ReportModel
from db import db


# Function to get all the data
def get_all_data():
    try:
        all_data = ReportModel.query.all()
        if not all_data:
            return jsonify(success=False, message="No data found"), 400
        return jsonify(success=True, message="All data", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by year
def filtered_by_year(year):
    try:
        if len(year) != 4:
            return jsonify(success=False, message="Invalid year"), 400
        all_data = ReportModel.query.filter(
            (ReportModel.start_year == year) | 
            (ReportModel.end_year == year) | 
            (ReportModel.published.like(f"%{year}%")) | 
            (ReportModel.added.like(f"%{year}%"))
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by year {year}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by topic
def filtered_by_topic(topic):
    try:
        if len(topic) < 3:
            return jsonify(success=False, message="Invalid topic"), 400
        all_data = ReportModel.query.filter(
            ReportModel.topic.like(f"%{topic}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by topic: {topic}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by title
def filtered_by_title(title):
    try:
        if len(title) < 3:
            return jsonify(success=False, message="Invalid title"), 400
        all_data = ReportModel.query.filter(
            ReportModel.title.like(f"%{title}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by title: {title}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by sector
def filtered_by_sector(sector):
    try:
        if len(sector) < 3:
            return jsonify(success=False, message="Invalid sector"), 400
        all_data = ReportModel.query.filter(
            ReportModel.sector.like(f"%{sector}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by sector: {sector}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by region
def filtered_by_region(region):
    try:
        if len(region) < 3:
            return jsonify(success=False, message="Invalid region"), 400
        all_data = ReportModel.query.filter(
            ReportModel.region.like(f"%{region}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by region: {region}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by country
def filtered_by_country(country):
    try:
        if len(country) < 3:
            return jsonify(success=False, message="Invalid country"), 400
        all_data = ReportModel.query.filter(
            ReportModel.country.like(f"%{country}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by country: {country}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by pestle
def filtered_by_pestle(pestle):
    try:
        if len(pestle) < 3:
            return jsonify(success=False, message="Invalid pestle"), 400
        all_data = ReportModel.query.filter(
            ReportModel.pestle.like(f"%{pestle}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by pestle: {pestle}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by source
def filtered_by_source(source):
    try:
        if len(source) < 3:
            return jsonify(success=False, message="Invalid source"), 400
        all_data = ReportModel.query.filter(
            ReportModel.source.like(f"%{source}%")
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by source: {source}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by intensity
def filtered_by_intensity(intensity):
    try:
        all_data = ReportModel.query.filter(
            ReportModel.intensity == int(intensity)
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by intensity: {intensity}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

# Function to get data filtered by likelihood
def filtered_by_likelihood(likelihood):
    try:
        all_data = ReportModel.query.filter(
            ReportModel.likelihood == int(likelihood)
        ).all()
        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400
        return jsonify(success=True, message=f"Filtered by likelihood: {likelihood}", data=[data.to_dict() for data in all_data]), 200
    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500

def filtered_by_any(search):
    try:
        if len(search) < 3:
            return jsonify(success=False, message="Invalid search"), 400

        all_data = ReportModel.query.filter(
            (ReportModel.title.like(f"%{search}%")) |
            (ReportModel.sector.like(f"%{search}%")) |
            (ReportModel.region.like(f"%{search}%")) |
            (ReportModel.country.like(f"%{search}%")) |
            (ReportModel.pestle.like(f"%{search}%")) |
            (ReportModel.source.like(f"%{search}%")) |
            (ReportModel.insight.like(f"%{search}%")) |
            (ReportModel.url.like(f"%{search}%")) |
            (ReportModel.end_year.like(f"%{search}%")) |
            (ReportModel.start_year.like(f"%{search}%")) |
            (ReportModel.impact.like(f"%{search}%")) |
            (ReportModel.added.like(f"%{search}%")) |
            (ReportModel.published.like(f"%{search}%")) |
            (ReportModel.relevance.like(f"%{search}%")) |
            (ReportModel.likelihood.like(f"%{search}%")) |
            (ReportModel.intensity.like(f"%{search}%"))
        ).all()

        if not all_data:
            return jsonify(success=False, message="No Data Found"), 400

        return jsonify(success=True, message=f"Filtered by any: {search}", data=[data.to_dict() for data in all_data]), 200

    except Exception as e:
        return jsonify(success=False, message="Internal Server Error"), 500