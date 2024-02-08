$(document).ready(function() {
  function getTranslation() {
      var languageCode = $("#language_code").val();
      var api_url = "https://hellosalut.stefanbohacek.dev/?lang=" + languageCode;

      $.get(api_url, function(data) {
          $("#hello").text(data.hello);
      });
  }

  $("#btn_translate").click(getTranslation);

  $("#language_code").keypress(function(event) {
      if (event.keyCode === 13) {
          event.preventDefault();
          getTranslation();
      }
  });
});
