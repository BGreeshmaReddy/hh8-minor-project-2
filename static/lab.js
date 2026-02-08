const out = document.getElementById("output");

async function upload() {
    let f = document.getElementById("file").files[0];
    let fd = new FormData();
    fd.append("file", f);

    let r = await fetch("/step/upload", {method:"POST", body:fd});
    out.textContent = await r.text();
}

async function normalDelete() {
    let r = await fetch("/step/normal-delete", {method:"POST"});
    out.textContent = await r.text();
}

async function encrypt() {
    let r = await fetch("/step/encrypt", {method:"POST"});
    out.textContent = await r.text();
}

async function overwrite() {
    let r = await fetch("/step/overwrite", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({level:"medium"})
    });
    out.textContent = await r.text();
}

async function audit() {
    let r = await fetch("/step/audit");
    out.textContent = await r.text();
}
