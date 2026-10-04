import { useState } from "react";


function Mensaje() {
    const [Mensaje, setMensaje] = useState("");
    const [mensajeUsuario, setMensajeUsuario] = useState("");


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
        <div style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            textAlign: "center",
            minHeight: "30vh",
            gap: "12px"
        }}>
            <p>{Mensaje}</p>
            <button
                onClick={cargarUsuario}
                style={{
                    background: "linear-gradient(135deg, #e5465b 0%, #ed3a3a 100%)",
                    color: "white",
                    border: "none",
                    borderRadius: "999px",
                    padding: "0.9rem 1.8rem",
                    fontSize: "1.05rem",
                    fontWeight: 700,
                    cursor: "pointer",
                    boxShadow: "0 10px 25px rgba(70, 229, 91, 0.35)",
                    transition: "transform 0.2s ease, box-shadow 0.2s ease, opacity 0.2s ease",
                }}
            >
                click
            </button>
        </div>
    )

}

export default Mensaje;


