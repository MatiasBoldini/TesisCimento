
console.log("El script java.js se está ejecutando correctamentes.");

const hamBurger = document.querySelector(".toggle-btn");
let logoExpanded = false; // Estado inicial

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");

  var logoElement = document.querySelector('.navbar-brand.my-logo');

  // Cambiar el estado y aplicar el estilo correspondiente
  logoExpanded = !logoExpanded;

  if (logoExpanded) {
    // Logo expandido
    logoElement.style.transition = 'margin-left 0.7s ease-in-out';
    logoElement.style.marginLeft = '170px';
  } else {
    // Logo en posición original
    logoElement.style.transition = 'margin-left 0.7s ease-in-out';
    logoElement.style.marginLeft = '0px';
  }
});


const toggleBtn = document.querySelector('.toggle-btn');

const sidebarLogo = document.querySelector('.sidebar-logo');

const parte2 = document.querySelector('.parte2');
const body = document.body
let sidebarAbierto = false

toggleBtn.addEventListener('click', function() {
  this.classList.toggle('rotated');
  sidebarAbierto = !sidebarAbierto; // Cambia el estado

    if (sidebarAbierto) {
      // Si el sidebar está abierto, mostrarlo
      parte2.style.left = '0';
      parte2.style.transition = 'left 0.7s ease-in-out';
      body.style.overflow = "hidden"
    } else {
      // Si el sidebar está cerrado, ocultarlo
      parte2.style.left = '-100%';
      parte2.style.transition = 'left 0.7s ease-in-out';
      body.style.overflow= "visible"
    }
});



//sidebar






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


function iniciarMap(){
    var coord = {lat:-34.5956145 ,lng: -58.4431949};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}



// 



src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"
src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"