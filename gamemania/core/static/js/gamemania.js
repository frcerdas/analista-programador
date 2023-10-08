document.addEventListener("DOMContentLoaded", function () {
  // Consumo API https://mindicador.cl/api
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "https://mindicador.cl/api", true);
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Ok
      var response = JSON.parse(xhr.responseText);
      // response es body
      // Fecha
      var fecha = moment(response.dolar.fecha);
      var ahora = moment();
      var diferencia = ahora.diff(fecha, "days");
      var mensaje = "";
      if (diferencia < 1) {
        mensaje = ahora.from(fecha);
      } else {
        mensaje = "hace " + diferencia + " día(s)";
      }
      var usdSinceSpan = document.getElementById("usd-since");
      usdSinceSpan.innerHTML = mensaje;
      // Valor del dólar actual (cámbialo por el valor real)
      var valorDolarActual = response.dolar.valor; // Ejemplo

      // Función para formatear un número como precio en peso chileno
      function formatearPrecioCLP(precioCLP) {
        // Formatear el número como precio en peso chileno (agregar separador de miles y símbolo "$")
        return "$" + precioCLP.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
      }

      var gamePriceCLP = document.querySelectorAll("span.game-price-clp");

      for (var i = 0; i < gamePriceCLP.length; i++) {
        var spanCLP = gamePriceCLP[i];
        var textoCLP = parseFloat(spanCLP.textContent);
        var valorUSD = textoCLP / valorDolarActual;
        var spanUSD = spanCLP.nextElementSibling;

        while (spanUSD && !spanUSD.classList.contains("game-price-usd")) {
          spanUSD = spanUSD.nextElementSibling;
        }

        if (spanUSD) {
          spanUSD.textContent = valorUSD.toFixed(2);

          // Formatear el valor en span.game-price-clp como peso chileno y actualizar el texto
          spanCLP.textContent = formatearPrecioCLP(textoCLP);
        }
      }
    } else {
      console.error(
        "Error al realizar la solicitud: Código de estado " + xhr.status
      );
    }
  };
  xhr.onerror = function () {
    console.error("Error de red al realizar la solicitud a la API.");
  };
  xhr.send();
});
