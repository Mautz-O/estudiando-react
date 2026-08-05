import { useState } from "react";


function Mensaje() {
    const [Mensaje, setMensaje] = useState("");


    async function cargarUsuario() {
        const response = await fetch("http://127.0.0.1:8000/hello");
        const data = await response.json();
        setMensaje(data.message);
        console.log(data);





        console.log();
        cargarUsuario();
    }

    return (
        <div>

            <p>{Mensaje}</p>

            <button onClick={cargarUsuario}>click</button>

        </div>

    )

}

export default Mensaje;


