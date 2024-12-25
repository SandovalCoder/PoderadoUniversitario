// Variables globales
let datos = [];

// Referencias a elementos del DOM
const nombreContainer = document.getElementById("nombre-container");
const calculadoraContainer = document.getElementById("calculadora-container");
const bienvenida = document.getElementById("bienvenida");
const tablaNotas = document.getElementById("tabla-notas");
const totalPesoEl = document.getElementById("total-peso");
const resultadoEl = document.getElementById("resultado");

// Botón para continuar
document.getElementById("continuar").addEventListener("click", () => {
    const nombre = document.getElementById("nombre").value.trim();
    if (nombre === "") {
        alert("Por favor, ingrese su nombre.");
        return;
    }

    // Mostrar calculadora y personalizar mensaje
    bienvenida.textContent = `Bienvenido, ${nombre}!`;
    nombreContainer.style.display = "none";
    calculadoraContainer.style.display = "block";
});

// Botón para agregar nota
document.getElementById("agregar").addEventListener("click", () => {
    const nota = parseFloat(document.getElementById("nota").value);
    const peso = parseFloat(document.getElementById("peso").value);

    // Validaciones
    if (isNaN(nota) || nota < 0 || nota > 20) {
        alert("La nota debe ser un número entre 0 y 20.");
        return;
    }
    if (isNaN(peso) || peso <= 0 || peso > 100) {
        alert("El peso debe ser un número mayor a 0 y menor o igual a 100.");
        return;
    }
    const pesoTotal = datos.reduce((sum, dato) => sum + dato.peso, 0);
    if (pesoTotal + peso > 100) {
        alert(`El peso total no puede exceder 100%. Peso actual: ${pesoTotal}%.`);
        return;
    }

    // Agregar datos
    datos.push({ nota, peso });
    actualizarTabla();
    limpiarInputs();
});

// Botón para calcular promedio
document.getElementById("calcular").addEventListener("click", () => {
    const pesoTotal = datos.reduce((sum, dato) => sum + dato.peso, 0);
    if (pesoTotal === 0) {
        resultadoEl.textContent = "No hay datos para calcular el promedio.";
        return;
    }

    const promedio = datos.reduce((sum, dato) => sum + dato.nota * dato.peso, 0) / pesoTotal;
    resultadoEl.textContent = `El promedio ponderado es: ${promedio.toFixed(2)}`;
});

// Actualizar tabla
function actualizarTabla() {
    tablaNotas.innerHTML = "";
    let pesoTotal = 0;

    datos.forEach((dato, index) => {
        pesoTotal += dato.peso;
        const row = `
            <tr>
                <td>${dato.nota}</td>
                <td>${dato.peso}%</td>
            </tr>
        `;
        tablaNotas.innerHTML += row;
    });

    totalPesoEl.textContent = `${pesoTotal}%`;
}

// Limpiar inputs
function limpiarInputs() {
    document.getElementById("nota").value = "";
    document.getElementById("peso").value = "";
}
