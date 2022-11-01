import json
import httpx

from schemas.schemas import University

url = 'http://universities.hipolabs.com/search'


def get_all_universities_for_country(country: str) -> dict:
    params = {'country': country}
    with httpx.Client() as client:
        response = client.get(url, params=params)
        response_json = json.loads(response.text)
    universities = []
    for university in response_json:
        university_obj = University.parse_obj(university)
        universities.append(university_obj)
    return {country: universities}
