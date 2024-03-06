



const hamBurger = document.querySelector(".toggle-btn");
let logoExpanded = false; // Estado inicial

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");

  var logoElement = document.querySelector('.navbar-brand.my-logo');

  // Cambiar el estado y aplicar el estilo correspondiente
  logoExpanded = !logoExpanded;

  if (logoExpanded) {
    // Logo expandido
    logoElement.style.transition = 'margin-left 0.5s ease-in-out';
    logoElement.style.marginLeft = '0';
  } else {
    // Logo en posición original
    logoElement.style.transition = 'margin-left 0.5s ease-in-out';
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
      parte2.style.left = '-50%';
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



// $(document).ready(function(){
//     $('#fecha-entrega').datepicker({
//       format: 'dd/mm/yyyy', // Establece el formato de la fecha
//       autoclose: true // Cierra automáticamente el calendario después de seleccionar la fecha
//     });
//   });


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


// ========= CALENDAR =============

let currentMonth = document.querySelector(".current-month");
let calendarDays = document.querySelector(".calendar-days");
let today = new Date();
let date = new Date();


currentMonth.textContent = date.toLocaleDateString("en-EN", {month:'long', year:'numeric'});
today.setHours(0,0,0,0);
renderCalendar();

function renderCalendar() {
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();
    const totalMonthDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    const startWeekDay = new Date(date.getFullYear(), date.getMonth(), 0).getDay();

    calendarDays.innerHTML = "";

    let totalCalendarDay = 6 * 7;
    for (let i = 0; i < totalCalendarDay; i++) {
        let day = i - startWeekDay;

        if (i <= startWeekDay) {
            // adding previous month days
            calendarDays.innerHTML += `<div class="prev-month">${prevLastDay - i}</div>`;
        } else if (i <= startWeekDay + totalMonthDay) {
            // adding this month days
            date.setDate(day);
            date.setHours(0, 0, 0, 0);

            let dayClass = date.getTime() === today.getTime() ? 'current-day' : 'month-day';
            calendarDays.innerHTML += `<div class="${dayClass}">${day}</div>`;
        } else {
            // adding next month days
            calendarDays.innerHTML += `<div class="next-month">${day - totalMonthDay}</div>`;
        }
    }



    addDayClickListeners();
}

function addDayClickListeners() {
    document.querySelectorAll(".month-day, .current-day").forEach(function (element) {
        element.addEventListener("click", function () {
            // Remover la clase de selección y current-day de todos los días
            document.querySelectorAll(".month-day").forEach(function(day) {
                day.classList.remove("selected-day");
                day.classList.remove("current-day");
            });

            // Agregar la clase de selección al día actual
            element.classList.add("selected-day");

            

            // Obtener la fecha del día seleccionado
            const dayOfMonth = parseInt(element.textContent);
            const selectedDate = new Date(date.getFullYear(), date.getMonth(), dayOfMonth);

            // Formatear la fecha a YYYY-MM-DD
            const formattedDate = selectedDate.toISOString().split('T')[0];

            // Mostrar la fecha en la consola
            console.log("Fecha seleccionada:", formattedDate);
            
            var xhr = new XMLHttpRequest();

            // Configurar la solicitud con el método y la URL
            xhr.open('POST', 'calendarioPedidos', true);
            
            // Configurar los encabezados necesarios (incluyendo CSRF token)
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            // Configurar la función de devolución de llamada para manejar la respuesta
            xhr.onload = function () {
                if (xhr.status >= 200 && xhr.status < 300) {
                    // Manejar la respuesta (puedes hacer algo si es necesario)
                    console.log("Datos enviados");
                } else {
                    // Manejar errores
                    console.error("Error en la solicitud:", xhr.statusText);
                }
            };

            // Enviar la solicitud con los datos del cuerpo
            xhr.send('fecha=' + formattedDate);


        });
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Buscar la cookie por el nombre
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



// Enviar AJAX solo si se hace clic en un día
            // $.ajax({
            //     type: "GET",
            //     url: "/pedidos/obtenerPedidos",
            //     data: {
            //         fechaSeleccionada: formattedDate
            //     },
            //     success: function (response) {
                    
            //         // Realizar alguna acción adicional con la respuesta
            //         console.log("Datos enviados correctamente al servidor.");
            //         window.location.href = "/pedidos/mostrarGrilla";
            
            //     },
            //     error: function (error) {
            //         // Manejar el error si ocurre
            //         console.error(error);
            //     }
            // });




document.querySelectorAll(".month-day").forEach(function (element) {
    element.addEventListener("click", function () {
        // Remover la clase de selección de todos los días
        document.querySelectorAll(".month-day").forEach(function(day) {
            day.classList.remove("selected-day");
        });

        // Agregar la clase de selección al día actual
        element.classList.add("selected-day");

        // Obtener la fecha del día seleccionado
        const dayOfMonth = parseInt(element.textContent);
        const selectedDate = new Date(date.getFullYear(), date.getMonth(), dayOfMonth);
        
        // Formatear la fecha a YYYY-MM-DD
        const formattedDate = selectedDate.toISOString().split('T')[0];

        // Mostrar la fecha en la consola
        //console.log("Fecha seleccionada:", formattedDate);
    });
});

document.querySelectorAll(".month-btn").forEach(function (element) {
	element.addEventListener("click", function () {
		date = new Date(currentMonth.textContent);
        date.setMonth(date.getMonth() + (element.classList.contains("prev") ? -1 : 1));
		currentMonth.textContent = date.toLocaleDateString("en-US", {month:'long', year:'numeric'});
		renderCalendar();
	});
});

// document.querySelectorAll(".btn").forEach(function (element) {
// 	element.addEventListener("click", function () {
//         let btnClass = element.classList;
//         date = new Date(currentMonth.textContent);
//         if(btnClass.contains("today"))
//             date = new Date()
//         else if(btnClass.contains("prev-year"))
//             date = new Date(date.getFullYear()-1, 0, 1);
//         else
//             date = new Date(date.getFullYear()+1, 0, 1);

// 		currentMonth.textContent = date.toLocaleDateString("en-US", {month:'long', year:'numeric'});
// 		renderCalendar();
// 	});
// });

document.querySelectorAll(".btn").forEach(function (element) {
    element.addEventListener("click", function () {
        let btnClass = element.classList;
        date = new Date(currentMonth.textContent);

        if (btnClass.contains("today")) {
            date = new Date();
            // window.location.href = "/pedidos/";
        } else if (btnClass.contains("prev-year")) {
            date = new Date(date.getFullYear() - 1, 0, 1);
        } else {
            date = new Date(date.getFullYear() + 1, 0, 1);
        }

        currentMonth.textContent = date.toLocaleDateString("en-US", { month: 'long', year: 'numeric' });
        renderCalendar();
    });
});



document.getElementById("volverBtn").addEventListener("click", function() {
    window.location.href = "/pedidos/";
});







console.log("El script java.js se está ejecutando correctamente.");

src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"
src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"