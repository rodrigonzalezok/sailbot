# SailBot
SailBot es un bot creado en Selenium para automatizar mensajes por Whatsapp muy ligero y fácil de implementar.

Para iniciar el bot simplemente debes instalar Selenium, las demás librerias utilizadas las tomas del OS, con el siguiente comando:

- pip install Selenium

Una vez instalado Selenium descargas todos los documentos y reemplazas en la función 'send_message()' el mensaje esperado y el que quieres recibir (dejé varios ejemplos debajo simulando una conversación para abrir una cuenta en X plataforma). Si quieres hacer el bot más dinámico recomiendo usar el json 'Diccionario' y agregarle frases esperadas o una variable extra al código que cuando una frase input no la reconozca pregunte qué quiso decir el interlocutor y de esa forma simular un aprendizaje.

Espero que te sea de utilidad, suerte!

P.D.: recomiendo no utilizar el bot si se esperan responder varios mensajes al mismo tiempo, lo probé con 12 personas y en determinado punto Whatsapp reconoce eso como SPAM y bloquean el número de Whatsapp por un día (es para que pagues por su API).
