import express from "express";

const app = express();
const PORT = 3000;

app.use(express.json());

//creamos nuestra primera ruta
app.get("/api/test", function(request, response) {
    response.json({ok: true, message: "Mi API funciona!!!" });
});

app.listen(PORT, function() {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});