let item = "";
let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");

btn1.addEventListener("click", function () {
   if (tg.MainButton.isVisible) {
      tg.MainButton.hide();
   }
   else {
      tg.MainButton.setText("Бесполезная кнопка 1");
      item = "1";
      tg.MainButton.show();
   }
});

btn2.addEventListener("click", function () {
   if (tg.MainButton.isVisible) {
      tg.MainButton.hide();
   }
   else {
      tg.MainButton.setText("Бесполезная кнопка 2");
      item = "2";
      tg.MainButton.show();
   }
});

Telegram.WebApp.onEvent("mainButtonClicked", function () {
   if (item === "1") {
      window.open("https://doka.guide/js/window-open/", "_blank");
   } else {
      tg.sendData();
   }
});
