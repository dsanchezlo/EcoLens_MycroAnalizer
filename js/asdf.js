document.getElementById('startStreaming').addEventListener('click', function(){
  const imageElement = document.getElementById('image');
  const imageUrl = "http://192.168.137.103/640x480.jpg";
  const interval = 1000;

  imageElement.src = imageUrl;

  function changeImage() {
      //imageElement.src = imageUrl;
      const timestamp = new Date().getTime();
      imageElement.src = `${imageUrl}?timestamp=${timestamp}`;
  }

  // Initialen Bildwechsel aufrufen
  changeImage();

  // Wiederhole den Bildwechsel in regelmäßigen Abständen
  intervalID = setInterval(changeImage, interval);
});

document.getElementById('stopStreaming').addEventListener('click', function() {
  // Intervall mit dem gespeicherten Verweis löschen
  clearInterval(intervalID);
});



<script>
  document.getElementById('startStreaming').addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    var pathimg = "/imageStreaming"; // Hier den gewünschten Pfad eintragen
    xhr.open("GET", path, true);

    xhr.onload = function() {
        if (xhr.status === 200) {
            alert("GET-Anfrage erfolgreich.");
        } else {
            alert("Fehler bei der GET-Anfrage.");
        }
    };

    xhr.send();
  });
</script>



<!DOCTYPE html>
<html>
<head>
    <title>Imagen nueva desde URL externa</title>
</head>
<body>
    <button id="enviarBtn">Send POST</button>
    <button id="startStreaming">Start streaming</button>
    <button id="stopStreaming">End Streaming</button>
    <h1>Automatischer Bildwechsel</h1>
      <img id="image" alt="Bild von externer URL">


    <script>
      document.getElementById('enviarBtn').addEventListener('click', function() {
                // Datos que deseas enviar en la solicitud POST <script src="js/scripts.js"></script>
                var datos = { mensaje: "flashON" };

                // Convierte los datos a una cadena JSON
                var jsonDatos = JSON.stringify(datos);

                // Configura la solicitud POST
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "/", true);
                xhr.setRequestHeader("Content-Type", "application/json");

                // Maneja la respuesta de la solicitud POST
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        alert("Solicitud POST exitosa");
                    } else {
                        alert("Error en la solicitud POST");
                    }
                };

                // Envía la solicitud POST con los datos
                xhr.send(jsonDatos);
            });
    </script>

</body>
</html>
