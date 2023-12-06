const fileInput = document.getElementById('fileInput');
const downloadButton = document.getElementById('downloadButton');
const filenameInput = document.getElementById('filenameInput');
const imgElement = document.getElementById('imageElement');
var on = false;

downloadButton.addEventListener('click', () => {
  const imageSource = imgElement.src;
  const userFilename = filenameInput.value || 'EcoLens_MycroAnalizer_muestra.jpg';

  //userFilename = userFilename.replace(/[^\w\s.-áéíóúÁÉÍÓÚüÜñÑ]/g, '');

  // Zeige eine Bestätigungsbox an
  const confirmDownload = window.confirm(`La imagen se descargará bajo el siguiente nombre: "${userFilename}" \n desea continuar?`);

  if (confirmDownload) {
    const link = document.createElement('a');
    link.href = imageSource;
    link.download = userFilename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

});

async function loadModelOptions() {
  const data = await (await fetch('/env.json')).json();
  console.log(data)
  const select = document.getElementById("modelSelection")
  Object.keys(data).forEach(key => {
    let option = document.createElement("option");
    // Set the text and value of the option
    option.text = key;
    option.value = key;
    // Append the option to the select element
    select.appendChild(option);
  });
}

document.getElementById('startStreaming').addEventListener('click', function () {
  const interval = 100;
  // Start fetching the stream and displaying it
  const modelSelected = document.getElementById("modelSelection")
  var selectedModel = (modelSelected.options[modelSelected.selectedIndex]).value;
  console.log(selectedModel)
  var streamUrl = `http://127.0.0.1:5000/model/${selectedModel}`; // Hier den gewünschten Pfad eintragen
  imgElement.src = streamUrl
});

document.getElementById('stopStreaming').addEventListener('click', function () {
  // Intervall mit dem gespeicherten Verweis löschen
  clearInterval(intervalID);
  on = false;
});

document.getElementById('enviarBtn').addEventListener('click', function () {
  // Datos que deseas enviar en la solicitud POST
  var datos = { mensaje: "flashON" };
  var pathflash = "/flash";
  // Convierte los datos a una cadena JSON
  var jsonDatos = JSON.stringify(datos);

  // Configura la solicitud POST
  var xhr = new XMLHttpRequest();
  xhr.open("POST", pathflash, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  // Maneja la respuesta de la solicitud POST
  xhr.onload = function () {
    if (xhr.status === 200) {
      //alert("Flash activated");
    } else {
      alert("Error en la solicitud POST");
    }
  };

  // Envía la solicitud POST con los datos
  xhr.send(jsonDatos);
});

loadModelOptions()
