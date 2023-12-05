// Warten, bis die Seite vollständig geladen ist
window.onload = function() {
    // Rufen Sie die Funktion zum Laden des Bildes auf
    loadInitialImage();
};

const fileInput = document.getElementById('fileInput');
const downloadButton = document.getElementById('downloadButton');
const filenameInput = document.getElementById('filenameInput');
const imgElement = document.getElementById('imageElement');
var on = false;

function loadInitialImage() {
    loadDefaultImage()
        .then(function(blob) {
            var imageUrl = URL.createObjectURL(blob);
            imgElement.src = imageUrl;
        })
        .catch(function(error) {
            alert(error);
        });
}

function loadDefaultImage() {
  var xhr = new XMLHttpRequest();
  var pathimg = "/defaultImage"; // Hier den gewünschten Pfad eintragen
  xhr.open("GET", pathimg, true);
  xhr.responseType = "blob"; // Daten als Binärdaten empfangen

  return new Promise(function(resolve, reject) {
    xhr.onload = function() {
      if (xhr.status === 200) {
        var blob = xhr.response; // Binärdaten des Bildes
        resolve(blob); // Die Blob-Daten auflösen, wenn die Anfrage erfolgreich ist
      } else {
        reject("Fehler bei der GET-Anfrage."); // Die Promise wird abgelehnt, wenn die Anfrage fehlschlägt
      }
    };

    xhr.send();
  });
}

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

function getImage() {
  var xhr = new XMLHttpRequest();
  var pathimg = "/imageStreaming"; // Hier den gewünschten Pfad eintragen
  xhr.open("GET", pathimg, true);
  xhr.responseType = "blob"; // Daten als Binärdaten empfangen

  return new Promise(function(resolve, reject) {
    xhr.onload = function() {
      if (xhr.status === 200) {
        var blob = xhr.response; // Binärdaten des Bildes
        resolve(blob); // Die Blob-Daten auflösen, wenn die Anfrage erfolgreich ist
      } else {
        reject("Fehler bei der GET-Anfrage."); // Die Promise wird abgelehnt, wenn die Anfrage fehlschlägt
      }
    };

    xhr.send();
  });
}

document.getElementById('startStreaming').addEventListener('click', function() {
  const interval = 100;

  //Verifica si ya se presionó el botón
  if (!on){
    on = true;
    function changeImage() {
      getImage()
        .then(function(blob) {
          var imageUrl = URL.createObjectURL(blob); // URL für das Bild erstellen
          imageElement.src = imageUrl
        })
        .catch(function(error) {
          alert(error);
        });
    }

    // Initialen Bildwechsel aufrufen
    changeImage();

    // Wiederhole den Bildwechsel in regelmäßigen Abständen
    intervalID = setInterval(changeImage, interval);
  }
});

document.getElementById('stopStreaming').addEventListener('click', function() {
  // Intervall mit dem gespeicherten Verweis löschen
  clearInterval(intervalID);
  on = false;
});

document.getElementById('enviarBtn').addEventListener('click', function() {
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
  xhr.onload = function() {
      if (xhr.status === 200) {
          //alert("Flash activated");
      } else {
          alert("Error en la solicitud POST");
      }
  };

  // Envía la solicitud POST con los datos
  xhr.send(jsonDatos);
});
