const $ = window.$;
$(document).ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const hello = $('DIV#hello');
  const translateBtn = $('INPUT#btn_translate');
  const lang = $('INPUT#language_code');

  translateBtn.click(() => {
    $.get(url + lang.val(), (data) => {
      hello.text(data.hello);
    });
  });
});
