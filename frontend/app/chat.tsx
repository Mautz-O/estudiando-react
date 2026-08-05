function Chat() {
    const [Mensajes, setMensajes] = React.useState<string[]>([]);
    const [texto, setTexto] = React.useState("");
    function enviarMensaje() {
        setMensajes([...Mensajes, texto]);
        setTexto("");
    }

    return (
        <div>
            <input
                value={texto}
                onChange={(e) => setTexto(e.target.value)}
            />

            < button > onClick={enviarMensaje}
                enviar
            </button >



        </div >
    );



}

