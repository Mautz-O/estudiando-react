import { useState, useEffect } from "react";


function Mensaje() {
    const [Mensaje, setMensaje] = useState("");

    useEffect(() => {
        async function cargarUsuario() {
            const response = await fetch("http://127.0.0.1:8000/hello");
            const data = await response.json();
            setMensaje(data.message);
            console.log(data);
        }


        console.log();
        cargarUsuario();
    }, []);

    return (
        <p>{Mensaje}</p>

    )
}

export default Mensaje;