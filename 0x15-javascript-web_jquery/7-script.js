var api_url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
$.get(api_url, function (data) {
  $('#character').text(data.name)
});
