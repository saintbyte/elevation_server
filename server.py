#!/usr/bin/env python
from bottle import route, run, template, request, response
import srtm
@route('/ele')
def index():
  response.content_type = 'application/json; charset=utf-8'
  try:
      lat=request.query.lat
      lon=request.query.lon
  except:
      return "{'error':'empty'}"
  ele=elevation_data.get_elevation(lat, lon)
  s = "{'ele':"+str(ele)+",'lat':'"+lat+"','lon':'"+lon+"','src':'nasa_srtm','src_str':'Nasa SRTM'}"
  return s
elevation_data = srtm.get_data()
run(host='0.0.0.0', port=5007,server='paste') 