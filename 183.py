api_request = request.get("https://restcountries.eu/rest/v2/capital/paris" + city_entry.get())
api_output_json = json.loads(api_request.content)
api_output_json[0]['name']