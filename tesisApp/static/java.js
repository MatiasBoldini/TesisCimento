
console.log("El script java.js se está ejecutando correctamentes.");

function moveToNextInput(currentInput, nextInputName) {
    if (currentInput.value.length == currentInput.maxLength) {
        var nextInput = document.getElementsByName(nextInputName)[0];
        if (nextInput) {
            nextInput.focus();
        }
    }

    // Verificar si todos los campos están llenos
    var inputs = document.querySelectorAll('input[name^="input"]');
    var allFilled = true;
    inputs.forEach(function(input) {
        if (input.value.length !== input.maxLength) {
            allFilled = false;
        }
    });

    // Cambiar el color del borde dependiendo del estado de llenado
    inputs.forEach(function(input) {
        if (!allFilled) {
            input.style.borderColor = 'red'; // Si falta al menos un dato, borde rojo en todos los campos
        } else {
            input.style.borderColor = "#019fda"; // Si todos los campos están llenos, borde verde en todos los campos
        }
    });

    // Mostrar u ocultar el mensaje de código incorrecto
    var codigoIncorrecto = document.getElementById('codigo-incorrecto');
    if (!allFilled) {
        codigoIncorrecto.style.display = 'block';
    } else {
        codigoIncorrecto.style.display = 'none';
    }
}



$(document).ready(function(){
    $('#fecha-entrega').datepicker({
      format: 'dd/mm/yyyy', // Establece el formato de la fecha
      autoclose: true // Cierra automáticamente el calendario después de seleccionar la fecha
    });
  });


// Map de ubicación



src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"
src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"