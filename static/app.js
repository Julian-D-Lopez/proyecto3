// static/app.js
document.addEventListener("DOMContentLoaded", () => {
  // Inicializar mapa centrado en Bogotá (ajusta coords si quieres)
  const map = L.map("map").setView([4.575, -74.14], 13);

  // Capa base (OpenStreetMap)
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  let localidadLayer = L.geoJSON(null);
  let sitpLayer = L.layerGroup();

  // Referencias a controles
  const chkLocalidad = document.getElementById("chkLocalidad");
  const chkSitp = document.getElementById("chkSitp");
  const selectorInfo = document.getElementById("selectorInfo");
  const infoBox = document.getElementById("infoBox");

  // Función para obtener JSON de la API
  async function fetchJSON(url) {
    const resp = await fetch(url);
    if (!resp.ok) throw new Error(`HTTP ${resp.status} - ${resp.statusText}`);
    return await resp.json();
  }

  // Cargar localidad (polígono)
  fetchJSON("/api/localidad")
    .then(geojson => {
      localidadLayer = L.geoJSON(geojson, {
        style: { color: "#2c7fb8", weight: 2, fillOpacity: 0.2 }
      }).addTo(map);
      // Ajusta la vista al polígono
      map.fitBounds(localidadLayer.getBounds());
    })
    .catch(err => console.error("Error cargando localidad:", err));

  // Cargar SITP (puntos)
  fetchJSON("/api/sitp")
    .then(data => {
      sitpLayer = L.geoJSON(data, {
        pointToLayer: (feature, latlng) => {
          return L.marker(latlng);
        },
        onEachFeature: (feature, layer) => {
          const p = feature.properties || {};
          const popup = `<b>${p.nombre || "Paradero"}</b><br/>Ruta: ${p.ruta || "-"}`;
          layer.bindPopup(popup);
        }
      }).addTo(map);
    })
    .catch(err => console.error("Error cargando SITP:", err));

  // Cargar info general
  fetchJSON("/api/info")
    .then(info => {
      // cuando el usuario seleccione "general", mostraremos esta info
      selectorInfo.addEventListener("change", () => {
        if (selectorInfo.value === "general") {
          infoBox.innerHTML = `
            <h4>${info.nombre}</h4>
            <p>${info.descripcion}</p>
            <p><b>Área:</b> ${info.area}</p>
            <p><b>Población:</b> ${info.poblacion}</p>
            <ul>${(info.caracteristicas || []).map(c => `<li>${c}</li>`).join("")}</ul>
          `;
        } else {
          infoBox.innerHTML = "";
        }
      });
    })
    .catch(err => console.error("Error cargando info:", err));

  // Checkbox handlers
  chkLocalidad.addEventListener("change", () => {
    if (chkLocalidad.checked) {
      localidadLayer.addTo(map);
    } else {
      map.removeLayer(localidadLayer);
    }
  });

  chkSitp.addEventListener("change", () => {
    if (chkSitp.checked) {
      sitpLayer.addTo(map);
    } else {
      map.removeLayer(sitpLayer);
    }
    
  });
  
});