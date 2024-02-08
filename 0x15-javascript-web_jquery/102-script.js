$(document).ready(function() {
  $("#btn_translate").click(function() {
      var languageCode = $("#language_code").val();
      var api_url = "https://hellosalut.stefanbohacek.dev/?lang=" + languageCode;

      $.get(api_url, function(data) {
          $("#hello").text(data.hello);
      });
  });
});
