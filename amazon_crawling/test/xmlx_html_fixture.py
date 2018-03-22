
class Xmlx_html_fixture



Sample data

response = requests.get(url)
lxml.html.fromstring(response.text)
