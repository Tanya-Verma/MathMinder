const API = "http://127.0.0.1:8000";

async function solve() {
  let q = document.getElementById("input").value;

  let res = await fetch(`${API}/solve?q=${q}`);
  let data = await res.json();

  document.getElementById("output").innerText =
    data.explanation;
}

async function upload() {
  let file = document.getElementById("file").files[0];

  let form = new FormData();
  form.append("file", file);

  let res = await fetch(`${API}/solve-image`, {
    method: "POST",
    body: form
  });

  let data = await res.json();

  document.getElementById("output").innerText =
    data.explanation;
}