import type { Component } from "solid-js";
import { createSignal } from "solid-js";

const App: Component = () => {
  const [message, setMessage] = createSignal("");

  // open websocket
  const ws = new WebSocket("ws://localhost:8000/ws/send-notification/solid.io");
  ws.onmessage = (ev) => {
    const recv = JSON.parse(ev.data);
    console.log(recv);
    setMessage(recv.message);
  };

  return (
    <div>
      Email user: <textarea id="username"></textarea>
      <br />
      <br />
      <button
        onClick={() => ws.send(document.getElementById("username").value)}
      >
        Send
      </button>
      <br />
      Server message: {message()}
    </div>
  );
};

export default App;
