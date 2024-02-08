api_url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$.get(api_url, function (data) {
  $('#hello').text(data.hello)
});
