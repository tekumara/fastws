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
    <div class="grid grid-flow-row-dense grid-cols-3 grid-rows-2">
      <span>Email</span><textarea id="username" class="border-2 rounded" placeholder="name"></textarea>
      <button
        class="px-5 py-1 text-sm text-purple-600 font-semibold rounded-full border border-purple-200 hover:text-white hover:bg-purple-600 hover:border-transparent"
        onClick={() => ws.send(document.getElementById("username").value)}
      >
        Send
      </button>
      <div class="col-span-3 text-center">{message()}</div>
    </div>
  );
};

export default App;
