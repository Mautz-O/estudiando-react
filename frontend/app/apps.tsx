import { useState } from "react";


function Mensaje() {
    const [Mensaje, setMensaje] = useState("");


    async function cargarUsuario() {
        const response = await fetch("http://127.0.0.1:8000/openrouter", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: "Hello, OpenRouter!"
            })
        });
        const data = await response.json();
        setMensaje(data.answer);
        console.log(data);







    }

    return (
        <div>

            <p>{Mensaje}</p>

            <button onClick={cargarUsuario}>click</button>

        </div>

    )

}

export default Mensaje;


