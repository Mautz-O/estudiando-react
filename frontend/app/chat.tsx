import { useState } from "react";

type Mensaje = {
    contenido: string;
    rol: "user" | "assistant";
};

function Chat() {
    const [Mensajes, setMensajes] = useState<Mensaje[]>([]);
    const [texto, setTexto] = useState("");
    async function enviarMensaje() {
        const mensajeUsuario = texto;

        setTexto("");
        const response = await fetch("http://127.0.0.1:8000/openrouter", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: mensajeUsuario
            })
        });
        const data = await response.json();
        setMensajes((mensajesActuales) => [
            ...mensajesActuales,
            {
                contenido: mensajeUsuario,
                rol: "user"
            },

            {
                contenido: data.answer,
                rol: "assistant"
            }
        ]);
    }
    console.log(Mensajes);

    return (
        <div>
            <input
                value={texto}
                onChange={(e) => setTexto(e.target.value)}
            />

            < button onClick={enviarMensaje}>
                enviar
            </button >

            <div>
                {Mensajes.map((mensaje, index) => (
                    <p key={index}>
                        {mensaje.rol} : {mensaje.contenido}
                    </p>


                ))}
            </div>
        </div >
    );



}

export default Chat;