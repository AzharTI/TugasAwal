function toggleTheme() {
    document.body.classList.toggle('dark-mode')

    if(document.body.classList.contains("dark-mode")) {
        tema.textContent = "Mode Terang"
    }
    else {
        tema.textContent = "Mode Gelap"
    }
}

function sapaUser() {
        const Nama = document.getElementById("Nama").value;

    if (Nama === "") {
        document.getElementById("hasil").textContent =
            "Masukkin nama dulu ya!";
    } else {
        document.getElementById("hasil").textContent =
            "Hai, " + Nama + "!";
    }
}